# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-02-24 15:12:13 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.3
"Germany" : 4.2
"United Kingdom" : 2.5
"Canada" : 2.2
"South Korea" : 1.8
"Australia" : 1.8
"Other/Unfiltered" : 68.2
```

## Overall Summary

- **Total Input IPs:** 379,506
- **Countries Processed:** 6
- **Combined Unique IPs:** 120,777
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 31.82%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 187,140 | 185,523 | 73,432 | 19.35% | `aggregated-us-only.txt` |
| Canada | CA | 16,884 | 16,753 | 8,379 | 2.21% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,109 | 32,941 | 9,374 | 2.47% | `aggregated-gb-only.txt` |
| Australia | AU | 11,405 | 11,339 | 6,840 | 1.80% | `aggregated-au-only.txt` |
| Germany | DE | 28,130 | 28,030 | 15,908 | 4.19% | `aggregated-de-only.txt` |
| South Korea | KR | 4,020 | 4,019 | 6,844 | 1.80% | `aggregated-kr-only.txt` |

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

