# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-12-16 14:46:18 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.0
"Germany" : 3.8
"South Korea" : 2.6
"United Kingdom" : 2.3
"Canada" : 2.1
"Australia" : 1.3
"Other/Unfiltered" : 69.9
```

## Overall Summary

- **Total Input IPs:** 416,160
- **Countries Processed:** 6
- **Combined Unique IPs:** 125,402
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 30.13%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 205,029 | 203,447 | 74,929 | 18.00% | `aggregated-us-only.txt` |
| Canada | CA | 17,534 | 17,408 | 8,547 | 2.05% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,613 | 33,458 | 9,633 | 2.31% | `aggregated-gb-only.txt` |
| Australia | AU | 11,630 | 11,560 | 5,589 | 1.34% | `aggregated-au-only.txt` |
| Germany | DE | 27,435 | 27,295 | 15,957 | 3.83% | `aggregated-de-only.txt` |
| South Korea | KR | 3,986 | 3,985 | 10,747 | 2.58% | `aggregated-kr-only.txt` |

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

