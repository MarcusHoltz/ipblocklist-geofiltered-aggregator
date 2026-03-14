# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-03-14 04:21:09 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.7
"Germany" : 4.4
"United Kingdom" : 3.3
"Australia" : 2.4
"Canada" : 2.3
"South Korea" : 1.6
"Other/Unfiltered" : 67.3
```

## Overall Summary

- **Total Input IPs:** 413,819
- **Countries Processed:** 6
- **Combined Unique IPs:** 135,177
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 32.67%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 182,708 | 181,071 | 77,317 | 18.68% | `aggregated-us-only.txt` |
| Canada | CA | 16,787 | 16,659 | 9,473 | 2.29% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 34,352 | 34,165 | 13,679 | 3.31% | `aggregated-gb-only.txt` |
| Australia | AU | 11,350 | 11,275 | 10,096 | 2.44% | `aggregated-au-only.txt` |
| Germany | DE | 28,411 | 28,332 | 18,108 | 4.38% | `aggregated-de-only.txt` |
| South Korea | KR | 4,030 | 4,029 | 6,504 | 1.57% | `aggregated-kr-only.txt` |

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

