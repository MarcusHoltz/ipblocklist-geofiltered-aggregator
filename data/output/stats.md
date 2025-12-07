# Multi-Country IP Aggregation Statistics

**Last Updated:** 2025-12-07 03:44:34 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 18.0
"Germany" : 3.8
"South Korea" : 2.8
"United Kingdom" : 2.3
"Canada" : 2.1
"Australia" : 1.4
"Other/Unfiltered" : 69.7
```

## Overall Summary

- **Total Input IPs:** 400,730
- **Countries Processed:** 6
- **Combined Unique IPs:** 121,547
- **Combined Output File:** `aggregated-multi-6countries-combined.txt`
- **Overall Filter Rate:** 30.33%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| United States | US | 208,444 | 206,866 | 72,273 | 18.04% | `aggregated-us-only.txt` |
| Canada | CA | 17,376 | 17,261 | 8,504 | 2.12% | `aggregated-ca-only.txt` |
| United Kingdom | GB | 33,249 | 33,123 | 9,109 | 2.27% | `aggregated-gb-only.txt` |
| Australia | AU | 11,332 | 11,274 | 5,453 | 1.36% | `aggregated-au-only.txt` |
| Germany | DE | 27,316 | 27,187 | 15,034 | 3.75% | `aggregated-de-only.txt` |
| South Korea | KR | 4,031 | 4,030 | 11,174 | 2.79% | `aggregated-kr-only.txt` |

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

