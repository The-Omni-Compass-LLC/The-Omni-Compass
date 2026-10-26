# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 936 | +1.2% | 10 to 12.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0418 to 0.0318 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00657 to 0.00851 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.7 | +0.0% | 0.000486 to 0.0031 | LOSS |
| latency, 99th percentile (ms) | 5.75 | 5.77 | +0.2% | -0.000899 to 0.0277 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.23 | -1.7% | -0.0437 to -0.0345 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.35 to 1.4 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.22 to 1.24 | power given |
| keys evicted | 243,220 | 234,998 | -3.4% | -8,858 to -7,588 | shown, not judged |
| host CPU busy (share of the run) | 0.148 | 0.145 | -2.0% | -0.0111 to 0.00519 | EVEN, no difference beyond the noise |
| host CPU-seconds | 248 | 243 | -2.2% | -21.8 to 10.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.597 | 0.576 | -3.4% | -0.0596 to 0.0192 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 12.3 |  | 9.46 to 15.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 313 | 312 | -0.3% | -2.26 to 0.442 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 35.7 | 35.3 | -1.0% | -0.721 to -0.0252 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 277 | 276 | -0.5% | -2.54 to -0.375 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.921 |  | 0.838 to 1 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.236 | 0.232 | -1.5% | -0.0134 to 0.00622 | shown, not judged |
| host CPU-seconds without steal | 248 | 243 | -2.2% | -21.8 to 10.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
