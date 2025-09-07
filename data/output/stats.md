# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-09-07 14:35:58 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 12.7
"Germany" : 3.3
"South Korea" : 2.3
"Canada" : 1.9
"United Kingdom" : 1.7
"Australia" : 0.8
"Other/Unfiltered" : 77.4
```

## Overall Summary

- **Total Input IPs:** 599,742
- **Countries Processed:** 6
- **Combined Unique IPs:** 135,749
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 22.63%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 221,782 | 219,407 | 75,959 | 12.67% | `aggregated-us-only.txt` |
| Canada | CA | 17,528 | 17,415 | 11,596 | 1.93% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 32,235 | 32,074 | 10,012 | 1.67% | `aggregated-gb-only.txt` |
| Australia | AU | 11,462 | 11,404 | 4,870 | 0.81% | `aggregated-au-only.txt` |
| Germany | DE | 27,414 | 27,292 | 19,724 | 3.29% | `aggregated-de-only.txt` |
| South Korea | KR | 3,962 | 3,949 | 13,588 | 2.27% | `aggregated-kr-only.txt` |

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

