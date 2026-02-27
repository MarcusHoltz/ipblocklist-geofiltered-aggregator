# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-02-27 15:01:22 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.4
"Germany" : 4.3
"United Kingdom" : 2.7
"Canada" : 2.3
"Australia" : 1.9
"South Korea" : 1.8
"Other/Unfiltered" : 67.6
```

## Overall Summary

- **Total Input IPs:** 380,554
- **Countries Processed:** 6
- **Combined Unique IPs:** 123,258
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 32.39%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 187,140 | 185,523 | 73,968 | 19.44% | `aggregated-us-only.txt` |
| Canada | CA | 16,884 | 16,753 | 8,662 | 2.28% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,109 | 32,941 | 10,100 | 2.65% | `aggregated-gb-only.txt` |
| Australia | AU | 11,405 | 11,339 | 7,351 | 1.93% | `aggregated-au-only.txt` |
| Germany | DE | 28,130 | 28,030 | 16,414 | 4.31% | `aggregated-de-only.txt` |
| South Korea | KR | 4,020 | 4,019 | 6,763 | 1.78% | `aggregated-kr-only.txt` |

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

