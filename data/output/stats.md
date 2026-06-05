# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-06-05 16:44:27 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.4
"Germany" : 5.3
"United Kingdom" : 3.8
"Canada" : 2.6
"Australia" : 2.6
"South Korea" : 1.3
"Other/Unfiltered" : 65.0
```

## Overall Summary

- **Total Input IPs:** 423,524
- **Countries Processed:** 6
- **Combined Unique IPs:** 148,437
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 35.05%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 165,171 | 163,351 | 82,230 | 19.42% | `aggregated-us-only.txt` |
| Canada | CA | 17,038 | 16,909 | 10,970 | 2.59% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 34,022 | 33,847 | 16,106 | 3.80% | `aggregated-gb-only.txt` |
| Australia | AU | 12,034 | 11,967 | 10,842 | 2.56% | `aggregated-au-only.txt` |
| Germany | DE | 28,948 | 28,868 | 22,622 | 5.34% | `aggregated-de-only.txt` |
| South Korea | KR | 3,938 | 3,928 | 5,667 | 1.34% | `aggregated-kr-only.txt` |

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

