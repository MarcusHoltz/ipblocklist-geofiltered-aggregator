# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-10-08 14:42:35 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 13.3
"Germany" : 3.2
"South Korea" : 2.4
"Canada" : 2.0
"United Kingdom" : 1.8
"Australia" : 0.8
"Other/Unfiltered" : 76.4
```

## Overall Summary

- **Total Input IPs:** 525,587
- **Countries Processed:** 6
- **Combined Unique IPs:** 123,908
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 23.58%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 226,331 | 223,775 | 69,821 | 13.28% | `aggregated-us-only.txt` |
| Canada | CA | 17,971 | 17,851 | 10,625 | 2.02% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,071 | 32,917 | 9,413 | 1.79% | `aggregated-gb-only.txt` |
| Australia | AU | 11,560 | 11,500 | 4,247 | 0.81% | `aggregated-au-only.txt` |
| Germany | DE | 27,643 | 27,520 | 17,042 | 3.24% | `aggregated-de-only.txt` |
| South Korea | KR | 4,001 | 4,000 | 12,760 | 2.43% | `aggregated-kr-only.txt` |

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

