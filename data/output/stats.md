# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-06-21 16:14:04 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.2
"Germany" : 5.3
"United Kingdom" : 3.6
"Australia" : 2.5
"Canada" : 2.5
"South Korea" : 1.4
"Other/Unfiltered" : 65.4
```

## Overall Summary

- **Total Input IPs:** 434,393
- **Countries Processed:** 6
- **Combined Unique IPs:** 150,377
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 34.62%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 157,756 | 155,950 | 83,303 | 19.18% | `aggregated-us-only.txt` |
| Canada | CA | 17,019 | 16,891 | 11,019 | 2.54% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,639 | 35,460 | 15,855 | 3.65% | `aggregated-gb-only.txt` |
| Australia | AU | 12,040 | 11,957 | 11,049 | 2.54% | `aggregated-au-only.txt` |
| Germany | DE | 28,842 | 28,762 | 23,060 | 5.31% | `aggregated-de-only.txt` |
| South Korea | KR | 3,964 | 3,954 | 6,091 | 1.40% | `aggregated-kr-only.txt` |

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

