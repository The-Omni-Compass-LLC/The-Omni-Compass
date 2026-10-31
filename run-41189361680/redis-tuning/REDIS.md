# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 197 to 208 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0346 to 0.00381 | EVEN, no difference beyond the noise |
| cache hit rate | 0.79 | 0.925 | +17.2% | 0.131 to 0.139 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.7 | -1.1% | -0.0747 to -0.0527 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.79 | -0.5% | -0.0475 to -0.0158 | GAIN |
| latency, mean (ms) | 1.35 | 0.593 | -56.1% | -0.774 to -0.741 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 350 | +446.5% | 271 to 301 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.5% | 244 to 274 | power given |
| keys evicted | 138,037 | 2,397 | -98.3% | -138,356 to -132,925 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.115 | -21.8% | -0.0919 to 0.0277 | EVEN, no difference beyond the noise |
| host CPU-seconds | 250 | 194 | -22.3% | -171 to 59.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.469 | 0.311 | -33.6% | -0.36 to 0.044 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 16.2 to 19.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 296 | 257 | -13.2% | -44.3 to -33.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.4 | 31.8 | -12.6% | -6.71 to -2.43 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 259 | 223 | -14.0% | -39.3 to -33.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.74 |  | 1.3 to 2.19 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.241 | 0.229 | -4.9% | -0.0275 to 0.00371 | shown, not judged |
| host CPU-seconds without steal | 250 | 194 | -22.3% | -171 to 59.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
