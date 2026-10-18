# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,075 | -0.1% | -4.31 to 1.99 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0166 to 0.0183 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00268 to 0.00135 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.58 | 5.6 | +0.4% | -0.0622 to 0.104 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.63 | 5.67 | +0.7% | -0.0918 to 0.17 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.63 | 1.65 | +0.9% | -0.0462 to 0.0771 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -1.68 to -1.22 | GAIN |
| memory used, mean (MB) | 57.1 | 56.6 | -0.9% | -0.801 to -0.201 | GAIN |
| keys evicted | 71,646 | 71,838 | +0.3% | -370 to 756 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.116 | -4.2% | -0.0216 to 0.0115 | EVEN, no difference beyond the noise |
| host CPU-seconds | 86.2 | 81.5 | -5.4% | -18 to 8.62 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.445 | 0.421 | -5.3% | -0.0931 to 0.0456 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,283 | +1.3% | 6.18 to 26.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00464 to 0.00433 | EVEN, the same |
| cache hit rate | 0.845 | 0.856 | +1.3% | 0.00415 to 0.018 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.0% | -0.0138 to 0.00874 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.1% | -0.00587 to 0.0183 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.997 | -5.4% | -0.0862 to -0.0267 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.6 | -0.6% | -4.71 to 3.99 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 60.5 | -1.3% | -5.03 to 3.44 | EVEN, no difference beyond the noise |
| keys evicted | 103,611 | 96,556 | -6.8% | -12,161 to -1,950 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.117 | +9.5% | -0.0276 to 0.0478 | EVEN, no difference beyond the noise |
| host CPU-seconds | 176 | 195 | +11.0% | -50.9 to 89.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.308 | 0.337 | +9.5% | -0.0898 to 0.149 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 12.6 to 44.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 11.2 to 11.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0139 to -0.00557 | LOSS |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00744 to 0.00798 | GAIN |
| latency, 95th percentile (ms) | 5.62 | 5.64 | +0.2% | -0.0309 to 0.0564 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.69 | 5.7 | +0.3% | -0.0183 to 0.0564 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.18 | 2.16 | -1.2% | -0.0654 to 0.0127 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.1% | 1.14 to 1.58 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.16 to 1.31 | power given |
| keys evicted | 243,159 | 234,810 | -3.4% | -8,533 to -8,167 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.123 | -1.4% | -0.0346 to 0.0312 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 216 | -2.2% | -74.4 to 64.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.531 | 0.513 | -3.4% | -0.185 to 0.148 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.7 |  | 7.93 to 19.4 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,195 | +1.1% | 10.8 to 14.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0113 to 0.00238 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.00642 to 0.0104 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.22 | +0.1% | -0.00808 to 0.0138 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.26 | +0.1% | 0.000815 to 0.0105 | LOSS |
| latency, mean (ms) | 1.17 | 1.13 | -3.7% | -0.0514 to -0.0356 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 0.31 to 2.91 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.9% | 0.216 to 2.07 | power given |
| keys evicted | 138,209 | 133,371 | -3.5% | -6,185 to -3,491 | shown, not judged |
| host CPU busy (share of the run) | 0.0695 | 0.0614 | -11.7% | -0.0484 to 0.0322 | EVEN, no difference beyond the noise |
| host CPU-seconds | 124 | 108 | -12.6% | -91.9 to 60.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.233 | 0.201 | -13.5% | -0.174 to 0.111 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 21 to 21 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
