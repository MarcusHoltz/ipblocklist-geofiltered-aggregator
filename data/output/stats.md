# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-03-08 04:22:12 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.8
"Germany" : 4.5
"United Kingdom" : 3.0
"Canada" : 2.2
"Australia" : 2.2
"South Korea" : 1.7
"Other/Unfiltered" : 67.6
```

## Overall Summary

- **Total Input IPs:** 398,400
- **Countries Processed:** 6
- **Combined Unique IPs:** 129,137
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 32.41%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 182,708 | 181,071 | 74,981 | 18.82% | `aggregated-us-only.txt` |
| Canada | CA | 16,787 | 16,659 | 8,927 | 2.24% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 34,352 | 34,165 | 11,953 | 3.00% | `aggregated-gb-only.txt` |
| Australia | AU | 11,350 | 11,275 | 8,839 | 2.22% | `aggregated-au-only.txt` |
| Germany | DE | 28,411 | 28,332 | 17,862 | 4.48% | `aggregated-de-only.txt` |
| South Korea | KR | 4,030 | 4,029 | 6,575 | 1.65% | `aggregated-kr-only.txt` |

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

