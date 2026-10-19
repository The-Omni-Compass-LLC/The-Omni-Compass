# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -1.85 to 0.858 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00469 to 0.0204 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00118 to 0.000659 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.0% | -0.0149 to 0.0145 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.1% | -0.0178 to 0.0341 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.75 | +0.2% | -0.00204 to 0.0102 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.4% | -1.8 to -1.25 | GAIN |
| memory used, mean (MB) | 57.2 | 56.6 | -1.1% | -0.864 to -0.338 | GAIN |
| keys evicted | 71,742 | 71,826 | +0.1% | -153 to 322 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.139 | +10.1% | -0.0886 to 0.114 | EVEN, no difference beyond the noise |
| host CPU-seconds | 83.5 | 93.6 | +12.2% | -67.3 to 87.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.431 | 0.483 | +12.2% | -0.347 to 0.452 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,287 | +1.6% | 20.2 to 21.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00842 to 0.00484 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.859 | +1.6% | 0.0131 to 0.0146 | GAIN |
| latency, 95th percentile (ms) | 5.49 | 5.48 | -0.2% | -0.0222 to 0.000264 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.1% | -0.00641 to 0.0125 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.958 | 0.887 | -7.4% | -0.0762 to -0.0657 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.3% | -0.00659 to 1.73 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.8 | +0.8% | 0.125 to 0.911 | power given |
| keys evicted | 103,456 | 94,321 | -8.8% | -9,641 to -8,630 | shown, not judged |
| host CPU busy (share of the run) | 0.0892 | 0.095 | +6.5% | -0.0343 to 0.046 | EVEN, no difference beyond the noise |
| host CPU-seconds | 155 | 166 | +7.4% | -65.5 to 88.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.271 | 0.287 | +5.7% | -0.118 to 0.149 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.2% | 10.1 to 13 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0284 to 0.0142 | EVEN, no difference beyond the noise |
| cache hit rate | 0.618 | 0.625 | +1.3% | 0.00677 to 0.00873 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.0074 to 0.0108 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | -0.00757 to 0.0258 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% | -0.0415 to -0.0348 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 0.961 to 1.79 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.888 to 1.45 | power given |
| keys evicted | 243,036 | 236,790 | -2.6% | -14,799 to 2,308 | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.147 | +13.3% | 0.00114 to 0.0333 | power given |
| host CPU-seconds | 214 | 248 | +15.7% | 3.51 to 63.7 | power given |
| host CPU-seconds per 1,000 requests inside the line | 0.513 | 0.587 | +14.3% | 0.00192 to 0.145 | power given |
| ceiling changes written (the knob's moves) | 0 | 14.7 |  | 10.9 to 18.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,197 | +1.1% | 4.39 to 21 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.006 to 0.00569 | EVEN, the same |
| cache hit rate | 0.79 | 0.798 | +1.1% | 0.00312 to 0.0137 | GAIN |
| latency, 95th percentile (ms) | 5.2 | 5.2 | +0.0% | -0.00293 to 0.00373 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.00609 to 0.00761 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.15 | 1.1 | -3.8% | -0.0735 to -0.0139 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.8 | +2.9% | 0.0628 to 3.6 | power given |
| memory used, mean (MB) | 61.2 | 62.5 | +2.2% | 0.213 to 2.46 | power given |
| keys evicted | 137,976 | 133,127 | -3.5% | -8,435 to -1,262 | shown, not judged |
| host CPU busy (share of the run) | 0.0465 | 0.0543 | +16.7% | -0.0592 to 0.0748 | EVEN, no difference beyond the noise |
| host CPU-seconds | 81.9 | 96.4 | +17.8% | -108 to 137 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.154 | 0.179 | +16.6% | -0.203 to 0.254 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 15.9 to 27.4 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
