# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-01-12 04:00:30 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 20.9
"Germany" : 3.9
"South Korea" : 2.5
"United Kingdom" : 2.3
"Canada" : 2.1
"Australia" : 1.0
"Other/Unfiltered" : 67.2
```

## Overall Summary

- **Total Input IPs:** 571,286
- **Countries Processed:** 6
- **Combined Unique IPs:** 187,448
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 32.81%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 194,691 | 193,051 | 119,675 | 20.95% | `aggregated-us-only.txt` |
| Canada | CA | 17,361 | 17,238 | 12,132 | 2.12% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,705 | 33,541 | 13,285 | 2.33% | `aggregated-gb-only.txt` |
| Australia | AU | 11,514 | 11,445 | 5,977 | 1.05% | `aggregated-au-only.txt` |
| Germany | DE | 27,639 | 27,491 | 22,292 | 3.90% | `aggregated-de-only.txt` |
| South Korea | KR | 3,991 | 3,977 | 14,087 | 2.47% | `aggregated-kr-only.txt` |

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

