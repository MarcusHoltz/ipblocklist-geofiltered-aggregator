# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-07-28 16:17:36 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.7
"Germany" : 4.4
"United Kingdom" : 2.1
"Canada" : 1.8
"South Korea" : 1.4
"Australia" : 1.3
"Other/Unfiltered" : 71.3
```

## Overall Summary

- **Total Input IPs:** 449,587
- **Countries Processed:** 6
- **Combined Unique IPs:** 129,229
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 28.74%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 135,484 | 133,670 | 79,571 | 17.70% | `aggregated-us-only.txt` |
| Canada | CA | 16,948 | 16,824 | 8,164 | 1.82% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,497 | 35,342 | 9,636 | 2.14% | `aggregated-gb-only.txt` |
| Australia | AU | 12,139 | 12,065 | 5,942 | 1.32% | `aggregated-au-only.txt` |
| Germany | DE | 29,225 | 29,158 | 19,584 | 4.36% | `aggregated-de-only.txt` |
| South Korea | KR | 3,949 | 3,939 | 6,332 | 1.41% | `aggregated-kr-only.txt` |

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

