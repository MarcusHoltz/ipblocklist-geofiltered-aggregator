# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-09-03 14:37:06 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 12.7
"Germany" : 3.3
"South Korea" : 2.3
"Canada" : 1.9
"United Kingdom" : 1.7
"Australia" : 0.8
"Other/Unfiltered" : 77.4
```

## Overall Summary

- **Total Input IPs:** 604,099
- **Countries Processed:** 6
- **Combined Unique IPs:** 136,348
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 22.57%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 220,451 | 218,516 | 76,571 | 12.68% | `aggregated-us-only.txt` |
| Canada | CA | 17,656 | 17,532 | 11,475 | 1.90% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 32,222 | 32,048 | 10,053 | 1.66% | `aggregated-gb-only.txt` |
| Australia | AU | 11,427 | 11,369 | 4,883 | 0.81% | `aggregated-au-only.txt` |
| Germany | DE | 27,379 | 27,270 | 19,719 | 3.26% | `aggregated-de-only.txt` |
| South Korea | KR | 3,959 | 3,946 | 13,647 | 2.26% | `aggregated-kr-only.txt` |

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

