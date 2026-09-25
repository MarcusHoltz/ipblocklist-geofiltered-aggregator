# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-09-25 18:50:53 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 20.9
"Germany" : 3.1
"United Kingdom" : 1.9
"Canada" : 1.6
"South Korea" : 1.4
"Australia" : 0.7
"Other/Unfiltered" : 70.4
```

## Overall Summary

- **Total Input IPs:** 744,214
- **Countries Processed:** 6
- **Combined Unique IPs:** 220,042
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 29.57%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 128,919 | 127,081 | 155,173 | 20.85% | `aggregated-us-only.txt` |
| Canada | CA | 17,281 | 17,163 | 11,696 | 1.57% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 36,037 | 35,862 | 14,410 | 1.94% | `aggregated-gb-only.txt` |
| Australia | AU | 12,686 | 12,614 | 5,339 | 0.72% | `aggregated-au-only.txt` |
| Germany | DE | 29,692 | 29,583 | 22,705 | 3.05% | `aggregated-de-only.txt` |
| South Korea | KR | 3,953 | 3,919 | 10,719 | 1.44% | `aggregated-kr-only.txt` |

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

