# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-05-06 05:41:10 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.4
"Germany" : 4.5
"United Kingdom" : 3.5
"Australia" : 2.4
"Canada" : 2.3
"South Korea" : 1.4
"Other/Unfiltered" : 68.4
```

## Overall Summary

- **Total Input IPs:** 460,090
- **Countries Processed:** 6
- **Combined Unique IPs:** 145,345
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 31.59%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 169,198 | 167,680 | 80,151 | 17.42% | `aggregated-us-only.txt` |
| Canada | CA | 16,890 | 16,768 | 10,689 | 2.32% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,411 | 33,252 | 16,140 | 3.51% | `aggregated-gb-only.txt` |
| Australia | AU | 11,396 | 11,317 | 10,955 | 2.38% | `aggregated-au-only.txt` |
| Germany | DE | 28,972 | 28,867 | 20,879 | 4.54% | `aggregated-de-only.txt` |
| South Korea | KR | 4,006 | 3,996 | 6,531 | 1.42% | `aggregated-kr-only.txt` |

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

