# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,045 | 1,045 | -0.0% | -2.64 to 2.36 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0446 to 0.0138 | EVEN, no difference beyond the noise |
| cache hit rate | 0.698 | 0.697 | -0.0% | -0.000729 to 0.000578 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.0076 to 0.00745 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.27 | +0.0% | -0.00144 to 0.00232 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.64 | 1.64 | -0.1% | -0.0138 to 0.00911 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.1 | -1.3% | -0.86 to -0.86 | GAIN |
| memory used, mean (MB) | 56.9 | 57 | +0.1% | 0.0369 to 0.109 | power given |
| keys evicted | 49,885 | 50,552 | +1.3% | 507 to 827 | shown, not judged |
| host CPU busy (share of the run) | 0.0551 | 0.0494 | -10.3% | -0.0357 to 0.0243 | EVEN, no difference beyond the noise |
| host CPU-seconds | 25.7 | 22.9 | -10.9% | -17.5 to 11.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.205 | 0.183 | -10.8% | -0.139 to 0.095 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 32.6 | 32.6 | +0.1% | -0.663 to 0.703 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 4.72 | 4.73 | +0.1% | -0.105 to 0.119 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 27.9 | 27.7 | -0.5% | -0.91 to 0.619 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.16 |  | 0.141 to 0.179 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0313 | 0.03 | -4.0% | -0.00534 to 0.00283 | shown, not judged |
| host CPU-seconds without steal | 25.7 | 22.9 | -10.9% | -17.5 to 11.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
