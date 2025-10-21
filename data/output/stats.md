# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-10-21 14:35:50 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 14.2
"Germany" : 3.4
"South Korea" : 2.5
"Canada" : 2.1
"United Kingdom" : 1.9
"Australia" : 0.8
"Other/Unfiltered" : 75.1
```

## Overall Summary

- **Total Input IPs:** 495,302
- **Countries Processed:** 6
- **Combined Unique IPs:** 123,169
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 24.87%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 230,148 | 227,488 | 70,174 | 14.17% | `aggregated-us-only.txt` |
| Canada | CA | 18,010 | 17,893 | 10,358 | 2.09% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,277 | 33,132 | 9,447 | 1.91% | `aggregated-gb-only.txt` |
| Australia | AU | 11,625 | 11,568 | 4,136 | 0.84% | `aggregated-au-only.txt` |
| Germany | DE | 27,789 | 27,673 | 16,832 | 3.40% | `aggregated-de-only.txt` |
| South Korea | KR | 4,036 | 4,035 | 12,222 | 2.47% | `aggregated-kr-only.txt` |

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

