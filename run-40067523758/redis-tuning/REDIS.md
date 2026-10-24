# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.2% | 12.3 to 15.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0149 to 0.00407 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.00804 to 0.00993 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.23 | +0.3% | -0.0238 to 0.0525 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.33 | +1.1% | -0.0993 to 0.213 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.13 | -3.7% | -0.0571 to -0.03 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 0.723 to 2.18 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +1.9% | 1.01 to 1.32 | power given |
| keys evicted | 138,233 | 132,994 | -3.8% | -5,869 to -4,608 | shown, not judged |
| host CPU busy (share of the run) | 0.0553 | 0.0711 | +28.5% | -0.0224 to 0.0539 | EVEN, no difference beyond the noise |
| host CPU-seconds | 96.7 | 126 | +30.1% | -41.2 to 99.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.182 | 0.234 | +28.5% | -0.0796 to 0.183 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
