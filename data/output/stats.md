# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-02-08 14:49:52 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.0
"Germany" : 3.9
"United Kingdom" : 2.4
"Canada" : 2.3
"South Korea" : 2.0
"Australia" : 1.4
"Other/Unfiltered" : 69.0
```

## Overall Summary

- **Total Input IPs:** 381,232
- **Countries Processed:** 6
- **Combined Unique IPs:** 118,359
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 31.05%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 187,914 | 186,301 | 72,532 | 19.03% | `aggregated-us-only.txt` |
| Canada | CA | 16,725 | 16,598 | 8,603 | 2.26% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,454 | 33,292 | 9,233 | 2.42% | `aggregated-gb-only.txt` |
| Australia | AU | 11,406 | 11,340 | 5,392 | 1.41% | `aggregated-au-only.txt` |
| Germany | DE | 27,868 | 27,751 | 14,897 | 3.91% | `aggregated-de-only.txt` |
| South Korea | KR | 4,014 | 4,000 | 7,702 | 2.02% | `aggregated-kr-only.txt` |

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

