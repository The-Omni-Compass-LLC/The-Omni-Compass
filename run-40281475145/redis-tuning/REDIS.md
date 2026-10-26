# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.9% | 3.37 to 17.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.01 to 0.00478 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.796 | +0.9% | 0.00241 to 0.0117 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.0% | -0.0116 to 0.00858 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.00947 to 0.0144 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.32 | 1.28 | -2.7% | -0.0561 to -0.0162 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.7% | 0.0123 to 2.22 | power given |
| memory used, mean (MB) | 61.2 | 62 | +1.3% | -0.34 to 1.97 | EVEN, no difference beyond the noise |
| keys evicted | 138,177 | 134,521 | -2.6% | -7,131 to -181 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.136 | -2.8% | -0.0206 to 0.0128 | EVEN, no difference beyond the noise |
| host CPU-seconds | 244 | 236 | -3.1% | -41 to 25.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.457 | 0.439 | -4.0% | -0.0785 to 0.0419 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20 |  | 11 to 29 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 258 | 257 | -0.3% | -3.64 to 2.17 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 31.5 | 31.5 | -0.2% | -1.78 to 1.63 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 226 | 225 | -0.7% | -3.05 to -0.0518 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.897 |  | 0.839 to 0.954 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.218 | 0.215 | -1.3% | -0.00561 to -2.46e-05 | shown, not judged |
| host CPU-seconds without steal | 244 | 236 | -3.1% | -41 to 25.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
