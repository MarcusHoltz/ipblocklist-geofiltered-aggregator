# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-11-10 10:00:28 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 23.3
"Germany" : 3.6
"United Kingdom" : 2.1
"Canada" : 1.6
"South Korea" : 1.3
"Australia" : 0.7
"Other/Unfiltered" : 67.4
```

## Overall Summary

- **Total Input IPs:** 905,480
- **Countries Processed:** 6
- **Combined Unique IPs:** 294,919
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 32.57%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 129,352 | 127,481 | 210,765 | 23.28% | `aggregated-us-only.txt` |
| Canada | CA | 17,672 | 17,547 | 14,819 | 1.64% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 36,757 | 36,605 | 19,411 | 2.14% | `aggregated-gb-only.txt` |
| Australia | AU | 11,939 | 11,864 | 6,197 | 0.68% | `aggregated-au-only.txt` |
| Germany | DE | 30,360 | 30,243 | 32,313 | 3.57% | `aggregated-de-only.txt` |
| South Korea | KR | 3,997 | 3,988 | 11,414 | 1.26% | `aggregated-kr-only.txt` |

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

