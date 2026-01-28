# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-01-28 03:55:06 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.8
"Germany" : 3.9
"Canada" : 2.5
"United Kingdom" : 2.5
"South Korea" : 1.9
"Australia" : 1.3
"Other/Unfiltered" : 70.2
```

## Overall Summary

- **Total Input IPs:** 463,174
- **Countries Processed:** 6
- **Combined Unique IPs:** 138,243
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 29.85%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 191,318 | 189,710 | 82,283 | 17.77% | `aggregated-us-only.txt` |
| Canada | CA | 17,196 | 17,071 | 11,705 | 2.53% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,750 | 33,592 | 11,560 | 2.50% | `aggregated-gb-only.txt` |
| Australia | AU | 11,508 | 11,442 | 5,822 | 1.26% | `aggregated-au-only.txt` |
| Germany | DE | 27,570 | 27,449 | 18,286 | 3.95% | `aggregated-de-only.txt` |
| South Korea | KR | 3,997 | 3,983 | 8,587 | 1.85% | `aggregated-kr-only.txt` |

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

