# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-01-18 14:36:52 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.7
"Germany" : 3.7
"United Kingdom" : 2.3
"Canada" : 2.1
"South Korea" : 1.9
"Australia" : 1.1
"Other/Unfiltered" : 71.1
```

## Overall Summary

- **Total Input IPs:** 538,822
- **Countries Processed:** 6
- **Combined Unique IPs:** 155,847
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 28.92%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 192,503 | 190,855 | 95,572 | 17.74% | `aggregated-us-only.txt` |
| Canada | CA | 17,317 | 17,192 | 11,516 | 2.14% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,656 | 33,494 | 12,474 | 2.32% | `aggregated-gb-only.txt` |
| Australia | AU | 11,536 | 11,469 | 6,073 | 1.13% | `aggregated-au-only.txt` |
| Germany | DE | 27,599 | 27,451 | 20,194 | 3.75% | `aggregated-de-only.txt` |
| South Korea | KR | 3,999 | 3,985 | 10,018 | 1.86% | `aggregated-kr-only.txt` |

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

