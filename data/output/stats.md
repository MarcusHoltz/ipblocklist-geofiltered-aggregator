# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-06-19 16:43:07 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.1
"Germany" : 5.4
"United Kingdom" : 3.7
"Canada" : 2.6
"Australia" : 2.5
"South Korea" : 1.4
"Other/Unfiltered" : 65.3
```

## Overall Summary

- **Total Input IPs:** 438,570
- **Countries Processed:** 6
- **Combined Unique IPs:** 152,077
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 34.68%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 162,102 | 160,287 | 83,784 | 19.10% | `aggregated-us-only.txt` |
| Canada | CA | 16,986 | 16,858 | 11,365 | 2.59% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,600 | 35,425 | 16,149 | 3.68% | `aggregated-gb-only.txt` |
| Australia | AU | 12,043 | 11,960 | 11,133 | 2.54% | `aggregated-au-only.txt` |
| Germany | DE | 28,808 | 28,728 | 23,522 | 5.36% | `aggregated-de-only.txt` |
| South Korea | KR | 3,954 | 3,944 | 6,124 | 1.40% | `aggregated-kr-only.txt` |

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

