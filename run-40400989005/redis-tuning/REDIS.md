# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,129 | 1,138 | +0.8% | 5.64 to 12.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0289 to 0.0221 | EVEN, no difference beyond the noise |
| cache hit rate | 0.754 | 0.759 | +0.8% | 0.00286 to 0.00854 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.0% | -0.00636 to 0.00562 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.28 | +0.2% | -0.109 to 0.124 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.32 | -2.6% | -0.0471 to -0.0248 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.0% | 0.196 to 2.38 | power given |
| memory used, mean (MB) | 61.1 | 62.1 | +1.6% | 0.267 to 1.7 | power given |
| keys evicted | 106,840 | 104,006 | -2.7% | -5,273 to -396 | shown, not judged |
| host CPU busy (share of the run) | 0.0736 | 0.0674 | -8.4% | -0.0438 to 0.0314 | EVEN, no difference beyond the noise |
| host CPU-seconds | 87.7 | 79.6 | -9.2% | -55.7 to 39.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.259 | 0.233 | -9.9% | -0.166 to 0.114 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.7 |  | 11.8 to 17.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 82.2 | 82.2 | -0.0% | -4.14 to 4.12 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 11.7 | 11.6 | -1.0% | -0.812 to 0.572 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 70.4 | 70.1 | -0.4% | -3.66 to 3.15 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.372 |  | 0.292 to 0.452 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0808 | 0.0755 | -6.6% | -0.0124 to 0.0018 | shown, not judged |
| host CPU-seconds without steal | 87.7 | 79.6 | -9.2% | -55.7 to 39.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
