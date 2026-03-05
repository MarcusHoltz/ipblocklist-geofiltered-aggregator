# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-03-05 04:22:10 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.0
"Germany" : 4.5
"United Kingdom" : 3.0
"Canada" : 2.5
"Australia" : 2.2
"South Korea" : 1.7
"Other/Unfiltered" : 67.2
```

## Overall Summary

- **Total Input IPs:** 394,987
- **Countries Processed:** 6
- **Combined Unique IPs:** 129,685
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 32.83%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 184,107 | 182,462 | 74,923 | 18.97% | `aggregated-us-only.txt` |
| Canada | CA | 16,752 | 16,621 | 9,992 | 2.53% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,936 | 33,761 | 11,700 | 2.96% | `aggregated-gb-only.txt` |
| Australia | AU | 11,343 | 11,264 | 8,526 | 2.16% | `aggregated-au-only.txt` |
| Germany | DE | 28,037 | 27,936 | 17,914 | 4.54% | `aggregated-de-only.txt` |
| South Korea | KR | 4,019 | 4,018 | 6,630 | 1.68% | `aggregated-kr-only.txt` |

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

