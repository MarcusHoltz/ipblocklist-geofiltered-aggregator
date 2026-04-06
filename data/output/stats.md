# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-04-06 15:08:57 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.3
"Germany" : 4.5
"United Kingdom" : 3.3
"Australia" : 2.4
"Canada" : 2.2
"South Korea" : 1.5
"Other/Unfiltered" : 68.8
```

## Overall Summary

- **Total Input IPs:** 436,051
- **Countries Processed:** 6
- **Combined Unique IPs:** 136,117
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 31.22%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 178,007 | 176,418 | 75,596 | 17.34% | `aggregated-us-only.txt` |
| Canada | CA | 17,099 | 16,965 | 9,466 | 2.17% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 34,704 | 34,521 | 14,557 | 3.34% | `aggregated-gb-only.txt` |
| Australia | AU | 11,516 | 11,432 | 10,547 | 2.42% | `aggregated-au-only.txt` |
| Germany | DE | 29,921 | 29,834 | 19,608 | 4.50% | `aggregated-de-only.txt` |
| South Korea | KR | 4,103 | 4,093 | 6,343 | 1.45% | `aggregated-kr-only.txt` |

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

