# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-11-12 21:31:41 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 23.7
"Germany" : 3.6
"United Kingdom" : 2.1
"Canada" : 1.8
"South Korea" : 1.2
"Australia" : 0.7
"Other/Unfiltered" : 66.8
```

## Overall Summary

- **Total Input IPs:** 943,182
- **Countries Processed:** 6
- **Combined Unique IPs:** 313,062
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 33.19%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 129,352 | 127,481 | 223,722 | 23.72% | `aggregated-us-only.txt` |
| Canada | CA | 17,672 | 17,547 | 17,246 | 1.83% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 36,757 | 36,605 | 20,155 | 2.14% | `aggregated-gb-only.txt` |
| Australia | AU | 11,939 | 11,864 | 6,454 | 0.68% | `aggregated-au-only.txt` |
| Germany | DE | 30,360 | 30,243 | 34,105 | 3.62% | `aggregated-de-only.txt` |
| South Korea | KR | 3,997 | 3,988 | 11,380 | 1.21% | `aggregated-kr-only.txt` |

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

