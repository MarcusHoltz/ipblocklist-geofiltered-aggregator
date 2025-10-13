# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-10-13 14:38:49 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 13.4
"Germany" : 3.3
"South Korea" : 2.4
"Canada" : 2.0
"United Kingdom" : 1.8
"Australia" : 0.8
"Other/Unfiltered" : 76.2
```

## Overall Summary

- **Total Input IPs:** 522,533
- **Countries Processed:** 6
- **Combined Unique IPs:** 124,201
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 23.77%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 227,690 | 225,148 | 70,099 | 13.42% | `aggregated-us-only.txt` |
| Canada | CA | 17,925 | 17,808 | 10,564 | 2.02% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,170 | 33,025 | 9,514 | 1.82% | `aggregated-gb-only.txt` |
| Australia | AU | 11,608 | 11,551 | 4,343 | 0.83% | `aggregated-au-only.txt` |
| Germany | DE | 27,833 | 27,710 | 17,054 | 3.26% | `aggregated-de-only.txt` |
| South Korea | KR | 4,022 | 4,021 | 12,627 | 2.42% | `aggregated-kr-only.txt` |

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

