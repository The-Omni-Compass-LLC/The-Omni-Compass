# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,195 | +1.0% | 5.43 to 17.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0168 to 0.0194 | EVEN, the same |
| cache hit rate | 0.79 | 0.797 | +1.0% | 0.00296 to 0.0121 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.0368 to 0.02 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.81 | -0.1% | -0.0423 to 0.0339 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.31 | -3.1% | -0.0687 to -0.0164 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | -0.519 to 2.93 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.2 | +1.7% | -0.308 to 2.35 | EVEN, no difference beyond the noise |
| keys evicted | 138,031 | 133,777 | -3.1% | -7,357 to -1,151 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.124 | -0.1% | -0.0269 to 0.0266 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 207 | +0.4% | -52.3 to 53.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.388 | 0.385 | -0.6% | -0.0999 to 0.0954 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 10.7 to 25.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
