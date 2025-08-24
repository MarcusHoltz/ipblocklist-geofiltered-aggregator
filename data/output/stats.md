# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-08-24 14:33:58 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 12.3
"Germany" : 3.2
"South Korea" : 2.2
"Canada" : 1.8
"United Kingdom" : 1.6
"Australia" : 0.7
"Other/Unfiltered" : 78.2
```

## Overall Summary

- **Total Input IPs:** 606,003
- **Countries Processed:** 6
- **Combined Unique IPs:** 131,864
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 21.76%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 218,244 | 216,816 | 74,340 | 12.27% | `aggregated-us-only.txt` |
| Canada | CA | 17,804 | 17,678 | 10,626 | 1.75% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 32,316 | 32,142 | 9,654 | 1.59% | `aggregated-gb-only.txt` |
| Australia | AU | 11,315 | 11,257 | 4,513 | 0.74% | `aggregated-au-only.txt` |
| Germany | DE | 27,285 | 27,176 | 19,457 | 3.21% | `aggregated-de-only.txt` |
| South Korea | KR | 3,946 | 3,933 | 13,274 | 2.19% | `aggregated-kr-only.txt` |

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

