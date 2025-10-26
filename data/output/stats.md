# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-10-26 03:19:12 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 14.5
"Germany" : 3.4
"South Korea" : 2.5
"Canada" : 2.1
"United Kingdom" : 1.9
"Australia" : 0.8
"Other/Unfiltered" : 74.7
```

## Overall Summary

- **Total Input IPs:** 482,005
- **Countries Processed:** 6
- **Combined Unique IPs:** 121,966
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 25.30%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 230,975 | 227,909 | 70,086 | 14.54% | `aggregated-us-only.txt` |
| Canada | CA | 18,037 | 17,920 | 10,117 | 2.10% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,449 | 33,304 | 9,206 | 1.91% | `aggregated-gb-only.txt` |
| Australia | AU | 11,593 | 11,524 | 4,043 | 0.84% | `aggregated-au-only.txt` |
| Germany | DE | 27,871 | 27,768 | 16,537 | 3.43% | `aggregated-de-only.txt` |
| South Korea | KR | 4,035 | 4,034 | 11,977 | 2.48% | `aggregated-kr-only.txt` |

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

