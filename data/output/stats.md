# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-06-13 15:53:05 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.1
"Germany" : 5.5
"United Kingdom" : 3.7
"Australia" : 2.5
"Canada" : 2.5
"South Korea" : 1.3
"Other/Unfiltered" : 65.3
```

## Overall Summary

- **Total Input IPs:** 430,456
- **Countries Processed:** 6
- **Combined Unique IPs:** 149,482
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 34.73%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 164,583 | 162,769 | 82,252 | 19.11% | `aggregated-us-only.txt` |
| Canada | CA | 17,078 | 16,950 | 10,844 | 2.52% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 34,200 | 34,027 | 16,025 | 3.72% | `aggregated-gb-only.txt` |
| Australia | AU | 11,518 | 11,439 | 10,913 | 2.54% | `aggregated-au-only.txt` |
| Germany | DE | 29,036 | 28,962 | 23,756 | 5.52% | `aggregated-de-only.txt` |
| South Korea | KR | 3,940 | 3,930 | 5,692 | 1.32% | `aggregated-kr-only.txt` |

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

