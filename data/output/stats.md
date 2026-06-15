# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-06-15 07:42:27 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.1
"Germany" : 5.5
"United Kingdom" : 3.7
"Australia" : 2.6
"Canada" : 2.5
"South Korea" : 1.3
"Other/Unfiltered" : 65.3
```

## Overall Summary

- **Total Input IPs:** 431,367
- **Countries Processed:** 6
- **Combined Unique IPs:** 149,787
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 34.72%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 162,102 | 160,287 | 82,478 | 19.12% | `aggregated-us-only.txt` |
| Canada | CA | 16,986 | 16,858 | 10,779 | 2.50% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,600 | 35,425 | 15,911 | 3.69% | `aggregated-gb-only.txt` |
| Australia | AU | 12,043 | 11,960 | 11,054 | 2.56% | `aggregated-au-only.txt` |
| Germany | DE | 28,808 | 28,728 | 23,789 | 5.51% | `aggregated-de-only.txt` |
| South Korea | KR | 3,954 | 3,944 | 5,776 | 1.34% | `aggregated-kr-only.txt` |

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

