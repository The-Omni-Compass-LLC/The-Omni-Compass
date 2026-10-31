# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 246 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00569 to 0.0172 | GAIN |
| cache hit rate | 0.617 | 0.782 | +26.7% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.66 | -0.4% | -0.0353 to -0.0157 | GAIN |
| latency, 99th percentile (ms) | 5.74 | 5.73 | -0.1% | -0.0171 to 0.003 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 1.36 | -39.9% | -0.906 to -0.895 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.7% | 244 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,084 | 0 | -100.0% | -243,447 to -242,721 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.126 | -15.1% | -0.0619 to 0.017 | EVEN, no difference beyond the noise |
| host CPU-seconds | 250 | 213 | -14.9% | -114 to 39.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.601 | 0.404 | -32.9% | -0.369 to -0.026 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 16.9 to 19.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 307 | 271 | -11.7% | -38.7 to -33.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 34.8 | 31.4 | -9.7% | -4.39 to -2.33 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 272 | 238 | -12.5% | -35.7 to -32.3 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.5 |  | 1.32 to 1.69 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.234 | 0.225 | -4.0% | -0.0129 to -0.00554 | shown, not judged |
| host CPU-seconds without steal | 250 | 213 | -14.9% | -114 to 39.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
