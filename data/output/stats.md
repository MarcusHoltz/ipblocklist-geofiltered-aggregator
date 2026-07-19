# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-07-19 05:33:57 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.7
"Germany" : 4.6
"United Kingdom" : 2.6
"Canada" : 2.1
"Australia" : 1.8
"South Korea" : 1.5
"Other/Unfiltered" : 69.9
```

## Overall Summary

- **Total Input IPs:** 443,112
- **Countries Processed:** 6
- **Combined Unique IPs:** 133,543
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 30.14%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 137,787 | 135,973 | 78,383 | 17.69% | `aggregated-us-only.txt` |
| Canada | CA | 16,857 | 16,741 | 9,345 | 2.11% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,446 | 35,279 | 11,340 | 2.56% | `aggregated-gb-only.txt` |
| Australia | AU | 12,109 | 12,038 | 7,809 | 1.76% | `aggregated-au-only.txt` |
| Germany | DE | 29,153 | 29,083 | 20,235 | 4.57% | `aggregated-de-only.txt` |
| South Korea | KR | 3,909 | 3,899 | 6,431 | 1.45% | `aggregated-kr-only.txt` |

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

