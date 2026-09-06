# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-09-06 17:08:42 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 21.3
"Germany" : 3.0
"United Kingdom" : 1.8
"Canada" : 1.7
"South Korea" : 1.3
"Australia" : 0.8
"Other/Unfiltered" : 70.1
```

## Overall Summary

- **Total Input IPs:** 505,537
- **Countries Processed:** 6
- **Combined Unique IPs:** 151,259
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 29.92%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 130,282 | 128,440 | 107,591 | 21.28% | `aggregated-us-only.txt` |
| Canada | CA | 17,185 | 17,069 | 8,552 | 1.69% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,923 | 35,760 | 9,304 | 1.84% | `aggregated-gb-only.txt` |
| Australia | AU | 12,309 | 12,242 | 3,863 | 0.76% | `aggregated-au-only.txt` |
| Germany | DE | 29,980 | 29,865 | 15,389 | 3.04% | `aggregated-de-only.txt` |
| South Korea | KR | 3,943 | 3,932 | 6,560 | 1.30% | `aggregated-kr-only.txt` |

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

