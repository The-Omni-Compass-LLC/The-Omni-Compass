# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -2.72 to 1.35 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.158 to 0.0817 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00197 to 0.0015 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.76 | +0.0% | -0.00799 to 0.00872 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.83 | +0.2% | -0.00385 to 0.028 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.76 | +0.5% | 0.00409 to 0.0123 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.3 | -2.6% | -1.86 to -1.53 | GAIN |
| memory used, mean (MB) | 57.2 | 56.5 | -1.2% | -0.854 to -0.526 | GAIN |
| keys evicted | 71,738 | 72,379 | +0.9% | 209 to 1,073 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.135 | -5.9% | -0.053 to 0.0362 | EVEN, no difference beyond the noise |
| host CPU-seconds | 96.3 | 90 | -6.5% | -39.9 to 27.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.497 | 0.465 | -6.5% | -0.207 to 0.142 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 123 | 123 | +0.1% | -1.95 to 2.17 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 15.4 | 15.3 | -0.8% | -0.544 to 0.311 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 108 | 108 | -0.2% | -1.76 to 1.43 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.394 |  | 0.356 to 0.431 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0957 | 0.0947 | -1.1% | -0.00707 to 0.00498 | shown, not judged |
| host CPU-seconds without steal | 96.3 | 90 | -6.5% | -39.9 to 27.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
