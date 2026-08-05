# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-08-05 05:27:30 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.9
"Germany" : 3.9
"United Kingdom" : 1.9
"Canada" : 1.8
"South Korea" : 1.4
"Australia" : 1.2
"Other/Unfiltered" : 71.9
```

## Overall Summary

- **Total Input IPs:** 451,073
- **Countries Processed:** 6
- **Combined Unique IPs:** 126,614
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 28.07%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 134,012 | 132,160 | 80,648 | 17.88% | `aggregated-us-only.txt` |
| Canada | CA | 17,066 | 16,942 | 7,996 | 1.77% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,276 | 35,129 | 8,648 | 1.92% | `aggregated-gb-only.txt` |
| Australia | AU | 12,122 | 12,050 | 5,344 | 1.18% | `aggregated-au-only.txt` |
| Germany | DE | 29,310 | 29,243 | 17,673 | 3.92% | `aggregated-de-only.txt` |
| South Korea | KR | 3,919 | 3,909 | 6,305 | 1.40% | `aggregated-kr-only.txt` |

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

