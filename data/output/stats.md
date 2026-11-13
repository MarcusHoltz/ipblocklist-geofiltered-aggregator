# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-11-13 09:42:25 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 23.9
"Germany" : 3.6
"United Kingdom" : 2.1
"Canada" : 1.8
"South Korea" : 1.2
"Australia" : 0.7
"Other/Unfiltered" : 66.7
```

## Overall Summary

- **Total Input IPs:** 942,139
- **Countries Processed:** 6
- **Combined Unique IPs:** 314,155
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 33.34%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 129,352 | 127,481 | 225,035 | 23.89% | `aggregated-us-only.txt` |
| Canada | CA | 17,672 | 17,547 | 17,314 | 1.84% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 36,757 | 36,605 | 20,126 | 2.14% | `aggregated-gb-only.txt` |
| Australia | AU | 11,939 | 11,864 | 6,417 | 0.68% | `aggregated-au-only.txt` |
| Germany | DE | 30,360 | 30,243 | 34,034 | 3.61% | `aggregated-de-only.txt` |
| South Korea | KR | 3,997 | 3,988 | 11,229 | 1.19% | `aggregated-kr-only.txt` |

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

