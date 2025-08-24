# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-08-24 03:34:16 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 12.2
"Germany" : 3.2
"South Korea" : 2.2
"Canada" : 1.7
"United Kingdom" : 1.6
"Australia" : 0.7
"Other/Unfiltered" : 78.3
```

## Overall Summary

- **Total Input IPs:** 603,470
- **Countries Processed:** 6
- **Combined Unique IPs:** 130,943
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 21.70%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 218,244 | 216,816 | 73,765 | 12.22% | `aggregated-us-only.txt` |
| Canada | CA | 17,804 | 17,678 | 10,531 | 1.75% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 32,316 | 32,142 | 9,601 | 1.59% | `aggregated-gb-only.txt` |
| Australia | AU | 11,315 | 11,257 | 4,488 | 0.74% | `aggregated-au-only.txt` |
| Germany | DE | 27,285 | 27,176 | 19,307 | 3.20% | `aggregated-de-only.txt` |
| South Korea | KR | 3,946 | 3,933 | 13,251 | 2.20% | `aggregated-kr-only.txt` |

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

