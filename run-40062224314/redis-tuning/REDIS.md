# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,193 | +0.8% | 1.46 to 17.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00155 to 0.00299 | EVEN, the same |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.00117 to 0.0116 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.0% | -0.00884 to 0.0118 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.2% | -0.0011 to 0.0204 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.32 | -2.3% | -0.064 to 0.00118 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.6% | -0.479 to 2.58 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62 | +1.3% | -0.0483 to 1.69 | EVEN, no difference beyond the noise |
| keys evicted | 138,215 | 134,753 | -2.5% | -6,960 to 34.7 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.125 | +0.5% | -0.0295 to 0.0307 | EVEN, no difference beyond the noise |
| host CPU-seconds | 207 | 209 | +0.6% | -55.9 to 58.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.389 | 0.389 | -0.2% | -0.109 to 0.108 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 6.19 to 29.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
