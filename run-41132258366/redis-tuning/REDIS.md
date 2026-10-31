# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 198 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00334 to 0.00534 | EVEN, the same |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.139 | GAIN |
| latency, 95th percentile (ms) | 5.71 | 5.59 | -2.1% | -0.209 to -0.0323 | GAIN |
| latency, 99th percentile (ms) | 5.78 | 5.72 | -1.0% | -0.111 to -0.00866 | GAIN |
| latency, mean (ms) | 1.31 | 0.551 | -58.0% | -0.791 to -0.73 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +445.3% | 276 to 294 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,259 | 2,716 | -98.0% | -137,820 to -133,265 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.104 | -25.0% | -0.0664 to -0.00315 | GAIN |
| host CPU-seconds | 247 | 184 | -25.5% | -128 to 1.74 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.464 | 0.295 | -36.4% | -0.268 to -0.0698 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 14.8 to 20.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 237 | 195 | -18.1% | -67.3 to -18.4 | GAIN |
| the server's own CPU-seconds (redis-server) | 25.4 | 21.1 | -16.9% | -5.84 to -2.78 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 212 | 172 | -18.8% | -62.8 to -16.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.31 |  | 1.2 to 1.43 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.223 | 0.208 | -6.7% | -0.0285 to -0.00134 | shown, not judged |
| host CPU-seconds without steal | 247 | 184 | -25.5% | -128 to 1.74 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
