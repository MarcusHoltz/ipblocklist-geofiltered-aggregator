# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-04-13 15:49:45 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.2
"Germany" : 4.5
"United Kingdom" : 3.4
"Australia" : 2.4
"Canada" : 2.2
"South Korea" : 1.4
"Other/Unfiltered" : 68.8
```

## Overall Summary

- **Total Input IPs:** 435,867
- **Countries Processed:** 6
- **Combined Unique IPs:** 135,949
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 31.19%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 174,297 | 172,744 | 75,031 | 17.21% | `aggregated-us-only.txt` |
| Canada | CA | 16,926 | 16,789 | 9,700 | 2.23% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,790 | 33,627 | 14,753 | 3.38% | `aggregated-gb-only.txt` |
| Australia | AU | 11,413 | 11,331 | 10,637 | 2.44% | `aggregated-au-only.txt` |
| Germany | DE | 28,732 | 28,618 | 19,629 | 4.50% | `aggregated-de-only.txt` |
| South Korea | KR | 4,047 | 4,037 | 6,199 | 1.42% | `aggregated-kr-only.txt` |

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

