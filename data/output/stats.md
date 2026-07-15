# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-07-15 15:55:12 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.7
"Germany" : 4.7
"United Kingdom" : 2.7
"Canada" : 2.1
"Australia" : 2.0
"South Korea" : 1.4
"Other/Unfiltered" : 69.4
```

## Overall Summary

- **Total Input IPs:** 442,775
- **Countries Processed:** 6
- **Combined Unique IPs:** 135,665
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 30.64%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 141,446 | 139,632 | 78,350 | 17.70% | `aggregated-us-only.txt` |
| Canada | CA | 16,872 | 16,752 | 9,259 | 2.09% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,500 | 35,331 | 12,004 | 2.71% | `aggregated-gb-only.txt` |
| Australia | AU | 12,038 | 11,968 | 8,814 | 1.99% | `aggregated-au-only.txt` |
| Germany | DE | 29,072 | 29,000 | 20,819 | 4.70% | `aggregated-de-only.txt` |
| South Korea | KR | 3,887 | 3,877 | 6,419 | 1.45% | `aggregated-kr-only.txt` |

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

