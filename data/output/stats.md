# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-10-02 14:37:09 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 13.4
"Germany" : 3.3
"South Korea" : 2.4
"Canada" : 2.0
"United Kingdom" : 1.7
"Australia" : 0.9
"Other/Unfiltered" : 76.4
```

## Overall Summary

- **Total Input IPs:** 549,376
- **Countries Processed:** 6
- **Combined Unique IPs:** 129,850
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 23.64%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 225,472 | 222,928 | 73,428 | 13.37% | `aggregated-us-only.txt` |
| Canada | CA | 17,937 | 17,822 | 11,117 | 2.02% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 32,943 | 32,788 | 9,490 | 1.73% | `aggregated-gb-only.txt` |
| Australia | AU | 11,681 | 11,621 | 4,698 | 0.86% | `aggregated-au-only.txt` |
| Germany | DE | 27,612 | 27,495 | 18,083 | 3.29% | `aggregated-de-only.txt` |
| South Korea | KR | 4,005 | 4,004 | 13,034 | 2.37% | `aggregated-kr-only.txt` |

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

