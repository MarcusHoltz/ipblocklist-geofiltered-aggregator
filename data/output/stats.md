# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-04-27 05:35:26 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 16.9
"Germany" : 4.4
"United Kingdom" : 3.4
"Australia" : 2.3
"Canada" : 2.3
"South Korea" : 1.5
"Other/Unfiltered" : 69.3
```

## Overall Summary

- **Total Input IPs:** 455,318
- **Countries Processed:** 6
- **Combined Unique IPs:** 139,873
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 30.72%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 171,324 | 169,740 | 76,797 | 16.87% | `aggregated-us-only.txt` |
| Canada | CA | 17,021 | 16,892 | 10,264 | 2.25% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,972 | 33,814 | 15,324 | 3.37% | `aggregated-gb-only.txt` |
| Australia | AU | 11,465 | 11,383 | 10,698 | 2.35% | `aggregated-au-only.txt` |
| Germany | DE | 29,039 | 28,924 | 20,129 | 4.42% | `aggregated-de-only.txt` |
| South Korea | KR | 4,071 | 4,061 | 6,661 | 1.46% | `aggregated-kr-only.txt` |

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

