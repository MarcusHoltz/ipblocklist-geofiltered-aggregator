# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-12-25 14:39:23 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.5
"Germany" : 4.1
"South Korea" : 2.5
"United Kingdom" : 2.2
"Canada" : 2.0
"Australia" : 1.4
"Other/Unfiltered" : 70.4
```

## Overall Summary

- **Total Input IPs:** 425,781
- **Countries Processed:** 6
- **Combined Unique IPs:** 125,853
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 29.56%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 201,619 | 200,020 | 74,333 | 17.46% | `aggregated-us-only.txt` |
| Canada | CA | 17,339 | 17,213 | 8,534 | 2.00% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,812 | 33,657 | 9,235 | 2.17% | `aggregated-gb-only.txt` |
| Australia | AU | 11,538 | 11,468 | 5,753 | 1.35% | `aggregated-au-only.txt` |
| Germany | DE | 27,526 | 27,387 | 17,411 | 4.09% | `aggregated-de-only.txt` |
| South Korea | KR | 4,005 | 4,004 | 10,587 | 2.49% | `aggregated-kr-only.txt` |

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

