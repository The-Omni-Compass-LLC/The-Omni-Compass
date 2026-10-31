# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `86b4d987fa63`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 196 to 209 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0106 to 0.00482 | EVEN, no difference beyond the noise |
| cache hit rate | 0.79 | 0.925 | +17.2% | 0.131 to 0.14 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.7 | -1.0% | -0.0609 to -0.0543 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.78 | -0.5% | -0.0349 to -0.022 | GAIN |
| latency, mean (ms) | 1.35 | 0.592 | -56.0% | -0.78 to -0.728 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 351 | +447.8% | 274 to 299 | power given |
| memory used, mean (MB) | 61.2 | 320 | +423.5% | 244 to 274 | power given |
| keys evicted | 138,057 | 2,381 | -98.3% | -138,723 to -132,630 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.123 | -8.8% | -0.0325 to 0.00868 | EVEN, no difference beyond the noise |
| host CPU-seconds | 227 | 211 | -7.4% | -57 to 23.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.427 | 0.337 | -20.9% | -0.156 to -0.0219 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 291 | 255 | -12.6% | -38.8 to -34.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.2 | 31.9 | -9.5% | -4.73 to -1.95 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 256 | 221 | -13.7% | -37.6 to -32.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.62 |  | 1.39 to 1.84 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.234 | 0.222 | -5.3% | -0.019 to -0.00576 | shown, not judged |
| host CPU-seconds without steal | 227 | 211 | -7.4% | -57 to 23.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
