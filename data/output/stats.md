# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-10-14 18:43:13 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 20.9
"Germany" : 3.3
"United Kingdom" : 2.0
"Canada" : 1.6
"South Korea" : 1.3
"Australia" : 0.7
"Other/Unfiltered" : 70.1
```

## Overall Summary

- **Total Input IPs:** 889,415
- **Countries Processed:** 6
- **Combined Unique IPs:** 265,760
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 29.88%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 128,498 | 126,625 | 185,687 | 20.88% | `aggregated-us-only.txt` |
| Canada | CA | 17,644 | 17,526 | 14,553 | 1.64% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 36,309 | 36,137 | 17,802 | 2.00% | `aggregated-gb-only.txt` |
| Australia | AU | 12,412 | 12,339 | 6,247 | 0.70% | `aggregated-au-only.txt` |
| Germany | DE | 30,255 | 30,145 | 29,490 | 3.32% | `aggregated-de-only.txt` |
| South Korea | KR | 3,979 | 3,956 | 11,981 | 1.35% | `aggregated-kr-only.txt` |

## IP Sources

- **Source 1:** https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level1.netset
- **Source 2:** https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level2.netset
- **Source 3:** https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt
- **Source 4:** https://raw.githubusercontent.com/borestad/blocklist-abuseipdb/main/abuseipdb-s100-30d.ipv4
- **Source 5:** https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt
- **Source 6:** https://raw.githubusercontent.com/stamparm/ipsum/master/levels/3.txt
- **Source 7:** https://www.spamhaus.org/drop/drop.txt
- **Source 8:** https://www.spamhaus.org/drop/edrop.txt
- **Source 9:** https://raw.githubusercontent.com/romainmarcoux/malicious-ip/refs/heads/main/full-300k-aa.txt
- **Source 10:** https://raw.githubusercontent.com/romainmarcoux/malicious-ip/refs/heads/main/full-300k-ab.txt
- **Source 11:** https://raw.githubusercontent.com/romainmarcoux/malicious-ip/refs/heads/main/full-300k-ac.txt
- **Source 12:** https://raw.githubusercontent.com/romainmarcoux/malicious-ip/refs/heads/main/full-300k-ad.txt
- **Source 14:** http://cinsscore.com/list/ci-badguys.txt
- **Source 15:** https://cdn.jsdelivr.net/gh/LittleJake/ip-blacklist/all_blacklist.txt

## Configuration Details

