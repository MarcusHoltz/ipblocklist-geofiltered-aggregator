#!/usr/bin/env python3
# Every-country allowlist check, offline.
# For every country in the GeoLite2 CSV (plus rows with no country), take up to 5 networks spread
# across that country's list, and test the first, middle and last address of each against
# geo_allow. Expected: allowed if and only if the country is one of the 82.
# Usage: countrycheck.py <geoip2-ipv4.csv> <.env> <geo_allow.txt> <samples_out.tsv>
import csv, ipaddress, bisect, sys, collections

csv_path, env_path, geo_path, out_path = sys.argv[1:5]
allowed = {l.split("=", 1)[1].strip() for l in open(env_path, encoding="utf-8")
           if l.startswith("COUNTRY_ISO_CODE_")}
assert allowed, "no COUNTRY_ISO_CODE_ lines"  # the count floor is build-sets.py FLOOR_COUNTRIES

by_cc = collections.defaultdict(list)
for r in csv.DictReader(open(csv_path, encoding="utf-8")):
    by_cc[r["country_iso_code"] or "(none)"].append(ipaddress.ip_network(r["network"]))

iv = sorted((int(n.network_address), int(n.broadcast_address))
            for n in (ipaddress.ip_network(l.strip()) for l in open(geo_path) if l.strip()))
m = []
for a, b in iv:
    if m and a <= m[-1][1] + 1: m[-1][1] = max(m[-1][1], b)
    else: m.append([a, b])
starts = [a for a, _ in m]
def in_geo(x):
    k = bisect.bisect_right(starts, x) - 1
    return k >= 0 and m[k][1] >= x

samples, fails = [], []
for cc, nets in sorted(by_cc.items()):
    nets.sort(key=lambda n: int(n.network_address))
    picks = sorted({round(i * (len(nets) - 1) / 4) for i in range(5)}) if len(nets) > 1 else [0]
    expect = "allow" if cc in allowed else "deny"
    for p in picks:
        n = nets[p]
        a, b = int(n.network_address), int(n.broadcast_address)
        for x in sorted({a, (a + b) // 2, b}):
            got = "allow" if in_geo(x) else "deny"
            ip = str(ipaddress.ip_address(x))
            samples.append((ip, cc, expect))
            if got != expect: fails.append((ip, cc, expect, got, str(n)))

with open(out_path, "w") as f:
    for s in samples: f.write("\t".join(s) + "\n")

in82 = [c for c in by_cc if c in allowed]
print(f"countries in CSV: {len(by_cc) - ('(none)' in by_cc)} (+ rows with no country: {len(by_cc.get('(none)', []))})")
print(f"of the {len(allowed)}, present in CSV: {len(in82)}; missing from CSV: {sorted(allowed - set(by_cc))}")
print(f"samples: {len(samples)} ({sum(s[2]=='allow' for s in samples)} expect allow, {sum(s[2]=='deny' for s in samples)} expect deny)")
print(f"FAILURES: {len(fails)}")
for f_ in fails[:40]: print("  ", *f_)
