# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-09-13 07:32:22 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 21.4
"Germany" : 2.7
"United Kingdom" : 2.0
"Canada" : 1.6
"South Korea" : 1.1
"Australia" : 0.7
"Other/Unfiltered" : 70.5
```

## Overall Summary

- **Total Input IPs:** 755,268
- **Countries Processed:** 6
- **Combined Unique IPs:** 222,524
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 29.46%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 130,348 | 128,515 | 161,860 | 21.43% | `aggregated-us-only.txt` |
| Canada | CA | 17,287 | 17,169 | 11,799 | 1.56% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 36,372 | 36,194 | 15,135 | 2.00% | `aggregated-gb-only.txt` |
| Australia | AU | 12,330 | 12,258 | 5,197 | 0.69% | `aggregated-au-only.txt` |
| Germany | DE | 29,911 | 29,797 | 20,280 | 2.69% | `aggregated-de-only.txt` |
| South Korea | KR | 3,952 | 3,918 | 8,253 | 1.09% | `aggregated-kr-only.txt` |

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

