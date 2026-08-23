# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-08-23 14:44:38 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.1
"Germany" : 3.2
"Canada" : 2.1
"United Kingdom" : 2.0
"South Korea" : 1.3
"Australia" : 0.8
"Other/Unfiltered" : 71.5
```

## Overall Summary

- **Total Input IPs:** 459,264
- **Countries Processed:** 6
- **Combined Unique IPs:** 130,882
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 28.50%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 131,379 | 129,526 | 87,753 | 19.11% | `aggregated-us-only.txt` |
| Canada | CA | 17,186 | 17,068 | 9,434 | 2.05% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,817 | 35,660 | 9,292 | 2.02% | `aggregated-gb-only.txt` |
| Australia | AU | 12,214 | 12,142 | 3,562 | 0.78% | `aggregated-au-only.txt` |
| Germany | DE | 29,887 | 29,783 | 14,649 | 3.19% | `aggregated-de-only.txt` |
| South Korea | KR | 3,914 | 3,903 | 6,192 | 1.35% | `aggregated-kr-only.txt` |

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

