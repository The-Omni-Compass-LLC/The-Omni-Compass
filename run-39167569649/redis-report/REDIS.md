# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -1.11 to -0.604 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0357 to 0.0219 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.1% | -0.00072 to -0.000379 | LOSS |
| latency, 95th percentile (ms) | 5.64 | 5.64 | -0.0% | -0.0454 to 0.0436 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.71 | +0.1% | -0.0331 to 0.0397 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.66 | 1.66 | +0.3% | -0.0107 to 0.0222 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.6 | -2.2% | -1.56 to -1.31 | GAIN |
| memory used, mean (MB) | 57.2 | 56.6 | -0.9% | -0.62 to -0.384 | GAIN |
| keys evicted | 71,589 | 71,748 | +0.2% | 126 to 193 | shown, not judged |
| host CPU busy (share of the run) | 0.0932 | 0.113 | +21.5% | -0.0266 to 0.0666 | EVEN, no difference beyond the noise |
| host CPU-seconds | 64.4 | 80.2 | +24.6% | -23 to 54.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.332 | 0.414 | +24.7% | -0.119 to 0.283 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,282 | +1.4% | 9.78 to 25 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.038 to 0.0197 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.856 | +1.4% | 0.00583 to 0.017 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.23 | +0.1% | -0.0117 to 0.0179 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.27 | +0.2% | -0.00016 to 0.0261 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.89 | 0.835 | -6.2% | -0.0813 to -0.03 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.4 | +0.6% | -0.25 to 0.996 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.2 | -0.1% | -0.296 to 0.17 | EVEN, no difference beyond the noise |
| keys evicted | 103,618 | 96,130 | -7.2% | -11,233 to -3,744 | shown, not judged |
| host CPU busy (share of the run) | 0.0471 | 0.0578 | +22.7% | -0.00358 to 0.025 | EVEN, no difference beyond the noise |
| host CPU-seconds | 81.9 | 102 | +24.0% | -7.03 to 46.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.144 | 0.176 | +22.4% | -0.0148 to 0.0792 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.3% | 10.1 to 13.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0209 to 0.0129 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00678 to 0.00899 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.69 | +0.1% | 0.0028 to 0.00532 | LOSS |
| latency, 99th percentile (ms) | 5.73 | 5.74 | +0.2% | 0.00626 to 0.0172 | LOSS |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% | -0.0496 to -0.0294 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 0.632 to 2.29 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.996 to 1.36 | power given |
| keys evicted | 243,233 | 236,900 | -2.6% | -14,997 to 2,331 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.142 | +2.4% | -0.0205 to 0.0272 | EVEN, no difference beyond the noise |
| host CPU-seconds | 232 | 239 | +2.9% | -39.2 to 52.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.557 | 0.567 | +1.6% | -0.101 to 0.119 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.7 |  | 10.9 to 18.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,197 | +1.1% | 6.46 to 19.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00197 to 0.00278 | EVEN, the same |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.0043 to 0.013 | GAIN |
| latency, 95th percentile (ms) | 5.62 | 5.62 | -0.0% | -0.00557 to 0.00405 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.7 | 5.7 | +0.0% | -0.0119 to 0.0176 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.28 | 1.23 | -3.5% | -0.0652 to -0.0245 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.8 | +2.9% | 0.18 to 3.49 | power given |
| memory used, mean (MB) | 61.2 | 62.5 | +2.1% | -0.0949 to 2.62 | EVEN, no difference beyond the noise |
| keys evicted | 138,100 | 133,371 | -3.4% | -8,817 to -642 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.104 | +3.1% | -0.0286 to 0.0349 | EVEN, no difference beyond the noise |
| host CPU-seconds | 176 | 182 | +3.6% | -54.8 to 67.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.33 | 0.338 | +2.5% | -0.104 to 0.12 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 17.7 to 26.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
