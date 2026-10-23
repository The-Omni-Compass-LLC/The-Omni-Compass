# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
