# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-10-18 03:07:00 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 13.9
"Germany" : 3.3
"South Korea" : 2.4
"Canada" : 2.0
"United Kingdom" : 1.9
"Australia" : 0.8
"Other/Unfiltered" : 75.6
```

## Overall Summary

- **Total Input IPs:** 506,323
- **Countries Processed:** 6
- **Combined Unique IPs:** 123,317
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 24.36%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 227,690 | 225,148 | 70,147 | 13.85% | `aggregated-us-only.txt` |
| Canada | CA | 17,925 | 17,808 | 10,370 | 2.05% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,170 | 33,025 | 9,473 | 1.87% | `aggregated-gb-only.txt` |
| Australia | AU | 11,608 | 11,551 | 4,240 | 0.84% | `aggregated-au-only.txt` |
| Germany | DE | 27,833 | 27,710 | 16,737 | 3.31% | `aggregated-de-only.txt` |
| South Korea | KR | 4,022 | 4,021 | 12,350 | 2.44% | `aggregated-kr-only.txt` |

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

