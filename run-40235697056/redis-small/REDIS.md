# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 10.1 to 13.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00553 to 0.00684 | EVEN, the same |
| cache hit rate | 0.618 | 0.625 | +1.3% | 0.00694 to 0.00883 | GAIN |
| latency, 95th percentile (ms) | 5.49 | 5.5 | +0.0% | -0.000502 to 0.00448 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.56 | 5.57 | +0.1% | 0.00381 to 0.00664 | LOSS |
| latency, mean (ms) | 2.13 | 2.09 | -1.9% | -0.0503 to -0.0297 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 0.916 to 1.93 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 0.985 to 1.47 | power given |
| keys evicted | 243,043 | 236,704 | -2.6% | -14,909 to 2,231 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.105 | -2.4% | -0.058 to 0.0527 | EVEN, no difference beyond the noise |
| host CPU-seconds | 189 | 183 | -2.7% | -114 to 103 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.453 | 0.435 | -4.0% | -0.277 to 0.241 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14 |  | 11.5 to 16.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 204 | 205 | +0.2% | -1.4 to 2.16 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 24.6 | 24.4 | -0.6% | -0.195 to -0.119 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 179 | 179 | -0.1% | -1.84 to 1.53 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.702 |  | 0.642 to 0.761 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.163 | 0.159 | -2.1% | -0.00556 to -0.00121 | shown, not judged |
| host CPU-seconds without steal | 189 | 183 | -2.7% | -114 to 103 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
