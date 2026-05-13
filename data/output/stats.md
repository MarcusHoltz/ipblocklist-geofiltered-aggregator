# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-05-13 16:36:03 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.0
"Germany" : 4.9
"United Kingdom" : 3.7
"Canada" : 2.4
"Australia" : 2.4
"South Korea" : 1.5
"Other/Unfiltered" : 67.1
```

## Overall Summary

- **Total Input IPs:** 445,916
- **Countries Processed:** 6
- **Combined Unique IPs:** 146,664
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 32.89%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 167,975 | 166,467 | 80,289 | 18.01% | `aggregated-us-only.txt` |
| Canada | CA | 17,039 | 16,905 | 10,923 | 2.45% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 34,028 | 33,858 | 16,281 | 3.65% | `aggregated-gb-only.txt` |
| Australia | AU | 12,110 | 12,041 | 10,912 | 2.45% | `aggregated-au-only.txt` |
| Germany | DE | 28,807 | 28,725 | 21,737 | 4.87% | `aggregated-de-only.txt` |
| South Korea | KR | 3,984 | 3,974 | 6,522 | 1.46% | `aggregated-kr-only.txt` |

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

