# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-11-27 14:40:25 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.1
"Germany" : 3.7
"South Korea" : 2.7
"Canada" : 2.1
"United Kingdom" : 2.1
"Australia" : 1.3
"Other/Unfiltered" : 71.0
```

## Overall Summary

- **Total Input IPs:** 414,613
- **Countries Processed:** 6
- **Combined Unique IPs:** 120,335
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 29.02%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 209,952 | 208,501 | 70,881 | 17.10% | `aggregated-us-only.txt` |
| Canada | CA | 17,580 | 17,458 | 8,913 | 2.15% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,180 | 33,043 | 8,797 | 2.12% | `aggregated-gb-only.txt` |
| Australia | AU | 11,254 | 11,184 | 5,252 | 1.27% | `aggregated-au-only.txt` |
| Germany | DE | 27,344 | 27,217 | 15,378 | 3.71% | `aggregated-de-only.txt` |
| South Korea | KR | 4,023 | 4,022 | 11,114 | 2.68% | `aggregated-kr-only.txt` |

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

