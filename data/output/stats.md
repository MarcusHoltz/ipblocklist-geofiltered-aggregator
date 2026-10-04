# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-10-04 08:32:34 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 20.5
"Germany" : 3.0
"United Kingdom" : 1.8
"Canada" : 1.4
"South Korea" : 1.4
"Australia" : 0.7
"Other/Unfiltered" : 71.0
```

## Overall Summary

- **Total Input IPs:** 805,251
- **Countries Processed:** 6
- **Combined Unique IPs:** 233,126
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 28.95%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 128,144 | 126,297 | 165,469 | 20.55% | `aggregated-us-only.txt` |
| Canada | CA | 17,518 | 17,394 | 11,644 | 1.45% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 36,152 | 35,983 | 14,465 | 1.80% | `aggregated-gb-only.txt` |
| Australia | AU | 12,365 | 12,292 | 5,636 | 0.70% | `aggregated-au-only.txt` |
| Germany | DE | 29,924 | 29,821 | 24,431 | 3.03% | `aggregated-de-only.txt` |
| South Korea | KR | 4,004 | 3,970 | 11,481 | 1.43% | `aggregated-kr-only.txt` |

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

