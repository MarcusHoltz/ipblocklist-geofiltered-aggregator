# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-04-17 05:13:14 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.3
"Germany" : 4.5
"United Kingdom" : 3.4
"Australia" : 2.5
"Canada" : 2.3
"South Korea" : 1.4
"Other/Unfiltered" : 68.6
```

## Overall Summary

- **Total Input IPs:** 431,245
- **Countries Processed:** 6
- **Combined Unique IPs:** 135,265
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 31.37%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 174,297 | 172,744 | 74,617 | 17.30% | `aggregated-us-only.txt` |
| Canada | CA | 16,926 | 16,789 | 9,885 | 2.29% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,790 | 33,627 | 14,581 | 3.38% | `aggregated-gb-only.txt` |
| Australia | AU | 11,413 | 11,331 | 10,584 | 2.45% | `aggregated-au-only.txt` |
| Germany | DE | 28,732 | 28,618 | 19,565 | 4.54% | `aggregated-de-only.txt` |
| South Korea | KR | 4,047 | 4,037 | 6,033 | 1.40% | `aggregated-kr-only.txt` |

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

