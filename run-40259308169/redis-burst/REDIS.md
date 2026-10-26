# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,071 | 1,072 | +0.1% | -6.34 to 8.66 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,499 | -0.1% | -4.98 to 3.09 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00151 to 0.000891 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.76 | -0.0% | -0.0155 to 0.013 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.49 | 6.13 | -5.5% | -3.42 to 2.71 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.78 | 1.79 | +0.2% | -0.0971 to 0.105 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.3 | -4.2% | -4.8 to -0.551 | GAIN |
| memory used, mean (MB) | 57.2 | 55.4 | -3.0% | -3.83 to 0.427 | EVEN, no difference beyond the noise |
| keys evicted | 71,726 | 71,966 | +0.3% | -318 to 798 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.141 | -2.1% | -0.0418 to 0.0357 | EVEN, no difference beyond the noise |
| host CPU-seconds | 96.9 | 94.5 | -2.5% | -34.1 to 29.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.503 | 0.489 | -2.6% | -0.176 to 0.15 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 126 | 126 | +0.0% | -4.92 to 4.92 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 15.4 | 15.5 | +0.8% | -0.379 to 0.626 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 110 | 110 | -0.5% | -4.98 to 3.95 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.398 |  | 0.355 to 0.442 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0984 | 0.0963 | -2.1% | -0.0142 to 0.0101 | shown, not judged |
| host CPU-seconds without steal | 96.9 | 94.5 | -2.5% | -34.1 to 29.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 8.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
