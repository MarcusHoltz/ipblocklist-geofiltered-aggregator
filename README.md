# Multi-Country IP Address Internet Blocklist Aggregator

![Workflow Status](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/actions/workflows/ip-aggregation.yml/badge.svg)
![Countries](https://img.shields.io/badge/Countries-82-278EF5)
![Total IPs Blocked](https://img.shields.io/badge/Blocked_IPs-978131-2D56A8)
          
![Issues](https://img.shields.io/github/issues/MarcusHoltz/ipblocklist-geofiltered-aggregator)
![Last Commit](https://img.shields.io/github/last-commit/MarcusHoltz/ipblocklist-geofiltered-aggregator)
![Forks](https://img.shields.io/github/forks/MarcusHoltz/ipblocklist-geofiltered-aggregator)

* * *

Automated IP blocklist aggregation with multi-country geographical filtering

* * *

## 🚀 Features

- **Multi-Country Support**: Filter IPs from multiple countries - aggregate or individual lists
- **Automated Aggregation**: Combines multiple IP blocklists into a single deduplicated list
- **Geographical Filtering**: Filters IPs by country with support for multiple countries
- **Individual & Combined Files**: Generates both per-country files and combined multi-country files
- **Docker Support**: Runs in containerized environment for consistency
- **GitHub Actions**: Automated daily updates with manual trigger support
- **Multi-source**: Supports multiple URL sources via environment configuration
- **Enhanced Statistics**: Comprehensive reporting with per-country breakdowns

## 📊 Latest Statistics

**Last Updated:** 2026-11-17 10:53:20 UTC

## 📈 Country Distribution

```mermaid
pie showData title IP Blocklist Distribution by Country
"United States" : 24.5
"Germany" : 3.6
"India" : 3.4
"Singapore" : 2.9
"France" : 2.2
"Belgium" : 2.2
"The Netherlands" : 2.1
"United Kingdom" : 2.1
"Ukraine" : 2.0
"Canada" : 1.8
"Indonesia" : 1.5
"Poland" : 1.4
"Mexico" : 1.3
"Vietnam" : 1.1
"Japan" : 1.1
"South Korea" : 1.1
"Hong Kong" : 1.0
"Italy" : 1.0
"Taiwan" : 1.0
"Other/Unfiltered" : 42.9
```

## Overall Summary

- **Total Input IPs:** 978,131
- **Countries Processed:** 82
- **Combined Unique IPs:** 668,108
- **Combined Output File:** `aggregated-multi-82countries-combined.txt`
- **Overall Filter Rate:** 68.30%

## Per-Country Results

| Country | Code | Networks Found | Networks Optimized | IPs Matched | Filter Rate | Output File |
|---------|------|----------------|--------------------|-----------|-----------|-----------|
| Albania | AL | 390 | 390 | 1,045 | 0.11% | `aggregated-al-only.txt` |
| Armenia | AM | 350 | 350 | 1,020 | 0.10% | `aggregated-am-only.txt` |
| Austria | AT | 4,611 | 4,602 | 890 | 0.09% | `aggregated-at-only.txt` |
| Australia | AU | 11,850 | 11,779 | 6,631 | 0.68% | `aggregated-au-only.txt` |
| Azerbaijan | AZ | 423 | 419 | 2,060 | 0.21% | `aggregated-az-only.txt` |
| Barbados | BB | 192 | 192 | 163 | 0.02% | `aggregated-bb-only.txt` |
| Belgium | BE | 5,779 | 5,777 | 21,177 | 2.17% | `aggregated-be-only.txt` |
| Bulgaria | BG | 2,380 | 2,370 | 1,623 | 0.17% | `aggregated-bg-only.txt` |
| Bermuda | BM | 347 | 347 | 15 | 0.00% | `aggregated-bm-only.txt` |
| Brunei | BN | 122 | 122 | 47 | 0.00% | `aggregated-bn-only.txt` |
| Belarus | BY | 463 | 463 | 818 | 0.08% | `aggregated-by-only.txt` |
| Canada | CA | 17,676 | 17,560 | 17,415 | 1.78% | `aggregated-ca-only.txt` |
| Switzerland | CH | 6,627 | 6,504 | 2,897 | 0.30% | `aggregated-ch-only.txt` |
| Cameroon | CM | 186 | 186 | 176 | 0.02% | `aggregated-cm-only.txt` |
| Cyprus | CY | 855 | 855 | 379 | 0.04% | `aggregated-cy-only.txt` |
| Czechia | CZ | 3,754 | 3,752 | 1,497 | 0.15% | `aggregated-cz-only.txt` |
| Germany | DE | 30,627 | 30,519 | 34,956 | 3.57% | `aggregated-de-only.txt` |
| Denmark | DK | 3,966 | 3,959 | 691 | 0.07% | `aggregated-dk-only.txt` |
| Estonia | EE | 1,126 | 1,126 | 390 | 0.04% | `aggregated-ee-only.txt` |
| Egypt | EG | 786 | 786 | 2,448 | 0.25% | `aggregated-eg-only.txt` |
| Spain | ES | 11,654 | 11,635 | 8,075 | 0.83% | `aggregated-es-only.txt` |
| Finland | FI | 3,698 | 3,692 | 3,199 | 0.33% | `aggregated-fi-only.txt` |
| France | FR | 33,666 | 33,636 | 21,435 | 2.19% | `aggregated-fr-only.txt` |
| United Kingdom | GB | 36,568 | 36,414 | 20,503 | 2.10% | `aggregated-gb-only.txt` |
| Georgia | GE | 480 | 479 | 788 | 0.08% | `aggregated-ge-only.txt` |
| Ghana | GH | 362 | 362 | 437 | 0.04% | `aggregated-gh-only.txt` |
| Gibraltar | GI | 165 | 165 | 1 | 0.00% | `aggregated-gi-only.txt` |
| Greece | GR | 1,558 | 1,555 | 766 | 0.08% | `aggregated-gr-only.txt` |
| Hong Kong | HK | 11,320 | 11,301 | 9,845 | 1.01% | `aggregated-hk-only.txt` |
| Croatia | HR | 849 | 849 | 382 | 0.04% | `aggregated-hr-only.txt` |
| Hungary | HU | 1,830 | 1,829 | 1,052 | 0.11% | `aggregated-hu-only.txt` |
| Indonesia | ID | 6,829 | 6,808 | 14,306 | 1.46% | `aggregated-id-only.txt` |
| Ireland | IE | 5,175 | 5,171 | 5,014 | 0.51% | `aggregated-ie-only.txt` |
| Israel | IL | 2,531 | 2,529 | 4,523 | 0.46% | `aggregated-il-only.txt` |
| India | IN | 13,681 | 13,656 | 33,229 | 3.40% | `aggregated-in-only.txt` |
| Iceland | IS | 388 | 388 | 159 | 0.02% | `aggregated-is-only.txt` |
| Italy | IT | 10,034 | 10,009 | 9,749 | 1.00% | `aggregated-it-only.txt` |
| Japan | JP | 12,436 | 12,371 | 10,708 | 1.09% | `aggregated-jp-only.txt` |
| Kenya | KE | 922 | 922 | 3,043 | 0.31% | `aggregated-ke-only.txt` |
| Kyrgyzstan | KG | 256 | 256 | 502 | 0.05% | `aggregated-kg-only.txt` |
| South Korea | KR | 4,001 | 3,992 | 10,405 | 1.06% | `aggregated-kr-only.txt` |
| Kuwait | KW | 468 | 468 | 370 | 0.04% | `aggregated-kw-only.txt` |
| Cayman Islands | KY | 155 | 155 | 15 | 0.00% | `aggregated-ky-only.txt` |
| Kazakhstan | KZ | 1,359 | 1,358 | 2,350 | 0.24% | `aggregated-kz-only.txt` |
| Laos | LA | 164 | 164 | 213 | 0.02% | `aggregated-la-only.txt` |
| Liechtenstein | LI | 378 | 378 | 36 | 0.00% | `aggregated-li-only.txt` |
| Lithuania | LT | 1,515 | 1,514 | 758 | 0.08% | `aggregated-lt-only.txt` |
| Luxembourg | LU | 1,534 | 1,534 | 251 | 0.03% | `aggregated-lu-only.txt` |
| Latvia | LV | 1,264 | 1,264 | 743 | 0.08% | `aggregated-lv-only.txt` |
| Moldova | MD | 797 | 796 | 1,027 | 0.10% | `aggregated-md-only.txt` |
| Macao | MO | 125 | 125 | 136 | 0.01% | `aggregated-mo-only.txt` |
| Malta | MT | 310 | 310 | 217 | 0.02% | `aggregated-mt-only.txt` |
| Mexico | MX | 4,376 | 4,369 | 12,923 | 1.32% | `aggregated-mx-only.txt` |
| Malaysia | MY | 2,680 | 2,680 | 5,304 | 0.54% | `aggregated-my-only.txt` |
| Nigeria | NG | 1,173 | 1,173 | 1,347 | 0.14% | `aggregated-ng-only.txt` |
| The Netherlands | NL | 19,107 | 19,008 | 20,532 | 2.10% | `aggregated-nl-only.txt` |
| Norway | NO | 3,257 | 3,256 | 643 | 0.07% | `aggregated-no-only.txt` |
| Nepal | NP | 467 | 467 | 1,770 | 0.18% | `aggregated-np-only.txt` |
| New Zealand | NZ | 2,325 | 2,311 | 534 | 0.05% | `aggregated-nz-only.txt` |
| Philippines | PH | 2,240 | 2,239 | 4,393 | 0.45% | `aggregated-ph-only.txt` |
| Poland | PL | 8,497 | 8,468 | 13,675 | 1.40% | `aggregated-pl-only.txt` |
| Portugal | PT | 2,094 | 2,092 | 2,659 | 0.27% | `aggregated-pt-only.txt` |
| Qatar | QA | 491 | 491 | 1,501 | 0.15% | `aggregated-qa-only.txt` |
| Romania | RO | 4,120 | 4,109 | 2,000 | 0.20% | `aggregated-ro-only.txt` |
| Serbia | RS | 1,019 | 1,019 | 975 | 0.10% | `aggregated-rs-only.txt` |
| Saudi Arabia | SA | 1,810 | 1,810 | 2,993 | 0.31% | `aggregated-sa-only.txt` |
| Sweden | SE | 10,339 | 10,330 | 4,469 | 0.46% | `aggregated-se-only.txt` |
| Singapore | SG | 9,821 | 9,809 | 28,277 | 2.89% | `aggregated-sg-only.txt` |
| Slovenia | SI | 1,071 | 1,071 | 219 | 0.02% | `aggregated-si-only.txt` |
| Slovakia | SK | 1,180 | 1,179 | 456 | 0.05% | `aggregated-sk-only.txt` |
| Thailand | TH | 2,101 | 2,101 | 4,498 | 0.46% | `aggregated-th-only.txt` |
| Tajikistan | TJ | 153 | 153 | 221 | 0.02% | `aggregated-tj-only.txt` |
| Türkiye | TR | 3,583 | 3,551 | 8,083 | 0.83% | `aggregated-tr-only.txt` |
| Taiwan | TW | 2,465 | 2,465 | 9,490 | 0.97% | `aggregated-tw-only.txt` |
| Ukraine | UA | 5,415 | 5,374 | 19,714 | 2.02% | `aggregated-ua-only.txt` |
| Uganda | UG | 247 | 247 | 340 | 0.03% | `aggregated-ug-only.txt` |
| United States | US | 129,584 | 127,711 | 239,387 | 24.47% | `aggregated-us-only.txt` |
| British Virgin Islands | VG | 261 | 261 | 43 | 0.00% | `aggregated-vg-only.txt` |
| Vietnam | VN | 2,264 | 2,264 | 11,248 | 1.15% | `aggregated-vn-only.txt` |
| South Africa | ZA | 4,000 | 3,987 | 9,327 | 0.95% | `aggregated-za-only.txt` |
| Zambia | ZM | 172 | 172 | 205 | 0.02% | `aggregated-zm-only.txt` |
| Zimbabwe | ZW | 241 | 241 | 307 | 0.03% | `aggregated-zw-only.txt` |

## IP Sources

- **Source 1:** https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level1.netset
- **Source 2:** https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level2.netset
- **Source 3:** https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt
- **Source 4:** https://raw.githubusercontent.com/borestad/blocklist-abuseipdb/main/abuseipdb-s100-30d.ipv4
- **Source 6:** https://raw.githubusercontent.com/stamparm/ipsum/master/levels/3.txt
- **Source 7:** https://www.spamhaus.org/drop/drop.txt
- **Source 9:** https://raw.githubusercontent.com/romainmarcoux/malicious-ip/refs/heads/main/full-300k-aa.txt
- **Source 10:** https://raw.githubusercontent.com/romainmarcoux/malicious-ip/refs/heads/main/full-300k-ab.txt
- **Source 11:** https://raw.githubusercontent.com/romainmarcoux/malicious-ip/refs/heads/main/full-300k-ac.txt
- **Source 12:** https://raw.githubusercontent.com/romainmarcoux/malicious-ip/refs/heads/main/full-300k-ad.txt
- **Source 13:** https://check.torproject.org/torbulkexitlist
- **Source 14:** https://cinsscore.com/list/ci-badguys.txt
- **Source 23:** https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level3.netset

## Configuration Details


### 📁 Generated Files

Every file is on the [blocklists release](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/tag/blocklists), replaced on every run.

- **[`aggregated.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated.txt)** - 978,131 total aggregated IPs from all sources
- **[`aggregated-al-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-al-only.txt)** - 1,045 IPs from AL
- **[`aggregated-am-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-am-only.txt)** - 1,020 IPs from AM
- **[`aggregated-at-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-at-only.txt)** - 890 IPs from AT
- **[`aggregated-au-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-au-only.txt)** - 6,631 IPs from AU
- **[`aggregated-az-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-az-only.txt)** - 2,060 IPs from AZ
- **[`aggregated-bb-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-bb-only.txt)** - 163 IPs from BB
- **[`aggregated-be-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-be-only.txt)** - 21,177 IPs from BE
- **[`aggregated-bg-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-bg-only.txt)** - 1,623 IPs from BG
- **[`aggregated-bm-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-bm-only.txt)** - 15 IPs from BM
- **[`aggregated-bn-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-bn-only.txt)** - 47 IPs from BN
- **[`aggregated-by-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-by-only.txt)** - 818 IPs from BY
- **[`aggregated-ca-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-ca-only.txt)** - 17,415 IPs from CA
- **[`aggregated-ch-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-ch-only.txt)** - 2,897 IPs from CH
- **[`aggregated-cm-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-cm-only.txt)** - 176 IPs from CM
- **[`aggregated-cy-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-cy-only.txt)** - 379 IPs from CY
- **[`aggregated-cz-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-cz-only.txt)** - 1,497 IPs from CZ
- **[`aggregated-de-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-de-only.txt)** - 34,956 IPs from DE
- **[`aggregated-dk-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-dk-only.txt)** - 691 IPs from DK
- **[`aggregated-ee-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-ee-only.txt)** - 390 IPs from EE
- **[`aggregated-eg-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-eg-only.txt)** - 2,448 IPs from EG
- **[`aggregated-es-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-es-only.txt)** - 8,075 IPs from ES
- **[`aggregated-fi-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-fi-only.txt)** - 3,199 IPs from FI
- **[`aggregated-fr-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-fr-only.txt)** - 21,435 IPs from FR
- **[`aggregated-gb-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-gb-only.txt)** - 20,503 IPs from GB
- **[`aggregated-ge-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-ge-only.txt)** - 788 IPs from GE
- **[`aggregated-gh-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-gh-only.txt)** - 437 IPs from GH
- **[`aggregated-gi-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-gi-only.txt)** - 1 IPs from GI
- **[`aggregated-gr-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-gr-only.txt)** - 766 IPs from GR
- **[`aggregated-hk-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-hk-only.txt)** - 9,845 IPs from HK
- **[`aggregated-hr-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-hr-only.txt)** - 382 IPs from HR
- **[`aggregated-hu-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-hu-only.txt)** - 1,052 IPs from HU
- **[`aggregated-id-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-id-only.txt)** - 14,306 IPs from ID
- **[`aggregated-ie-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-ie-only.txt)** - 5,014 IPs from IE
- **[`aggregated-il-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-il-only.txt)** - 4,523 IPs from IL
- **[`aggregated-in-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-in-only.txt)** - 33,229 IPs from IN
- **[`aggregated-is-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-is-only.txt)** - 159 IPs from IS
- **[`aggregated-it-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-it-only.txt)** - 9,749 IPs from IT
- **[`aggregated-jp-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-jp-only.txt)** - 10,708 IPs from JP
- **[`aggregated-ke-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-ke-only.txt)** - 3,043 IPs from KE
- **[`aggregated-kg-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-kg-only.txt)** - 502 IPs from KG
- **[`aggregated-kr-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-kr-only.txt)** - 10,405 IPs from KR
- **[`aggregated-kw-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-kw-only.txt)** - 370 IPs from KW
- **[`aggregated-ky-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-ky-only.txt)** - 15 IPs from KY
- **[`aggregated-kz-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-kz-only.txt)** - 2,350 IPs from KZ
- **[`aggregated-la-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-la-only.txt)** - 213 IPs from LA
- **[`aggregated-li-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-li-only.txt)** - 36 IPs from LI
- **[`aggregated-lt-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-lt-only.txt)** - 758 IPs from LT
- **[`aggregated-lu-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-lu-only.txt)** - 251 IPs from LU
- **[`aggregated-lv-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-lv-only.txt)** - 743 IPs from LV
- **[`aggregated-md-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-md-only.txt)** - 1,027 IPs from MD
- **[`aggregated-mo-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-mo-only.txt)** - 136 IPs from MO
- **[`aggregated-mt-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-mt-only.txt)** - 217 IPs from MT
- **[`aggregated-mx-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-mx-only.txt)** - 12,923 IPs from MX
- **[`aggregated-my-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-my-only.txt)** - 5,304 IPs from MY
- **[`aggregated-ng-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-ng-only.txt)** - 1,347 IPs from NG
- **[`aggregated-nl-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-nl-only.txt)** - 20,532 IPs from NL
- **[`aggregated-no-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-no-only.txt)** - 643 IPs from NO
- **[`aggregated-np-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-np-only.txt)** - 1,770 IPs from NP
- **[`aggregated-nz-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-nz-only.txt)** - 534 IPs from NZ
- **[`aggregated-ph-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-ph-only.txt)** - 4,393 IPs from PH
- **[`aggregated-pl-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-pl-only.txt)** - 13,675 IPs from PL
- **[`aggregated-pt-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-pt-only.txt)** - 2,659 IPs from PT
- **[`aggregated-qa-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-qa-only.txt)** - 1,501 IPs from QA
- **[`aggregated-ro-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-ro-only.txt)** - 2,000 IPs from RO
- **[`aggregated-rs-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-rs-only.txt)** - 975 IPs from RS
- **[`aggregated-sa-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-sa-only.txt)** - 2,993 IPs from SA
- **[`aggregated-se-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-se-only.txt)** - 4,469 IPs from SE
- **[`aggregated-sg-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-sg-only.txt)** - 28,277 IPs from SG
- **[`aggregated-si-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-si-only.txt)** - 219 IPs from SI
- **[`aggregated-sk-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-sk-only.txt)** - 456 IPs from SK
- **[`aggregated-th-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-th-only.txt)** - 4,498 IPs from TH
- **[`aggregated-tj-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-tj-only.txt)** - 221 IPs from TJ
- **[`aggregated-tr-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-tr-only.txt)** - 8,083 IPs from TR
- **[`aggregated-tw-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-tw-only.txt)** - 9,490 IPs from TW
- **[`aggregated-ua-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-ua-only.txt)** - 19,714 IPs from UA
- **[`aggregated-ug-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-ug-only.txt)** - 340 IPs from UG
- **[`aggregated-us-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-us-only.txt)** - 239,387 IPs from US
- **[`aggregated-vg-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-vg-only.txt)** - 43 IPs from VG
- **[`aggregated-vn-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-vn-only.txt)** - 11,248 IPs from VN
- **[`aggregated-za-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-za-only.txt)** - 9,327 IPs from ZA
- **[`aggregated-zm-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-zm-only.txt)** - 205 IPs from ZM
- **[`aggregated-zw-only.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-zw-only.txt)** - 307 IPs from ZW
- **[`aggregated-multi-82countries-combined.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/aggregated-multi-82countries-combined.txt)** - 668,108 unique IPs (deduplicated across all countries)
- **[`geo_allow.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/geo_allow.txt)** - 133,998 ranges covering every configured country
- **[`allow_ops.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/allow_ops.txt)** - Stripe webhook sender addresses
- **[`bl_single.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/bl_single.txt)** - 636,893 single addresses from the combined file
- **[`bl_range.txt`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/bl_range.txt)** - 31,215 ranges from the combined file
- **[`SHA256SUMS`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/SHA256SUMS)** - checksums of the four files above
- **[`country-samples.tsv`](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/releases/download/blocklists/country-samples.tsv)** - addresses the every-country check tested

---

## 🛴 Install

Set up your own copy of this repository to aggregate and filter your IP blocklists for multiple countries.

* * *

### 👆 Click the green "Use this template" button in the upper right corner

         
1. **Sign in** to GitHub and navigate to [this repository](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator).
2. Click the **"Use this template"** button (in the upper right corner).
3. Select **Create a new repository**. Enter a name (e.g., `my-eu-badip-blocklist`), and confirm.
4. Your new repository is now independent — it will not share commit history with the original.
5. You can immediately begin editing or configuring it for your own multi-country IP aggregation project.

> The **"Use this template"** button on GitHub allows you to quickly create a new, independent repository pre-populated with the project's files and structure. Your new repository won't inherit commit history from the template. This is perfect for your personal blocklist repo.

*Usage is below for steps on running this repository with Github Actions in your new IP aggregation project.*


## 🛠 Usage

### GitHub Actions (Recommended)

#### First Step - Enable Write Permissions

1. **Enable Actions**: Go to Settings > Actions > General > Workflow permissions
2. **Set Permissions**: Select "Read and write permissions", click "Save".


#### Second Step - Configure The Repo

3. **Configure Environment**: Edit `.env` file with your desired sources and countries
4. **Your Favorite Blocklists**: Load as many blocklists as you like, just make sure the line starts with `LIST1_`, `LIST2_`, `LIST3_`, etc.
5. **Multiple Countries**: Countries can be modified the same way, `COUNTRY_ISO_CODE_1`, `COUNTRY_NAME_1`, `COUNTRY_ISO_CODE_2`, `COUNTRY_NAME_2`, etc.
6. **Find Country Codes**: You can find your country codes in the [geoip2-ipv4 spreadsheet](https://datahub.io/core/geoip2-ipv4)
7. **Automatic Runs**: The workflow runs twice daily. At both **02:17 AM/PM UTC** or it will run anytime if you [modified the cron file](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/edit/main/.github/workflows/ip-aggregation.yml)


#### Third Step - Running This Action

8. **Run This Now**: You can run this Github Action by using the "Action" tab up top
9. **Generate Multi-Country Blocklists**: Under "All workflows" you can find this action
10. **Run workflow**: On this page, off to the right is a button with a dropdown to "Run workflow"
11. **Off to the races**: Each run will consume some of your free monthly Github Actions 2000 min (33.3 hours)

> Please adjust cron, it is how often your aggregator runs in [.github/workflows/ip-aggregation.yml](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/edit/main/.github/workflows/ip-aggregation.yml), also modify your blacklists and countries in the [.env](https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator/edit/main/.env) file.

## ⚙ Configuration

### 🌍 Multi-Country Setup

The `.env` file supports multiple countries:

```bash
# European Union Example
COUNTRY_ISO_CODE_1=DE
COUNTRY_NAME_1=Germany

COUNTRY_ISO_CODE_2=FR
COUNTRY_NAME_2=France

COUNTRY_ISO_CODE_3=NL
COUNTRY_NAME_3=Netherlands

COUNTRY_ISO_CODE_4=IT
COUNTRY_NAME_4=Italy

COUNTRY_ISO_CODE_5=ES
COUNTRY_NAME_5=Spain
```

This will generate:
- `aggregated-de-only.txt` (Germany IPs)
- `aggregated-fr-only.txt` (France IPs) 
- `aggregated-nl-only.txt` (Netherlands IPs)
- `aggregated-it-only.txt` (Italy IPs)
- `aggregated-es-only.txt` (Spain IPs)
- `aggregated-multi-5countries-combined.txt` (All countries combined, deduplicated)

### Sample .env file

```bash
# Add your IP list sources
LIST_1=https://example.com/blocklist1.txt
LIST_2=https://example.com/blocklist2.txt

# Set multiple countries (NEW FEATURE!)
COUNTRY_ISO_CODE_1=DE
COUNTRY_NAME_1=Germany

COUNTRY_ISO_CODE_2=FR  
COUNTRY_NAME_2=France

# Configure paths (usually don't need to change)
GEOIP_CSV_PATH=/data/geoip/geoip2-ipv4.csv
ALL_IPS_FROM_LISTS=/data/output/aggregated.txt
```

## 🏠 Local Deployment (Alternative)

If you'd rather download this repo and run this project offline, the instructions are below:

### 1. Clone the repository

The first step is to download the files from the internet, and get them locally on your machine.

```bash
git clone https://github.com/MarcusHoltz/ipblocklist-geofiltered-aggregator.git
```

### 2. Configure your sources and countries in .env

The next step is to configure the project to your liking. Edit your `.env` file. You can enter as many IP based block lists as you need and configure multiple countries.

```bash
nano .env
```

### 3. Run with Docker Compose

You can now run the project and see what happens.

```bash
docker compose up --build
```

### 4. Check results

Let's see what happened!

```bash
ls -la data/output/
```

## 📁 Output Files

### Per-Country Files
- `data/output/aggregated-{country-code}-only.txt` - Country-specific IPs (e.g., `aggregated-de-only.txt` for Germany)

### Combined Multi-Country Files  
- `data/output/aggregated-multi-{number-of-countries-total}countries-combined.txt` - Combined IPs from all countries (deduplicated)
- Example: `aggregated-multi-3countries-combined.txt` for Germany + France + Netherlands

### Core Files
- `data/output/aggregated.txt` - All deduplicated IPs from all sources (before country filtering)
- `data/output/stats.md` - Comprehensive processing statistics with per-country breakdowns

## 🔄 Workflow Triggers

The GitHub Action runs automatically when:

- **Daily Schedule**: Every day, twice. Once at at 02:17 AM UTC and then again at 02:17 PM UTC
- **File Changes**: When `.env`, `Dockerfile`, or key scripts are modified
- **Manual Trigger**: Via GitHub Actions interface


## ⚡ Performance

- **Multi-Country Processing**: Parallel processing of multiple countries
- **Processing Speed**: ~10,000 IPs per second for filtering per country
- **Parallel Processing**: Multi-core optimization for large datasets  
- **Memory Efficient**: Streaming processing for large files
- **Optimized Lookup**: Integer-based IP range matching with SubnetTree
- **Network Optimization**: Automatic collapsing of overlapping CIDR blocks

## 🌼 Features and Optimizations

- **🌍 Multi-country IP blocklist aggregation** for comprehensive regional security  
- **📊 Per-country statistical analysis** with detailed filtering metrics
- **🔄 Automated multi-country updates** via GitHub Actions
- **🚀 Parallel country processing** for improved performance
- **📁 Individual and combined output files** for flexible deployment
- **🛡️ Regional threat mitigation** with configurable multi-country rules
- **💾 Memory-efficient processing** even with multiple large country datasets
- **🔗 Network optimization** with automatic CIDR block collapsing

## 👍 Acknowledgements

This project would not have been possible without the amazing work of the following other projects:

* * *

### 🎩 Datopian

Thank you to [Datopian](https://github.com/datasets/geoip2-ipv4) for maintaining the [GeoIP2 IPv4 dataset](https://datahub.io/core/geoip2-ipv4). This dataset provides otherwise impossible information for IP geolocation, allowing this project to filter IPs based on multiple countries simultaneously.

- [GeoIP2 IPv4 Dataset](https://datahub.io/core/geoip2-ipv4) by Datopian is essential for filtering and identifying IP addresses across various countries, enabling the dynamic multi-country functionality of this project.


* * *

### 🦘 Andrew Twin

Special thanks to [Andrew Twin](https://github.com/andrewtwin) for creating and sharing the [IP Aggregator](https://github.com/andrewtwin/ip-aggregator) project. Andrew's work on efficiently aggregating IP blocklists was a fundamental inspiration and foundation for this enhanced multi-country version.

- The [IP Aggregator](https://github.com/andrewtwin/ip-aggregator) allows easy downloading, parsing, and filtering of multiple IP blocklists, which this project leverages and extends for multi-country IP management tasks.


* * *

### 📗 Blocklist maintainers

I would like to additionally acknowledge the maintainers and contributors of various [IP blocklists](https://github.com/topics/ip-blocklist) and [IP blacklists](https://github.com/topics/ip-blacklist). Thank you for maintaining up-to-date, community-driven threat intelligence that forms the foundation of generating these multi-country filtered files. While the specific lists in this repo may vary, the collective dedication to improving online security and privacy of all contributors is deeply appreciated.


* * *

