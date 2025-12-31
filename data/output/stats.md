# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-12-31 03:46:44 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.8
"Germany" : 4.3
"South Korea" : 2.4
"United Kingdom" : 2.2
"Canada" : 2.1
"Australia" : 1.3
"Other/Unfiltered" : 69.8
```

## Overall Summary

- **Total Input IPs:** 430,657
- **Countries Processed:** 6
- **Combined Unique IPs:** 130,017
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 30.19%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 199,419 | 197,811 | 76,869 | 17.85% | `aggregated-us-only.txt` |
| Canada | CA | 17,248 | 17,118 | 8,953 | 2.08% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,774 | 33,608 | 9,645 | 2.24% | `aggregated-gb-only.txt` |
| Australia | AU | 11,596 | 11,526 | 5,719 | 1.33% | `aggregated-au-only.txt` |
| Germany | DE | 27,528 | 27,389 | 18,396 | 4.27% | `aggregated-de-only.txt` |
| South Korea | KR | 3,990 | 3,989 | 10,435 | 2.42% | `aggregated-kr-only.txt` |

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

