# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-11-14 03:31:33 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 16.2
"Germany" : 3.6
"South Korea" : 2.7
"Canada" : 2.2
"United Kingdom" : 2.1
"Australia" : 1.1
"Other/Unfiltered" : 72.1
```

## Overall Summary

- **Total Input IPs:** 421,919
- **Countries Processed:** 6
- **Combined Unique IPs:** 117,628
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 27.88%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 215,951 | 213,355 | 68,522 | 16.24% | `aggregated-us-only.txt` |
| Canada | CA | 17,382 | 17,256 | 9,199 | 2.18% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 32,943 | 32,796 | 8,866 | 2.10% | `aggregated-gb-only.txt` |
| Australia | AU | 11,295 | 11,226 | 4,431 | 1.05% | `aggregated-au-only.txt` |
| Germany | DE | 27,415 | 27,308 | 15,298 | 3.63% | `aggregated-de-only.txt` |
| South Korea | KR | 4,057 | 4,056 | 11,312 | 2.68% | `aggregated-kr-only.txt` |

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

