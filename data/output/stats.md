# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-03-19 15:09:33 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.3
"Germany" : 4.5
"United Kingdom" : 3.4
"Australia" : 2.5
"Canada" : 2.3
"South Korea" : 1.5
"Other/Unfiltered" : 67.4
```

## Overall Summary

- **Total Input IPs:** 427,643
- **Countries Processed:** 6
- **Combined Unique IPs:** 139,286
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 32.57%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 182,037 | 180,421 | 78,245 | 18.30% | `aggregated-us-only.txt` |
| Canada | CA | 16,831 | 16,710 | 9,991 | 2.34% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,542 | 33,383 | 14,537 | 3.40% | `aggregated-gb-only.txt` |
| Australia | AU | 11,394 | 11,313 | 10,840 | 2.53% | `aggregated-au-only.txt` |
| Germany | DE | 28,759 | 28,678 | 19,110 | 4.47% | `aggregated-de-only.txt` |
| South Korea | KR | 4,059 | 4,048 | 6,563 | 1.53% | `aggregated-kr-only.txt` |

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

