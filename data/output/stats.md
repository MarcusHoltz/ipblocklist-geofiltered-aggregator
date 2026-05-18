# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-05-18 17:13:46 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.2
"Germany" : 5.0
"United Kingdom" : 3.7
"Canada" : 2.5
"Australia" : 2.5
"South Korea" : 1.5
"Other/Unfiltered" : 66.7
```

## Overall Summary

- **Total Input IPs:** 453,349
- **Countries Processed:** 6
- **Combined Unique IPs:** 150,748
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 33.25%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 167,217 | 165,713 | 82,437 | 18.18% | `aggregated-us-only.txt` |
| Canada | CA | 17,079 | 16,951 | 11,252 | 2.48% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,930 | 33,764 | 16,747 | 3.69% | `aggregated-gb-only.txt` |
| Australia | AU | 12,099 | 12,029 | 11,119 | 2.45% | `aggregated-au-only.txt` |
| Germany | DE | 28,842 | 28,762 | 22,585 | 4.98% | `aggregated-de-only.txt` |
| South Korea | KR | 3,976 | 3,966 | 6,608 | 1.46% | `aggregated-kr-only.txt` |

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

