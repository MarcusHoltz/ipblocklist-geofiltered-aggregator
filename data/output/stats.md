# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-10-10 08:37:51 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 21.5
"Germany" : 3.1
"United Kingdom" : 2.0
"Canada" : 1.5
"South Korea" : 1.4
"Australia" : 0.7
"Other/Unfiltered" : 69.8
```

## Overall Summary

- **Total Input IPs:** 835,676
- **Countries Processed:** 6
- **Combined Unique IPs:** 252,641
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 30.23%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 128,144 | 126,297 | 179,484 | 21.48% | `aggregated-us-only.txt` |
| Canada | CA | 17,518 | 17,394 | 12,832 | 1.54% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 36,152 | 35,983 | 16,453 | 1.97% | `aggregated-gb-only.txt` |
| Australia | AU | 12,365 | 12,292 | 5,754 | 0.69% | `aggregated-au-only.txt` |
| Germany | DE | 29,924 | 29,821 | 26,288 | 3.15% | `aggregated-de-only.txt` |
| South Korea | KR | 4,004 | 3,970 | 11,830 | 1.42% | `aggregated-kr-only.txt` |

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

