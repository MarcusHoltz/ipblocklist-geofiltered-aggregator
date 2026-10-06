# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-10-06 09:06:12 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 21.0
"Germany" : 3.1
"United Kingdom" : 1.8
"Canada" : 1.5
"South Korea" : 1.4
"Australia" : 0.7
"Other/Unfiltered" : 70.5
```

## Overall Summary

- **Total Input IPs:** 809,112
- **Countries Processed:** 6
- **Combined Unique IPs:** 238,946
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 29.53%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 128,144 | 126,297 | 169,949 | 21.00% | `aggregated-us-only.txt` |
| Canada | CA | 17,518 | 17,394 | 11,804 | 1.46% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 36,152 | 35,983 | 14,616 | 1.81% | `aggregated-gb-only.txt` |
| Australia | AU | 12,365 | 12,292 | 5,864 | 0.72% | `aggregated-au-only.txt` |
| Germany | DE | 29,924 | 29,821 | 25,060 | 3.10% | `aggregated-de-only.txt` |
| South Korea | KR | 4,004 | 3,970 | 11,653 | 1.44% | `aggregated-kr-only.txt` |

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

