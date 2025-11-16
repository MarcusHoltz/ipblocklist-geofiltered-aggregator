# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-11-16 14:33:18 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 16.4
"Germany" : 3.6
"South Korea" : 2.7
"Canada" : 2.2
"United Kingdom" : 2.1
"Australia" : 1.1
"Other/Unfiltered" : 71.9
```

## Overall Summary

- **Total Input IPs:** 416,668
- **Countries Processed:** 6
- **Combined Unique IPs:** 117,078
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 28.10%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 213,082 | 211,660 | 68,537 | 16.45% | `aggregated-us-only.txt` |
| Canada | CA | 17,510 | 17,389 | 9,100 | 2.18% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,226 | 33,096 | 8,543 | 2.05% | `aggregated-gb-only.txt` |
| Australia | AU | 11,247 | 11,177 | 4,579 | 1.10% | `aggregated-au-only.txt` |
| Germany | DE | 27,310 | 27,183 | 15,178 | 3.64% | `aggregated-de-only.txt` |
| South Korea | KR | 4,040 | 4,039 | 11,141 | 2.67% | `aggregated-kr-only.txt` |

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

