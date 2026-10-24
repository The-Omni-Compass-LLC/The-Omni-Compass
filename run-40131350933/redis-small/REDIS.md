# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.3% | 9.71 to 14 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0169 to 0.00441 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00661 to 0.00922 | GAIN |
| latency, 95th percentile (ms) | 5.19 | 5.19 | -0.0% | -0.000333 to 0.000291 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.00415 to 0.00682 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.03 | 1.99 | -2.0% | -0.0459 to -0.0342 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.6% | 1.01 to 2.27 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.2% | 1.29 to 1.35 | power given |
| keys evicted | 243,081 | 235,639 | -3.1% | -11,278 to -3,607 | shown, not judged |
| host CPU busy (share of the run) | 0.0485 | 0.0515 | +6.1% | -0.00849 to 0.0144 | EVEN, no difference beyond the noise |
| host CPU-seconds | 85.1 | 90.6 | +6.5% | -15.9 to 27 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.204 | 0.215 | +5.2% | -0.039 to 0.0602 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15 |  | 10 to 20 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
