# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-03-29 04:47:01 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.4
"Germany" : 4.4
"United Kingdom" : 3.4
"Australia" : 2.4
"Canada" : 2.2
"South Korea" : 1.5
"Other/Unfiltered" : 68.6
```

## Overall Summary

- **Total Input IPs:** 432,104
- **Countries Processed:** 6
- **Combined Unique IPs:** 135,619
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 31.39%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 179,402 | 177,798 | 75,237 | 17.41% | `aggregated-us-only.txt` |
| Canada | CA | 16,891 | 16,768 | 9,429 | 2.18% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,784 | 33,604 | 14,756 | 3.41% | `aggregated-gb-only.txt` |
| Australia | AU | 11,432 | 11,349 | 10,560 | 2.44% | `aggregated-au-only.txt` |
| Germany | DE | 28,326 | 28,235 | 19,132 | 4.43% | `aggregated-de-only.txt` |
| South Korea | KR | 4,015 | 4,005 | 6,505 | 1.51% | `aggregated-kr-only.txt` |

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

