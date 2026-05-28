# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-05-28 17:46:46 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.4
"Germany" : 5.1
"United Kingdom" : 3.6
"Australia" : 2.4
"Canada" : 2.4
"South Korea" : 1.4
"Other/Unfiltered" : 66.6
```

## Overall Summary

- **Total Input IPs:** 460,020
- **Countries Processed:** 6
- **Combined Unique IPs:** 153,547
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 33.38%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 166,410 | 164,906 | 84,552 | 18.38% | `aggregated-us-only.txt` |
| Canada | CA | 17,069 | 16,942 | 11,084 | 2.41% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 34,140 | 33,965 | 16,615 | 3.61% | `aggregated-gb-only.txt` |
| Australia | AU | 12,081 | 12,011 | 11,101 | 2.41% | `aggregated-au-only.txt` |
| Germany | DE | 28,870 | 28,778 | 23,553 | 5.12% | `aggregated-de-only.txt` |
| South Korea | KR | 3,959 | 3,949 | 6,642 | 1.44% | `aggregated-kr-only.txt` |

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

