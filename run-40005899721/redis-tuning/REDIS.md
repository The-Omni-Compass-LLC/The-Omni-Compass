# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,195 | +1.0% | 4.34 to 18.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00443 to 0.0107 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.797 | +1.0% | 0.00286 to 0.0124 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.74 | +0.0% | -0.0116 to 0.014 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.1% | -0.0123 to 0.0233 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.3 | -2.8% | -0.0661 to -0.0105 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 0.219 to 2.45 | power given |
| memory used, mean (MB) | 61.2 | 62.2 | +1.6% | 0.0419 to 1.96 | power given |
| keys evicted | 138,139 | 133,815 | -3.1% | -7,559 to -1,088 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.129 | +12.7% | -0.0192 to 0.0481 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 218 | +14.8% | -36.3 to 92.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.356 | 0.405 | +13.8% | -0.0725 to 0.171 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 12.1 to 27.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
