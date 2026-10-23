# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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
