# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-02-12 04:34:34 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 19.1
"Germany" : 3.9
"Canada" : 2.4
"United Kingdom" : 2.2
"South Korea" : 2.0
"Australia" : 1.4
"Other/Unfiltered" : 68.9
```

## Overall Summary

- **Total Input IPs:** 381,799
- **Countries Processed:** 6
- **Combined Unique IPs:** 118,549
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 31.05%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 187,914 | 186,301 | 72,820 | 19.07% | `aggregated-us-only.txt` |
| Canada | CA | 16,725 | 16,598 | 9,032 | 2.37% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,454 | 33,292 | 8,588 | 2.25% | `aggregated-gb-only.txt` |
| Australia | AU | 11,406 | 11,340 | 5,403 | 1.42% | `aggregated-au-only.txt` |
| Germany | DE | 27,868 | 27,751 | 15,011 | 3.93% | `aggregated-de-only.txt` |
| South Korea | KR | 4,014 | 4,000 | 7,695 | 2.02% | `aggregated-kr-only.txt` |

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

