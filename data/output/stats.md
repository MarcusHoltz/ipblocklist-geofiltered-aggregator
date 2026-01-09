# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-01-09 14:45:10 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 21.0
"Germany" : 3.9
"South Korea" : 2.5
"United Kingdom" : 2.3
"Canada" : 2.1
"Australia" : 1.1
"Other/Unfiltered" : 67.1
```

## Overall Summary

- **Total Input IPs:** 564,631
- **Countries Processed:** 6
- **Combined Unique IPs:** 185,711
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 32.89%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 196,770 | 195,158 | 118,646 | 21.01% | `aggregated-us-only.txt` |
| Canada | CA | 17,228 | 17,102 | 11,915 | 2.11% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,886 | 33,721 | 13,002 | 2.30% | `aggregated-gb-only.txt` |
| Australia | AU | 11,593 | 11,526 | 5,932 | 1.05% | `aggregated-au-only.txt` |
| Germany | DE | 27,570 | 27,431 | 22,050 | 3.91% | `aggregated-de-only.txt` |
| South Korea | KR | 3,983 | 3,982 | 14,166 | 2.51% | `aggregated-kr-only.txt` |

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

