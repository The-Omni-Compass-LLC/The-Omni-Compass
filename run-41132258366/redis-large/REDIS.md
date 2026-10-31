# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,465 | +15.7% | 193 to 203 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0168 to 0.00234 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.978 | +15.7% | 0.129 to 0.136 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 0.237 | -95.9% | -5.51 to -5.48 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.72 | -1.3% | -0.0939 to -0.0565 | GAIN |
| latency, mean (ms) | 1.04 | 0.306 | -70.7% | -0.763 to -0.715 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 338 | +427.5% | 270 to 277 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.9% | 248 to 256 | power given |
| keys evicted | 103,445 | 2,637 | -97.5% | -103,106 to -98,510 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.11 | -18.5% | -0.0556 to 0.00558 | EVEN, no difference beyond the noise |
| host CPU-seconds | 230 | 188 | -18.4% | -101 to 16.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.404 | 0.285 | -29.5% | -0.214 to -0.0236 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 26.9 to 29.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 278 | 241 | -13.1% | -39.8 to -32.9 | GAIN |
| the server's own CPU-seconds (redis-server) | 36.5 | 32.8 | -10.1% | -5.84 to -1.55 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 241 | 207 | -14.2% | -35.6 to -32.7 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.49 |  | 1.17 to 1.81 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.23 | 0.222 | -3.2% | -0.017 to 0.00229 | shown, not judged |
| host CPU-seconds without steal | 230 | 188 | -18.4% | -101 to 16.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
