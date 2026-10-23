# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -1.88 to 0.443 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00651 to 0.00381 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00123 to 0.000443 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.1% | -0.0184 to 0.0108 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.1% | -0.0158 to 0.0241 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.74 | +0.5% | -0.00577 to 0.0226 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.9 | -3.2% | -4.3 to 0.177 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 57.2 | 56 | -1.9% | -3.4 to 1.19 | EVEN, no difference beyond the noise |
| keys evicted | 71,747 | 71,875 | +0.2% | -93.1 to 349 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.135 | -3.0% | -0.0535 to 0.045 | EVEN, no difference beyond the noise |
| host CPU-seconds | 94.4 | 90.8 | -3.8% | -41.8 to 34.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.488 | 0.469 | -3.8% | -0.216 to 0.179 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
