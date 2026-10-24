# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,074 | 1,075 | +0.1% | -0.61 to 2.49 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0119 to 0.00336 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.000823 to 0.000756 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.1% | -0.0128 to 0.00372 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.24 | 5.25 | +0.1% | -0.0361 to 0.0457 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.53 | 1.54 | +0.1% | -0.0148 to 0.0169 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.7 | -2.0% | -2.19 to -0.385 | GAIN |
| memory used, mean (MB) | 57.1 | 56.6 | -1.0% | -0.792 to -0.343 | GAIN |
| keys evicted | 71,719 | 71,742 | +0.0% | -230 to 277 | shown, not judged |
| host CPU busy (share of the run) | 0.0571 | 0.0636 | +11.4% | -0.133 to 0.146 | EVEN, no difference beyond the noise |
| host CPU-seconds | 40.5 | 45.6 | +12.6% | -99.5 to 110 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.209 | 0.236 | +12.5% | -0.515 to 0.568 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
