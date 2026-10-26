# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.1% | 5.84 to 20.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.02 to 0.0196 | EVEN, the same |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.00482 to 0.0122 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.0% | -0.0394 to 0.0353 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.27 | -0.1% | -0.0923 to 0.0819 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.13 | -3.9% | -0.0692 to -0.0233 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.6% | 0.981 to 2.36 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +1.9% | 0.532 to 1.83 | power given |
| keys evicted | 138,152 | 133,247 | -3.6% | -7,387 to -2,423 | shown, not judged |
| host CPU busy (share of the run) | 0.064 | 0.0581 | -9.2% | -0.024 to 0.0123 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 102 | -9.8% | -45 to 22.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.213 | 0.19 | -10.8% | -0.0873 to 0.0412 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 124 | 123 | -0.6% | -14.8 to 13.2 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 17.3 | 17.2 | -0.6% | -2.73 to 2.53 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 107 | 105 | -1.2% | -12.6 to 10.1 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.576 |  | 0.51 to 0.641 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.128 | 0.124 | -3.1% | -0.0261 to 0.0182 | shown, not judged |
| host CPU-seconds without steal | 113 | 102 | -9.8% | -45 to 22.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
