# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 9.93 to 13.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00917 to 0.0153 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00662 to 0.00907 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.00206 to 0.00674 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | 0.00578 to 0.0157 | LOSS |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% | -0.0457 to -0.0328 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.36 to 1.45 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.799 to 1.51 | power given |
| keys evicted | 243,110 | 236,807 | -2.6% | -14,737 to 2,131 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.153 | +9.7% | -0.00422 to 0.0313 | EVEN, no difference beyond the noise |
| host CPU-seconds | 233 | 260 | +11.4% | -8.46 to 61.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.559 | 0.615 | +10.1% | -0.0283 to 0.141 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14 |  | 9.7 to 18.3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 310 | 311 | +0.3% | -1.05 to 3.02 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 35.6 | 35.5 | -0.3% | -1.17 to 0.991 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 274 | 274 | +0.1% | -3.04 to 3.34 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.924 |  | 0.818 to 1.03 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.233 | 0.231 | -1.0% | -0.0106 to 0.00601 | shown, not judged |
| host CPU-seconds without steal | 233 | 260 | +11.4% | -8.46 to 61.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
