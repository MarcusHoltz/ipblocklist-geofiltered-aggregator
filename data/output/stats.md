# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-07-27 06:03:56 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.7
"Germany" : 4.4
"United Kingdom" : 2.2
"Canada" : 2.1
"South Korea" : 1.4
"Australia" : 1.4
"Other/Unfiltered" : 70.8
```

## Overall Summary

- **Total Input IPs:** 448,159
- **Countries Processed:** 6
- **Combined Unique IPs:** 130,672
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 29.16%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 135,484 | 133,670 | 79,358 | 17.71% | `aggregated-us-only.txt` |
| Canada | CA | 16,948 | 16,824 | 9,342 | 2.08% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,497 | 35,342 | 9,897 | 2.21% | `aggregated-gb-only.txt` |
| Australia | AU | 12,139 | 12,065 | 6,132 | 1.37% | `aggregated-au-only.txt` |
| Germany | DE | 29,225 | 29,158 | 19,588 | 4.37% | `aggregated-de-only.txt` |
| South Korea | KR | 3,949 | 3,939 | 6,355 | 1.42% | `aggregated-kr-only.txt` |

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

