# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 198 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0059 to -0.00283 | LOSS |
| cache hit rate | 0.789 | 0.925 | +17.1% | 0.132 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.62 | 5.5 | -2.1% | -0.138 to -0.102 | GAIN |
| latency, 99th percentile (ms) | 5.69 | 5.66 | -0.5% | -0.0411 to -0.0145 | GAIN |
| latency, mean (ms) | 1.28 | 0.543 | -57.5% | -0.755 to -0.713 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 349 | +445.4% | 278 to 292 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 138,095 | 2,690 | -98.1% | -137,751 to -133,059 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.101 | -10.3% | -0.0747 to 0.0515 | EVEN, no difference beyond the noise |
| host CPU-seconds | 197 | 178 | -9.6% | -142 to 104 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.371 | 0.286 | -22.8% | -0.289 to 0.121 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 211 | 187 | -11.3% | -29.4 to -18.3 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.9 | 22 | -11.8% | -3.46 to -2.41 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 186 | 163 | -12.0% | -27.1 to -17.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.27 |  | 1.15 to 1.38 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.191 | 0.189 | -1.5% | -0.00848 to 0.0029 | shown, not judged |
| host CPU-seconds without steal | 197 | 178 | -9.6% | -142 to 104 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
