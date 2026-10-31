# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,465 | +15.6% | 196 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00389 to -0.00123 | LOSS |
| cache hit rate | 0.845 | 0.977 | +15.6% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 0.23 | -96.0% | -5.51 to -5.5 | GAIN |
| latency, 99th percentile (ms) | 5.79 | 5.73 | -1.2% | -0.0752 to -0.06 | GAIN |
| latency, mean (ms) | 1.04 | 0.305 | -70.6% | -0.739 to -0.729 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 337 | +426.6% | 270 to 276 | power given |
| memory used, mean (MB) | 61.3 | 313 | +410.1% | 247 to 256 | power given |
| keys evicted | 103,151 | 2,707 | -97.4% | -101,409 to -99,480 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.121 | -0.1% | -0.036 to 0.0358 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 209 | +2.7% | -62.4 to 73.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.356 | 0.317 | -11.2% | -0.158 to 0.0787 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29.3 |  | 27.9 to 30.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 277 | 241 | -12.9% | -36.9 to -34.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.6 | 31.9 | -10.2% | -5.41 to -1.86 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 241 | 208 | -13.9% | -35.3 to -31.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.4 |  | 1.17 to 1.63 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.227 | 0.214 | -5.9% | -0.0208 to -0.00609 | shown, not judged |
| host CPU-seconds without steal | 203 | 209 | +2.7% | -62.4 to 73.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
