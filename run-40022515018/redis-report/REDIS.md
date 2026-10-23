# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -1.98 to -0.158 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0198 to 0.0221 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00109 to 1.7e-05 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.78 | 5.78 | +0.0% | -0.00796 to 0.00929 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.85 | 5.87 | +0.3% | 0.0146 to 0.0217 | LOSS |
| latency, mean (ms) | 1.76 | 1.77 | +0.6% | -0.00517 to 0.0247 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.4 | -4.1% | -4.73 to -0.451 | GAIN |
| memory used, mean (MB) | 57.2 | 55.5 | -3.0% | -3.92 to 0.519 | EVEN, no difference beyond the noise |
| keys evicted | 71,738 | 71,900 | +0.2% | 8 to 315 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.152 | +15.0% | -0.00233 to 0.042 | EVEN, no difference beyond the noise |
| host CPU-seconds | 86.4 | 102 | +17.5% | -1.66 to 31.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.446 | 0.525 | +17.6% | -0.0082 to 0.165 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 8.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,283 | +1.5% | 13.4 to 25.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00342 to 0.00323 | EVEN, the same |
| cache hit rate | 0.845 | 0.857 | +1.5% | 0.00777 to 0.017 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.1% | -0.0182 to 0.0243 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.33 | +1.3% | -0.156 to 0.292 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.897 | 0.833 | -7.2% | -0.0822 to -0.0461 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 66 | +3.1% | 1.23 to 2.68 | power given |
| memory used, mean (MB) | 61.3 | 62.5 | +2.0% | 0.867 to 1.52 | power given |
| keys evicted | 103,371 | 95,029 | -8.1% | -11,065 to -5,619 | shown, not judged |
| host CPU busy (share of the run) | 0.075 | 0.051 | -32.0% | -0.0836 to 0.0356 | EVEN, no difference beyond the noise |
| host CPU-seconds | 135 | 88.9 | -33.9% | -159 to 67.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.236 | 0.154 | -34.9% | -0.28 to 0.115 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 14.7 to 23.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 8.75 to 14.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.02 to 0.0085 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00591 to 0.00952 | GAIN |
| latency, 95th percentile (ms) | 5.6 | 5.6 | +0.0% | -0.0017 to 0.00433 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.67 | 5.68 | +0.1% | 0.000156 to 0.0149 | LOSS |
| latency, mean (ms) | 2.19 | 2.15 | -1.8% | -0.0487 to -0.0313 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.6% | 0.316 to 3.07 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.1 to 1.33 | power given |
| keys evicted | 243,131 | 235,562 | -3.1% | -9,832 to -5,307 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.123 | +0.9% | -0.0294 to 0.0315 | EVEN, no difference beyond the noise |
| host CPU-seconds | 215 | 217 | +1.0% | -58.8 to 63 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.517 | 0.515 | -0.3% | -0.146 to 0.143 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.3 |  | 3.99 to 24.7 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,193 | +0.8% | 3.56 to 15.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0121 to 0.0132 | EVEN, the same |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.00246 to 0.0102 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.0% | -0.011 to 0.0115 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.83 | +0.1% | -0.0116 to 0.0283 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.32 | -2.4% | -0.0607 to -0.00424 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.8 | +1.2% | -0.0286 to 1.59 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 61.7 | +0.9% | 0.238 to 0.849 | power given |
| keys evicted | 138,176 | 135,263 | -2.1% | -4,565 to -1,262 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.127 | +19.8% | 0.00103 to 0.0411 | power given |
| host CPU-seconds | 174 | 213 | +22.6% | 5.57 to 73 | power given |
| host CPU-seconds per 1,000 requests inside the line | 0.327 | 0.397 | +21.6% | 0.00519 to 0.136 | power given |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 10.5 to 32.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
