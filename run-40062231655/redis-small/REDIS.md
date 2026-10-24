# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 10.8 to 13.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.028 to 0.00878 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.626 | +1.3% | 0.00725 to 0.00911 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.0% | -0.0143 to 0.0101 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.73 | +0.0% | -0.00769 to 0.0104 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.21 | -2.0% | -0.0549 to -0.0353 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 0.919 to 2.29 | power given |
| memory used, mean (MB) | 60.7 | 61.8 | +1.7% | 0.654 to 1.45 | power given |
| keys evicted | 243,128 | 238,495 | -1.9% | -12,738 to 3,472 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.128 | -6.0% | -0.041 to 0.0247 | EVEN, no difference beyond the noise |
| host CPU-seconds | 229 | 213 | -6.8% | -80 to 48.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.548 | 0.504 | -8.0% | -0.199 to 0.111 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 16 |  | 8.55 to 23.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
