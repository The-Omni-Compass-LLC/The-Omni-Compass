# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 8.75 to 14.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.02 to 0.0085 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00591 to 0.00952 | GAIN |
| latency, 95th percentile (ms) | 5.6 | 5.6 | +0.0% | -0.0017 to 0.00433 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.67 | 5.68 | +0.1% | 0.000156 to 0.0149 | LOSS |
| latency, mean (ms) | 2.19 | 2.15 | -1.8% | -0.0487 to -0.0313 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.6% | 0.316 to 3.07 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.1 to 1.33 | power given |
| keys evicted | 243,131 | 235,562 | -3.1% | -9,832 to -5,307 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.123 | +0.9% | -0.0294 to 0.0315 | EVEN, no difference beyond the noise |
| host CPU-seconds | 215 | 217 | +1.0% | -58.8 to 63 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.517 | 0.515 | -0.3% | -0.146 to 0.143 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.3 |  | 3.99 to 24.7 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
