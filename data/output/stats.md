# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-11-03 03:35:50 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 15.1
"Germany" : 3.5
"South Korea" : 2.6
"Canada" : 2.1
"United Kingdom" : 2.0
"Australia" : 0.9
"Other/Unfiltered" : 73.8
```

## Overall Summary

- **Total Input IPs:** 463,609
- **Countries Processed:** 6
- **Combined Unique IPs:** 121,236
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 26.15%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 231,913 | 228,631 | 69,908 | 15.08% | `aggregated-us-only.txt` |
| Canada | CA | 18,016 | 17,895 | 9,945 | 2.15% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,513 | 33,361 | 9,231 | 1.99% | `aggregated-gb-only.txt` |
| Australia | AU | 11,668 | 11,599 | 3,991 | 0.86% | `aggregated-au-only.txt` |
| Germany | DE | 28,153 | 28,044 | 16,155 | 3.48% | `aggregated-de-only.txt` |
| South Korea | KR | 4,075 | 4,074 | 12,006 | 2.59% | `aggregated-kr-only.txt` |

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

