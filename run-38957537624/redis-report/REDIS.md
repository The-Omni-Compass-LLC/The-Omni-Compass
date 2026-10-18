# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | +0.0% | -1.23 to 1.82 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0454 to 0.031 | EVEN, no difference beyond the noise |
| cache hit rate | 0.717 | 0.718 | +0.0% | -0.000859 to 0.0013 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.65 | 5.65 | +0.0% | -0.00509 to 0.008 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.71 | +0.1% | -0.00263 to 0.0132 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.67 | 1.67 | +0.1% | -0.00152 to 0.00521 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -1.62 to -1.28 | GAIN |
| memory used, mean (MB) | 57.2 | 56.6 | -0.9% | -0.619 to -0.387 | GAIN |
| keys evicted | 71,795 | 71,746 | -0.1% | -308 to 209 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.117 | -1.7% | -0.0447 to 0.0406 | EVEN, no difference beyond the noise |
| host CPU-seconds | 84.1 | 82.3 | -2.1% | -35.9 to 32.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.434 | 0.425 | -2.1% | -0.186 to 0.168 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,285 | +1.4% | 0.917 to 35.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000569 to 0.00178 | EVEN, the same |
| cache hit rate | 0.845 | 0.857 | +1.4% | 0.000197 to 0.0238 | GAIN |
| latency, 95th percentile (ms) | 5.54 | 5.54 | -0.1% | -0.0274 to 0.0217 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.63 | 5.63 | +0.1% | -0.00419 to 0.0123 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.968 | 0.906 | -6.4% | -0.124 to 0.00017 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.6 | +1.0% | -3.04 to 4.32 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.5 | +0.4% | -3.3 to 3.74 | EVEN, no difference beyond the noise |
| keys evicted | 103,364 | 95,559 | -7.6% | -16,050 to 441 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.109 | +8.4% | -0.0402 to 0.0571 | EVEN, no difference beyond the noise |
| host CPU-seconds | 176 | 193 | +9.8% | -80.4 to 115 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.309 | 0.334 | +8.2% | -0.14 to 0.191 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.7 |  | 13.3 to 32.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 936 | +1.3% | 7.34 to 16.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0767 to 0.062 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00623 to 0.0095 | GAIN |
| latency, 95th percentile (ms) | 5.65 | 5.64 | -0.1% | -0.0867 to 0.0745 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.26 | 6.26 | +0.0% | -1.93 to 1.94 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.2 | -2.3% | -0.156 to 0.0538 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 0.988 to 1.88 | power given |
| memory used, mean (MB) | 60.7 | 61.8 | +1.8% | 0.891 to 1.24 | power given |
| keys evicted | 243,199 | 240,030 | -1.3% | -6,568 to 230 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.134 | -1.9% | -0.0219 to 0.0167 | EVEN, no difference beyond the noise |
| host CPU-seconds | 240 | 236 | -1.8% | -43.3 to 34.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.577 | 0.56 | -3.1% | -0.111 to 0.0751 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15.3 |  | 7.74 to 22.9 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,198 | +1.2% | 12.7 to 16 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00468 to 0.00192 | EVEN, the same |
| cache hit rate | 0.789 | 0.799 | +1.2% | 0.00854 to 0.0106 | GAIN |
| latency, 95th percentile (ms) | 5.54 | 5.53 | -0.1% | -0.0361 to 0.0235 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.61 | -0.0% | -0.0234 to 0.0178 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.25 | 1.19 | -4.2% | -0.0656 to -0.0397 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.8 | +2.8% | 1.57 to 1.98 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +2.1% | 1.08 to 1.43 | power given |
| keys evicted | 138,160 | 132,529 | -4.1% | -6,320 to -4,942 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.0962 | -6.6% | -0.0399 to 0.0263 | EVEN, no difference beyond the noise |
| host CPU-seconds | 181 | 168 | -7.3% | -78 to 51.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.34 | 0.311 | -8.4% | -0.15 to 0.0932 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 23 to 23 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
