# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-05-12 05:49:50 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.8
"Germany" : 4.8
"United Kingdom" : 3.6
"Australia" : 2.5
"Canada" : 2.4
"South Korea" : 1.5
"Other/Unfiltered" : 67.4
```

## Overall Summary

- **Total Input IPs:** 442,163
- **Countries Processed:** 6
- **Combined Unique IPs:** 144,186
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 32.61%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 167,975 | 166,467 | 78,926 | 17.85% | `aggregated-us-only.txt` |
| Canada | CA | 17,039 | 16,905 | 10,756 | 2.43% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 34,028 | 33,858 | 15,982 | 3.61% | `aggregated-gb-only.txt` |
| Australia | AU | 12,110 | 12,041 | 10,882 | 2.46% | `aggregated-au-only.txt` |
| Germany | DE | 28,807 | 28,725 | 21,127 | 4.78% | `aggregated-de-only.txt` |
| South Korea | KR | 3,984 | 3,974 | 6,513 | 1.47% | `aggregated-kr-only.txt` |

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

