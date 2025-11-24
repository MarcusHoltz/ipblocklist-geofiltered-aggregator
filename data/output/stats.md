# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-11-24 14:41:47 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 16.9
"Germany" : 3.7
"South Korea" : 2.7
"Canada" : 2.2
"United Kingdom" : 2.1
"Australia" : 1.3
"Other/Unfiltered" : 71.2
```

## Overall Summary

- **Total Input IPs:** 407,962
- **Countries Processed:** 6
- **Combined Unique IPs:** 117,417
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 28.78%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 209,952 | 208,501 | 68,861 | 16.88% | `aggregated-us-only.txt` |
| Canada | CA | 17,580 | 17,458 | 8,837 | 2.17% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,180 | 33,043 | 8,599 | 2.11% | `aggregated-gb-only.txt` |
| Australia | AU | 11,254 | 11,184 | 5,139 | 1.26% | `aggregated-au-only.txt` |
| Germany | DE | 27,344 | 27,217 | 15,096 | 3.70% | `aggregated-de-only.txt` |
| South Korea | KR | 4,023 | 4,022 | 10,885 | 2.67% | `aggregated-kr-only.txt` |

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

