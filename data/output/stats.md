# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-08-03 05:55:06 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.9
"Germany" : 4.0
"United Kingdom" : 2.0
"Canada" : 1.8
"South Korea" : 1.4
"Australia" : 1.3
"Other/Unfiltered" : 71.7
```

## Overall Summary

- **Total Input IPs:** 448,491
- **Countries Processed:** 6
- **Combined Unique IPs:** 127,079
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 28.33%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 134,012 | 132,160 | 80,074 | 17.85% | `aggregated-us-only.txt` |
| Canada | CA | 17,066 | 16,942 | 8,068 | 1.80% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,276 | 35,129 | 9,010 | 2.01% | `aggregated-gb-only.txt` |
| Australia | AU | 12,122 | 12,050 | 5,653 | 1.26% | `aggregated-au-only.txt` |
| Germany | DE | 29,310 | 29,243 | 17,950 | 4.00% | `aggregated-de-only.txt` |
| South Korea | KR | 3,919 | 3,909 | 6,324 | 1.41% | `aggregated-kr-only.txt` |

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

