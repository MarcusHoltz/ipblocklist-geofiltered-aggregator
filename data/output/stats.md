# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-09-25 03:12:10 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 13.1
"Germany" : 3.4
"South Korea" : 2.4
"Canada" : 2.0
"United Kingdom" : 1.7
"Australia" : 0.8
"Other/Unfiltered" : 76.7
```

## Overall Summary

- **Total Input IPs:** 568,077
- **Countries Processed:** 6
- **Combined Unique IPs:** 132,609
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 23.34%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 224,791 | 222,401 | 74,161 | 13.05% | `aggregated-us-only.txt` |
| Canada | CA | 17,886 | 17,771 | 11,352 | 2.00% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 32,808 | 32,653 | 9,534 | 1.68% | `aggregated-gb-only.txt` |
| Australia | AU | 11,669 | 11,610 | 4,789 | 0.84% | `aggregated-au-only.txt` |
| Germany | DE | 27,582 | 27,471 | 19,390 | 3.41% | `aggregated-de-only.txt` |
| South Korea | KR | 4,009 | 4,008 | 13,383 | 2.36% | `aggregated-kr-only.txt` |

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

