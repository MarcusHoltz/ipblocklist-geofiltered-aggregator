# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-10-16 07:18:07 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 22.5
"Germany" : 4.1
"South Korea" : 2.7
"Canada" : 2.2
"United Kingdom" : 2.2
"Australia" : 0.8
"Other/Unfiltered" : 65.6
```

## Overall Summary

- **Total Input IPs:** 134,696
- **Countries Processed:** 6
- **Combined Unique IPs:** 46,283
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 34.36%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 128,424 | 126,547 | 30,291 | 22.49% | `aggregated-us-only.txt` |
| Canada | CA | 17,635 | 17,506 | 2,969 | 2.20% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 36,400 | 36,228 | 2,948 | 2.19% | `aggregated-gb-only.txt` |
| Australia | AU | 12,423 | 12,350 | 1,021 | 0.76% | `aggregated-au-only.txt` |
| Germany | DE | 30,289 | 30,183 | 5,465 | 4.06% | `aggregated-de-only.txt` |
| South Korea | KR | 3,991 | 3,968 | 3,589 | 2.66% | `aggregated-kr-only.txt` |

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

