# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-01-17 03:41:05 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.8
"Germany" : 3.7
"United Kingdom" : 2.3
"Canada" : 2.3
"South Korea" : 1.9
"Australia" : 1.1
"Other/Unfiltered" : 70.9
```

## Overall Summary

- **Total Input IPs:** 535,422
- **Countries Processed:** 6
- **Combined Unique IPs:** 155,952
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 29.13%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 194,691 | 193,051 | 95,222 | 17.78% | `aggregated-us-only.txt` |
| Canada | CA | 17,361 | 17,238 | 12,189 | 2.28% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,705 | 33,541 | 12,381 | 2.31% | `aggregated-gb-only.txt` |
| Australia | AU | 11,514 | 11,445 | 6,034 | 1.13% | `aggregated-au-only.txt` |
| Germany | DE | 27,639 | 27,491 | 20,056 | 3.75% | `aggregated-de-only.txt` |
| South Korea | KR | 3,991 | 3,977 | 10,070 | 1.88% | `aggregated-kr-only.txt` |

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

