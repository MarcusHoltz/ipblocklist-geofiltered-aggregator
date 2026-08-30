# Multi-Country IP Aggregation Statistics

**Last Updated:** 2026-08-30 18:06:32 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 20.3
"Germany" : 3.1
"United Kingdom" : 1.9
"Canada" : 1.8
"South Korea" : 1.3
"Australia" : 0.8
"Other/Unfiltered" : 70.9
```

## Overall Summary

- **Total Input IPs:** 474,726
- **Countries Processed:** 6
- **Combined Unique IPs:** 138,154
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 29.10%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 130,784 | 128,927 | 96,241 | 20.27% | `aggregated-us-only.txt` |
| Canada | CA | 17,155 | 17,039 | 8,501 | 1.79% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 35,780 | 35,619 | 8,793 | 1.85% | `aggregated-gb-only.txt` |
| Australia | AU | 12,241 | 12,174 | 3,625 | 0.76% | `aggregated-au-only.txt` |
| Germany | DE | 29,886 | 29,769 | 14,753 | 3.11% | `aggregated-de-only.txt` |
| South Korea | KR | 3,921 | 3,910 | 6,241 | 1.31% | `aggregated-kr-only.txt` |

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

