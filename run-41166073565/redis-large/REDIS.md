# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,464 | +15.7% | 195 to 202 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00684 to 0.00169 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.977 | +15.7% | 0.13 to 0.135 | GAIN |
| latency, 95th percentile (ms) | 5.55 | 0.252 | -95.5% | -5.6 to -4.99 | GAIN |
| latency, 99th percentile (ms) | 5.64 | 5.52 | -2.2% | -0.128 to -0.122 | GAIN |
| latency, mean (ms) | 0.982 | 0.263 | -73.2% | -0.733 to -0.706 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.2% | 270 to 275 | power given |
| memory used, mean (MB) | 61.3 | 312 | +409.5% | 248 to 253 | power given |
| keys evicted | 103,418 | 2,756 | -97.3% | -102,123 to -99,199 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.097 | -10.0% | -0.0329 to 0.0112 | EVEN, no difference beyond the noise |
| host CPU-seconds | 188 | 170 | -9.4% | -60.8 to 25.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.33 | 0.259 | -21.7% | -0.144 to 0.000636 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 26.9 to 29.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 207 | 182 | -12.1% | -31.6 to -18.4 | GAIN |
| the server's own CPU-seconds (redis-server) | 27.7 | 24.1 | -13.0% | -4.56 to -2.63 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 179 | 156 | -12.7% | -28.1 to -17.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.25 |  | 0.848 to 1.65 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.175 | 0.171 | -2.4% | -0.0142 to 0.00586 | shown, not judged |
| host CPU-seconds without steal | 188 | 170 | -9.4% | -60.8 to 25.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
