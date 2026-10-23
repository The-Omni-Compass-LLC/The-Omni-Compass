# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -1.98 to -0.158 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0198 to 0.0221 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00109 to 1.7e-05 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.78 | 5.78 | +0.0% | -0.00796 to 0.00929 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.85 | 5.87 | +0.3% | 0.0146 to 0.0217 | LOSS |
| latency, mean (ms) | 1.76 | 1.77 | +0.6% | -0.00517 to 0.0247 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.4 | -4.1% | -4.73 to -0.451 | GAIN |
| memory used, mean (MB) | 57.2 | 55.5 | -3.0% | -3.92 to 0.519 | EVEN, no difference beyond the noise |
| keys evicted | 71,738 | 71,900 | +0.2% | 8 to 315 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.152 | +15.0% | -0.00233 to 0.042 | EVEN, no difference beyond the noise |
| host CPU-seconds | 86.4 | 102 | +17.5% | -1.66 to 31.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.446 | 0.525 | +17.6% | -0.0082 to 0.165 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 8.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
