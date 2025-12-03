# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-12-03 03:36:17 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.9
"Germany" : 3.8
"South Korea" : 2.8
"United Kingdom" : 2.2
"Canada" : 2.1
"Australia" : 1.3
"Other/Unfiltered" : 69.9
```

## Overall Summary

- **Total Input IPs:** 396,299
- **Countries Processed:** 6
- **Combined Unique IPs:** 119,452
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 30.14%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 208,627 | 207,128 | 71,065 | 17.93% | `aggregated-us-only.txt` |
| Canada | CA | 17,397 | 17,271 | 8,339 | 2.10% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,084 | 32,951 | 8,727 | 2.20% | `aggregated-gb-only.txt` |
| Australia | AU | 11,257 | 11,196 | 5,315 | 1.34% | `aggregated-au-only.txt` |
| Germany | DE | 27,412 | 27,288 | 14,912 | 3.76% | `aggregated-de-only.txt` |
| South Korea | KR | 4,016 | 4,015 | 11,094 | 2.80% | `aggregated-kr-only.txt` |

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

