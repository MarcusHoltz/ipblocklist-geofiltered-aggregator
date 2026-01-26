# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-01-26 14:50:37 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 17.7
"Germany" : 4.1
"Canada" : 2.6
"United Kingdom" : 2.4
"South Korea" : 1.8
"Australia" : 1.2
"Other/Unfiltered" : 70.1
```

## Overall Summary

- **Total Input IPs:** 463,518
- **Countries Processed:** 6
- **Combined Unique IPs:** 138,623
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 29.91%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 191,318 | 189,710 | 82,155 | 17.72% | `aggregated-us-only.txt` |
| Canada | CA | 17,196 | 17,071 | 11,870 | 2.56% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,750 | 33,592 | 11,317 | 2.44% | `aggregated-gb-only.txt` |
| Australia | AU | 11,508 | 11,442 | 5,792 | 1.25% | `aggregated-au-only.txt` |
| Germany | DE | 27,570 | 27,449 | 18,915 | 4.08% | `aggregated-de-only.txt` |
| South Korea | KR | 3,997 | 3,983 | 8,574 | 1.85% | `aggregated-kr-only.txt` |

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

