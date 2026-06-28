# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-06-28 15:43:25 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.8
"Germany" : 5.2
"United Kingdom" : 3.5
"Australia" : 2.5
"Canada" : 2.5
"South Korea" : 1.4
"Other/Unfiltered" : 66.0
```

## Overall Summary

- **Total Input IPs:** 424,991
- **Countries Processed:** 6
- **Combined Unique IPs:** 144,443
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 33.99%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 149,937 | 148,118 | 79,782 | 18.77% | `aggregated-us-only.txt` |
| Canada | CA | 16,781 | 16,649 | 10,727 | 2.52% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,005 | 34,838 | 14,856 | 3.50% | `aggregated-gb-only.txt` |
| Australia | AU | 12,035 | 11,960 | 10,789 | 2.54% | `aggregated-au-only.txt` |
| Germany | DE | 28,921 | 28,848 | 22,186 | 5.22% | `aggregated-de-only.txt` |
| South Korea | KR | 3,914 | 3,904 | 6,103 | 1.44% | `aggregated-kr-only.txt` |

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

