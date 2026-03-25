# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-03-25 15:39:00 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.1
"Germany" : 4.4
"United Kingdom" : 3.4
"Australia" : 2.5
"Canada" : 2.3
"South Korea" : 1.5
"Other/Unfiltered" : 67.7
```

## Overall Summary

- **Total Input IPs:** 423,327
- **Countries Processed:** 6
- **Combined Unique IPs:** 136,815
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 32.32%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 181,809 | 180,208 | 76,518 | 18.08% | `aggregated-us-only.txt` |
| Canada | CA | 16,866 | 16,741 | 9,940 | 2.35% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,693 | 33,508 | 14,507 | 3.43% | `aggregated-gb-only.txt` |
| Australia | AU | 11,441 | 11,360 | 10,612 | 2.51% | `aggregated-au-only.txt` |
| Germany | DE | 28,381 | 28,291 | 18,684 | 4.41% | `aggregated-de-only.txt` |
| South Korea | KR | 4,031 | 4,020 | 6,554 | 1.55% | `aggregated-kr-only.txt` |

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

