# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-03-11 15:09:14 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.9
"Germany" : 4.4
"United Kingdom" : 3.2
"Canada" : 2.5
"Australia" : 2.4
"South Korea" : 1.6
"Other/Unfiltered" : 67.0
```

## Overall Summary

- **Total Input IPs:** 408,274
- **Countries Processed:** 6
- **Combined Unique IPs:** 134,594
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 32.97%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 182,708 | 181,071 | 77,068 | 18.88% | `aggregated-us-only.txt` |
| Canada | CA | 16,787 | 16,659 | 10,171 | 2.49% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 34,352 | 34,165 | 12,931 | 3.17% | `aggregated-gb-only.txt` |
| Australia | AU | 11,350 | 11,275 | 9,821 | 2.41% | `aggregated-au-only.txt` |
| Germany | DE | 28,411 | 28,332 | 18,070 | 4.43% | `aggregated-de-only.txt` |
| South Korea | KR | 4,030 | 4,029 | 6,533 | 1.60% | `aggregated-kr-only.txt` |

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

