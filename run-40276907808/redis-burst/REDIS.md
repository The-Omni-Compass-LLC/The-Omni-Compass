# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -0.805 to 0.345 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0264 to -0.000113 | LOSS |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.000413 to 5.46e-05 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.56 | 5.56 | +0.0% | -0.00912 to 0.0103 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.61 | +0.1% | -0.014 to 0.022 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.62 | 1.63 | +0.2% | -0.0111 to 0.0171 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.4% | -1.99 to -1.11 | GAIN |
| memory used, mean (MB) | 57.1 | 56.6 | -1.0% | -0.988 to -0.107 | GAIN |
| keys evicted | 71,696 | 72,349 | +0.9% | 640 to 665 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.0959 | -10.7% | -0.0733 to 0.0503 | EVEN, no difference beyond the noise |
| host CPU-seconds | 75.3 | 66.3 | -12.0% | -57.1 to 39.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.389 | 0.342 | -12.0% | -0.295 to 0.202 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 81.7 | 82 | +0.4% | -2 to 2.58 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 10.3 | 10.4 | +0.6% | -0.406 to 0.54 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 71.4 | 71.3 | -0.1% | -2.15 to 1.99 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.301 |  | 0.274 to 0.328 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0658 | 0.0656 | -0.3% | -0.000658 to 0.000296 | shown, not judged |
| host CPU-seconds without steal | 75.3 | 66.3 | -12.0% | -57.1 to 39.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
