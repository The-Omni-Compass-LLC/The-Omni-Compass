# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -1.78 to -0.528 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0317 to 0.047 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00146 to -8.48e-05 | LOSS |
| latency, 95th percentile (ms) | 5.57 | 5.57 | +0.1% | -0.00398 to 0.013 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.62 | 5.62 | +0.1% | -0.00101 to 0.0143 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.63 | 1.64 | +0.5% | -0.00675 to 0.0223 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.4% | -2.13 to -0.918 | GAIN |
| memory used, mean (MB) | 57.2 | 56.5 | -1.1% | -1.21 to -0.00782 | GAIN |
| keys evicted | 71,619 | 71,840 | +0.3% | 39.4 to 403 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.116 | +3.5% | -0.11 to 0.118 | EVEN, no difference beyond the noise |
| host CPU-seconds | 79.9 | 82.1 | +2.8% | -86.8 to 91.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.412 | 0.424 | +3.0% | -0.448 to 0.472 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
