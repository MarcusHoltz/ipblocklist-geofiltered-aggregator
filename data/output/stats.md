# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-08-10 04:10:08 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.3
"Germany" : 3.8
"United Kingdom" : 1.9
"Canada" : 1.7
"South Korea" : 1.4
"Australia" : 1.1
"Other/Unfiltered" : 71.8
```

## Overall Summary

- **Total Input IPs:** 447,286
- **Countries Processed:** 6
- **Combined Unique IPs:** 126,059
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 28.18%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 133,752 | 131,895 | 82,010 | 18.34% | `aggregated-us-only.txt` |
| Canada | CA | 17,090 | 16,967 | 7,551 | 1.69% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,611 | 35,465 | 8,341 | 1.86% | `aggregated-gb-only.txt` |
| Australia | AU | 12,166 | 12,097 | 5,002 | 1.12% | `aggregated-au-only.txt` |
| Germany | DE | 29,554 | 29,487 | 16,917 | 3.78% | `aggregated-de-only.txt` |
| South Korea | KR | 3,940 | 3,930 | 6,238 | 1.39% | `aggregated-kr-only.txt` |

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

