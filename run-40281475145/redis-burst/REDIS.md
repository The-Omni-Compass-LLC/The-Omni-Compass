# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -2.18 to 0.395 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0769 to 0.072 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00143 to 0.000303 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.7 | 5.7 | +0.1% | -0.00292 to 0.00931 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.77 | +0.1% | -0.000328 to 0.0176 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.69 | 1.69 | +0.5% | 0.00159 to 0.016 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.1 | -2.9% | -3.38 to -0.364 | GAIN |
| memory used, mean (MB) | 57.1 | 56.2 | -1.6% | -2.53 to 0.705 | EVEN, no difference beyond the noise |
| keys evicted | 71,651 | 72,208 | +0.8% | -357 to 1,471 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.119 | -14.8% | -0.0698 to 0.0285 | EVEN, no difference beyond the noise |
| host CPU-seconds | 100 | 83.1 | -16.9% | -56.5 to 22.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.516 | 0.429 | -16.9% | -0.291 to 0.117 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 93.7 | 94.5 | +0.8% | -1.37 to 2.91 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 10.2 | 10.4 | +1.5% | -0.463 to 0.77 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 83.4 | 83.7 | +0.4% | -1.3 to 1.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.312 |  | 0.297 to 0.328 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0839 | 0.0843 | +0.5% | -0.000862 to 0.00173 | shown, not judged |
| host CPU-seconds without steal | 100 | 83.1 | -16.9% | -56.5 to 22.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
