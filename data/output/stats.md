# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-02-01 04:39:03 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.0
"Germany" : 3.8
"United Kingdom" : 2.4
"Canada" : 2.4
"South Korea" : 1.9
"Australia" : 1.3
"Other/Unfiltered" : 70.1
```

## Overall Summary

- **Total Input IPs:** 438,653
- **Countries Processed:** 6
- **Combined Unique IPs:** 131,157
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 29.90%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 190,220 | 188,593 | 79,170 | 18.05% | `aggregated-us-only.txt` |
| Canada | CA | 17,173 | 17,044 | 10,602 | 2.42% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,684 | 33,533 | 10,673 | 2.43% | `aggregated-gb-only.txt` |
| Australia | AU | 11,494 | 11,428 | 5,754 | 1.31% | `aggregated-au-only.txt` |
| Germany | DE | 27,778 | 27,657 | 16,524 | 3.77% | `aggregated-de-only.txt` |
| South Korea | KR | 4,017 | 4,003 | 8,434 | 1.92% | `aggregated-kr-only.txt` |

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

