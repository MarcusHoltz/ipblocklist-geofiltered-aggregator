# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-09-16 03:07:03 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 13.0
"Germany" : 3.4
"South Korea" : 2.3
"Canada" : 2.0
"United Kingdom" : 1.7
"Australia" : 0.8
"Other/Unfiltered" : 76.7
```

## Overall Summary

- **Total Input IPs:** 587,093
- **Countries Processed:** 6
- **Combined Unique IPs:** 136,544
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 23.26%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 223,146 | 220,769 | 76,211 | 12.98% | `aggregated-us-only.txt` |
| Canada | CA | 17,802 | 17,689 | 11,856 | 2.02% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 32,651 | 32,492 | 10,040 | 1.71% | `aggregated-gb-only.txt` |
| Australia | AU | 11,651 | 11,596 | 4,911 | 0.84% | `aggregated-au-only.txt` |
| Germany | DE | 27,507 | 27,398 | 20,059 | 3.42% | `aggregated-de-only.txt` |
| South Korea | KR | 3,948 | 3,947 | 13,467 | 2.29% | `aggregated-kr-only.txt` |

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

