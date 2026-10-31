# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `86b4d987fa63`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 1,172 | +26.8% | 247 to 248 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0591 to 0.0386 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.783 | +26.8% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 5.48 | -0.8% | -0.0621 to -0.0256 | GAIN |
| latency, 99th percentile (ms) | 5.59 | 5.58 | -0.3% | -0.0398 to 0.00436 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.16 | 1.28 | -40.8% | -0.893 to -0.87 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 314 | +389.9% | 244 to 255 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,194 | 0 | -100.0% | -243,839 to -242,549 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.111 | -10.2% | -0.0573 to 0.032 | EVEN, no difference beyond the noise |
| host CPU-seconds | 218 | 197 | -9.8% | -112 to 68.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.524 | 0.373 | -28.9% | -0.338 to 0.0353 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 15.8 to 21.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 219 | 195 | -10.9% | -30.6 to -17.2 | GAIN |
| the server's own CPU-seconds (redis-server) | 25.4 | 22.6 | -11.0% | -3.26 to -2.33 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 193 | 171 | -11.6% | -29 to -15.8 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.3 |  | 1.1 to 1.5 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.173 | 0.169 | -2.3% | -0.00802 to 8.18e-05 | shown, not judged |
| host CPU-seconds without steal | 218 | 197 | -9.8% | -112 to 68.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
