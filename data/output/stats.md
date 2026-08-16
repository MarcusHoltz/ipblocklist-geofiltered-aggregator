# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-08-16 03:16:01 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.7
"Germany" : 3.5
"United Kingdom" : 1.9
"Canada" : 1.9
"South Korea" : 1.4
"Australia" : 0.9
"Other/Unfiltered" : 71.7
```

## Overall Summary

- **Total Input IPs:** 455,738
- **Countries Processed:** 6
- **Combined Unique IPs:** 129,047
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 28.32%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 131,721 | 129,853 | 85,189 | 18.69% | `aggregated-us-only.txt` |
| Canada | CA | 17,158 | 17,035 | 8,682 | 1.91% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,713 | 35,551 | 8,758 | 1.92% | `aggregated-gb-only.txt` |
| Australia | AU | 12,195 | 12,123 | 4,163 | 0.91% | `aggregated-au-only.txt` |
| Germany | DE | 29,761 | 29,693 | 15,963 | 3.50% | `aggregated-de-only.txt` |
| South Korea | KR | 3,928 | 3,918 | 6,292 | 1.38% | `aggregated-kr-only.txt` |

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

