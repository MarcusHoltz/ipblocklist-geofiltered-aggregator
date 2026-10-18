# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-10-18 17:26:55 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 21.3
"Germany" : 3.4
"United Kingdom" : 2.1
"Canada" : 1.6
"South Korea" : 1.4
"Australia" : 0.7
"Other/Unfiltered" : 69.5
```

## Overall Summary

- **Total Input IPs:** 885,843
- **Countries Processed:** 6
- **Combined Unique IPs:** 269,801
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 30.46%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 128,606 | 126,734 | 189,046 | 21.34% | `aggregated-us-only.txt` |
| Canada | CA | 17,658 | 17,529 | 14,255 | 1.61% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 36,427 | 36,255 | 18,556 | 2.09% | `aggregated-gb-only.txt` |
| Australia | AU | 12,448 | 12,375 | 6,058 | 0.68% | `aggregated-au-only.txt` |
| Germany | DE | 30,436 | 30,330 | 29,873 | 3.37% | `aggregated-de-only.txt` |
| South Korea | KR | 3,994 | 3,971 | 12,013 | 1.36% | `aggregated-kr-only.txt` |

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

