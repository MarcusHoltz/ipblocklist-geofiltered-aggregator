# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-09-09 17:53:07 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 20.7
"Germany" : 2.8
"United Kingdom" : 1.9
"Canada" : 1.6
"South Korea" : 1.2
"Australia" : 0.7
"Other/Unfiltered" : 71.1
```

## Overall Summary

- **Total Input IPs:** 644,424
- **Countries Processed:** 6
- **Combined Unique IPs:** 186,289
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 28.91%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 130,282 | 128,440 | 133,191 | 20.67% | `aggregated-us-only.txt` |
| Canada | CA | 17,185 | 17,069 | 10,451 | 1.62% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,923 | 35,760 | 12,206 | 1.89% | `aggregated-gb-only.txt` |
| Australia | AU | 12,309 | 12,242 | 4,574 | 0.71% | `aggregated-au-only.txt` |
| Germany | DE | 29,980 | 29,865 | 18,270 | 2.84% | `aggregated-de-only.txt` |
| South Korea | KR | 3,943 | 3,932 | 7,597 | 1.18% | `aggregated-kr-only.txt` |

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

