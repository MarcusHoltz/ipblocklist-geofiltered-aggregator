# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-02-20 04:24:52 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.2
"Germany" : 4.0
"United Kingdom" : 2.3
"Canada" : 2.2
"South Korea" : 1.8
"Australia" : 1.5
"Other/Unfiltered" : 68.9
```

## Overall Summary

- **Total Input IPs:** 371,706
- **Countries Processed:** 6
- **Combined Unique IPs:** 115,472
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 31.07%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 187,917 | 186,299 | 71,483 | 19.23% | `aggregated-us-only.txt` |
| Canada | CA | 16,886 | 16,755 | 8,136 | 2.19% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 32,949 | 32,783 | 8,655 | 2.33% | `aggregated-gb-only.txt` |
| Australia | AU | 11,393 | 11,327 | 5,630 | 1.51% | `aggregated-au-only.txt` |
| Germany | DE | 27,984 | 27,893 | 14,780 | 3.98% | `aggregated-de-only.txt` |
| South Korea | KR | 4,032 | 4,031 | 6,788 | 1.83% | `aggregated-kr-only.txt` |

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

