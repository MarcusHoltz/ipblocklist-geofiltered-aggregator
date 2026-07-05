# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-07-05 15:40:58 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.3
"Germany" : 4.8
"United Kingdom" : 3.2
"Canada" : 2.4
"Australia" : 2.3
"South Korea" : 1.5
"Other/Unfiltered" : 67.5
```

## Overall Summary

- **Total Input IPs:** 433,195
- **Countries Processed:** 6
- **Combined Unique IPs:** 141,001
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 32.55%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 146,470 | 144,657 | 79,467 | 18.34% | `aggregated-us-only.txt` |
| Canada | CA | 16,851 | 16,729 | 10,295 | 2.38% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,133 | 34,962 | 13,941 | 3.22% | `aggregated-gb-only.txt` |
| Australia | AU | 12,084 | 12,012 | 10,171 | 2.35% | `aggregated-au-only.txt` |
| Germany | DE | 29,016 | 28,930 | 20,840 | 4.81% | `aggregated-de-only.txt` |
| South Korea | KR | 3,913 | 3,903 | 6,287 | 1.45% | `aggregated-kr-only.txt` |

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

