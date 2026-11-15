#!/usr/bin/env python3
"""Build the four geoblock set files from the aggregator output.

Usage (stdlib only, run with python3 -I):
  build-sets.py --csv geoip2-ipv4.csv --env .env \
                --blocklist <aggregated-multi-82countries-combined.txt> \
                --stripe ips_webhooks.txt [--ops ADDRESS ...] --out <dir>

Writes into --out:
  geo_allow.txt  the 82 countries' ranges, collapsed (from the GeoLite2 CSV)
  allow_ops.txt  Stripe webhook senders + any --ops addresses
  bl_single.txt  blocklist /32s
  bl_range.txt   blocklist ranges
  SHA256SUMS     checksums of the four files

Refuses (exit 1, writes nothing) if any floor below is not met. An empty or short geo_allow
blocks every visitor on the planet, so these floors are the first guard, not the only one.
"""
import argparse, csv, ipaddress, os, sys, tempfile, hashlib

FLOOR_COUNTRIES = 82        # codes in .env
FLOOR_GEO_ALLOW = 100_000   # ranges; 134,280 on 2026-11-03
FLOOR_STRIPE = 10           # Stripe publishes 15 today
FLOOR_BLOCKLIST = 300_000   # entries; 610,263 on 2026-11-03

def die(msg):
    print(f"REFUSED: {msg}. Nothing written.", file=sys.stderr); sys.exit(1)

ap = argparse.ArgumentParser()
for a in ("--csv", "--env", "--blocklist", "--stripe", "--out"): ap.add_argument(a, required=True)
ap.add_argument("--ops", nargs="*", default=[])
args = ap.parse_args()

codes = {l.split("=", 1)[1].strip() for l in open(args.env, encoding="utf-8")
         if l.startswith("COUNTRY_ISO_CODE_") and "=" in l}
if len(codes) < FLOOR_COUNTRIES: die(f"{len(codes)} country codes in {args.env}, need {FLOOR_COUNTRIES}")

rows, seen = [], set()
with open(args.csv, encoding="utf-8") as f:
    r = csv.DictReader(f)
    if "country_iso_code" not in (r.fieldnames or []): die(f"{args.csv} has no country_iso_code column")
    for row in r:
        cc = row["country_iso_code"]; seen.add(cc)
        if cc in codes: rows.append(ipaddress.ip_network(row["network"]))
missing = codes - seen
if missing: die(f"country codes not in the GeoLite2 CSV: {sorted(missing)}")
geo = list(ipaddress.collapse_addresses(rows))
if len(geo) < FLOOR_GEO_ALLOW: die(f"geo_allow has {len(geo)} ranges, floor {FLOOR_GEO_ALLOW}")

stripe = []
for l in open(args.stripe):
    l = l.strip()
    if l: stripe.append(ipaddress.ip_address(l))   # raises on HTML or junk: good
if len(stripe) < FLOOR_STRIPE: die(f"{len(stripe)} Stripe webhook addresses, floor {FLOOR_STRIPE}")
ops = [ipaddress.ip_address(x) for x in args.ops]

bl = []
for l in open(args.blocklist):
    l = l.strip()
    if l: bl.append(ipaddress.ip_network(l))
if len(bl) < FLOOR_BLOCKLIST: die(f"blocklist has {len(bl)} entries, floor {FLOOR_BLOCKLIST}")
single = [n for n in bl if n.prefixlen == 32]
rng = [n for n in bl if n.prefixlen < 32]

os.makedirs(args.out, exist_ok=True)
files = {
    "geo_allow.txt": [str(n) for n in geo],
    "allow_ops.txt": sorted({str(a) for a in stripe + ops}),
    "bl_single.txt": [str(n.network_address) for n in single],
    "bl_range.txt": [str(n) for n in rng],
}
sums = []
for name, lines in files.items():
    data = ("\n".join(lines) + "\n").encode()
    fd, tmp = tempfile.mkstemp(dir=args.out); os.write(fd, data); os.close(fd)
    os.replace(tmp, os.path.join(args.out, name))
    sums.append(f"{hashlib.sha256(data).hexdigest()}  {name}")
open(os.path.join(args.out, "SHA256SUMS"), "w").write("\n".join(sums) + "\n")
print(f"countries {len(codes)}  geo_allow {len(geo)}  allow_ops {len(files['allow_ops.txt'])}  "
      f"bl_single {len(single)}  bl_range {len(rng)}  -> {args.out}")
