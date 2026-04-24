# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-04-24 15:40:49 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.1
"Germany" : 4.5
"United Kingdom" : 3.3
"Australia" : 2.4
"Canada" : 2.3
"South Korea" : 1.5
"Other/Unfiltered" : 69.0
```

## Overall Summary

- **Total Input IPs:** 452,145
- **Countries Processed:** 6
- **Combined Unique IPs:** 140,199
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 31.01%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 172,991 | 171,454 | 77,207 | 17.08% | `aggregated-us-only.txt` |
| Canada | CA | 17,012 | 16,879 | 10,240 | 2.26% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,890 | 33,724 | 15,059 | 3.33% | `aggregated-gb-only.txt` |
| Australia | AU | 11,491 | 11,409 | 10,681 | 2.36% | `aggregated-au-only.txt` |
| Germany | DE | 28,793 | 28,678 | 20,270 | 4.48% | `aggregated-de-only.txt` |
| South Korea | KR | 4,064 | 4,054 | 6,742 | 1.49% | `aggregated-kr-only.txt` |

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

