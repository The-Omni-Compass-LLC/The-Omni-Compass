# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,282 | +1.2% | 0.236 to 30.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0145 to 0.00996 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.855 | +1.2% | 0.00028 to 0.0205 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.75 | -0.1% | -0.0224 to 0.00952 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.83 | 5.83 | +0.0% | -0.0257 to 0.0292 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 1.01 | -5.1% | -0.103 to -0.00595 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | -0.622 to 2.4 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.7 | +0.7% | -0.179 to 1.05 | EVEN, no difference beyond the noise |
| keys evicted | 103,556 | 96,760 | -6.6% | -13,603 to 11.4 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.118 | -5.2% | -0.0413 to 0.0283 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 196 | -5.7% | -78.6 to 54.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.364 | 0.339 | -6.9% | -0.14 to 0.0898 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 12.4 to 29.6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 288 | 287 | -0.4% | -7.43 to 5.03 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 38.4 | 38.3 | -0.1% | -1.94 to 1.84 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 249 | 247 | -0.9% | -6.8 to 2.53 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.986 |  | 0.916 to 1.06 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.242 | 0.237 | -1.9% | -0.0176 to 0.00833 | shown, not judged |
| host CPU-seconds without steal | 208 | 196 | -5.7% | -78.6 to 54.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
