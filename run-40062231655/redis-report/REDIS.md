# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,074 | 1,075 | +0.1% | -0.61 to 2.49 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0119 to 0.00336 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.000823 to 0.000756 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.1% | -0.0128 to 0.00372 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.24 | 5.25 | +0.1% | -0.0361 to 0.0457 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.53 | 1.54 | +0.1% | -0.0148 to 0.0169 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.7 | -2.0% | -2.19 to -0.385 | GAIN |
| memory used, mean (MB) | 57.1 | 56.6 | -1.0% | -0.792 to -0.343 | GAIN |
| keys evicted | 71,719 | 71,742 | +0.0% | -230 to 277 | shown, not judged |
| host CPU busy (share of the run) | 0.0571 | 0.0636 | +11.4% | -0.133 to 0.146 | EVEN, no difference beyond the noise |
| host CPU-seconds | 40.5 | 45.6 | +12.6% | -99.5 to 110 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.209 | 0.236 | +12.5% | -0.515 to 0.568 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,284 | +1.5% | 11.4 to 25.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0319 to 0.02 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.858 | +1.6% | 0.0068 to 0.0195 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.0% | -0.0236 to 0.0198 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.25 | -0.0% | -0.0378 to 0.0348 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.885 | 0.824 | -7.0% | -0.0902 to -0.033 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 66.1 | +3.3% | 1.34 to 2.91 | power given |
| memory used, mean (MB) | 61.3 | 62.6 | +2.1% | 0.33 to 2.28 | power given |
| keys evicted | 103,244 | 94,381 | -8.6% | -12,989 to -4,737 | shown, not judged |
| host CPU busy (share of the run) | 0.0514 | 0.0575 | +11.8% | -0.0389 to 0.051 | EVEN, no difference beyond the noise |
| host CPU-seconds | 90 | 101 | +12.5% | -71.9 to 94.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.158 | 0.175 | +10.9% | -0.129 to 0.163 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.3 |  | 18.5 to 24.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 10.8 to 13.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.028 to 0.00878 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.626 | +1.3% | 0.00725 to 0.00911 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.0% | -0.0143 to 0.0101 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.73 | +0.0% | -0.00769 to 0.0104 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.21 | -2.0% | -0.0549 to -0.0353 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 0.919 to 2.29 | power given |
| memory used, mean (MB) | 60.7 | 61.8 | +1.7% | 0.654 to 1.45 | power given |
| keys evicted | 243,128 | 238,495 | -1.9% | -12,738 to 3,472 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.128 | -6.0% | -0.041 to 0.0247 | EVEN, no difference beyond the noise |
| host CPU-seconds | 229 | 213 | -6.8% | -80 to 48.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.548 | 0.504 | -8.0% | -0.199 to 0.111 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 16 |  | 8.55 to 23.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,197 | +1.1% | 10.8 to 15.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00215 to 0.000618 | EVEN, the same |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.00713 to 0.0102 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.51 | -0.1% | -0.025 to 0.0144 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.59 | -0.0% | -0.0127 to 0.011 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.19 | -3.8% | -0.0642 to -0.0304 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 66 | +3.1% | 0.726 to 3.24 | power given |
| memory used, mean (MB) | 61.2 | 62.5 | +2.2% | 0.37 to 2.34 | power given |
| keys evicted | 138,136 | 133,370 | -3.5% | -6,552 to -2,980 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.102 | -4.9% | -0.0253 to 0.0149 | EVEN, no difference beyond the noise |
| host CPU-seconds | 189 | 179 | -5.3% | -50.2 to 30.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.355 | 0.332 | -6.4% | -0.097 to 0.0519 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 15.4 to 28.6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
