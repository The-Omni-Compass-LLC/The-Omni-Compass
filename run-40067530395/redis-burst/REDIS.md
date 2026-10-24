# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | -0.0% | -0.916 to 0.103 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00677 to 0.00847 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00103 to 0.000326 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.57 | 5.57 | -0.0% | -0.00859 to 0.00425 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.62 | 5.62 | -0.0% | -0.00829 to 0.00758 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.64 | 1.64 | -0.1% | -0.0113 to 0.00929 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.9 | -3.3% | -3.95 to -0.316 | GAIN |
| memory used, mean (MB) | 57.1 | 55.9 | -2.1% | -3.01 to 0.589 | EVEN, no difference beyond the noise |
| keys evicted | 71,742 | 71,850 | +0.2% | -77.3 to 293 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.109 | -1.8% | -0.0314 to 0.0274 | EVEN, no difference beyond the noise |
| host CPU-seconds | 78.1 | 76.4 | -2.2% | -25.1 to 21.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.403 | 0.395 | -2.2% | -0.129 to 0.112 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
