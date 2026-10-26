# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,281 | +1.2% | -1.07 to 30.6 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00686 to 0.00328 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.855 | +1.2% | -0.000815 to 0.0209 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.1% | -0.00671 to 0.000106 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.82 | +0.0% | -0.0151 to 0.0202 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 1.01 | -4.9% | -0.106 to 0.00133 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.3 | +0.5% | -2.42 to 3.01 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.2 | -0.2% | -2.84 to 2.57 | EVEN, no difference beyond the noise |
| keys evicted | 103,370 | 96,908 | -6.3% | -13,804 to 882 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.115 | -7.8% | -0.0399 to 0.0204 | EVEN, no difference beyond the noise |
| host CPU-seconds | 210 | 192 | -8.7% | -75.5 to 38.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.369 | 0.333 | -9.8% | -0.132 to 0.0602 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 24 |  | 10.2 to 37.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 284 | 283 | -0.5% | -4.72 to 1.83 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 37.8 | 37.2 | -1.4% | -1.71 to 0.631 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 246 | 244 | -0.8% | -5.02 to 1.29 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.957 |  | 0.923 to 0.991 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.236 | 0.234 | -0.7% | -0.00686 to 0.00373 | shown, not judged |
| host CPU-seconds without steal | 210 | 192 | -8.7% | -75.5 to 38.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
