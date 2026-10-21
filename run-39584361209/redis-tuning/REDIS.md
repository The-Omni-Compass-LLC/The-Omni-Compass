# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.8% | 5.71 to 14.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00517 to 0.0114 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.00405 to 0.00925 | GAIN |
| latency, 95th percentile (ms) | 5.72 | 5.72 | +0.0% | -0.00341 to 0.00354 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.79 | +0.1% | -0.0018 to 0.0149 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.31 | -2.6% | -0.0529 to -0.0163 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | 0.129 to 2.3 | power given |
| memory used, mean (MB) | 61.2 | 62.1 | +1.6% | 0.274 to 1.63 | power given |
| keys evicted | 138,124 | 134,463 | -2.7% | -5,404 to -1,919 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.134 | +13.0% | -0.0388 to 0.0696 | EVEN, no difference beyond the noise |
| host CPU-seconds | 198 | 228 | +15.1% | -73.9 to 134 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.372 | 0.425 | +14.1% | -0.142 to 0.247 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 12.6 to 24.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
