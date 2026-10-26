# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | -0.0% | -0.0438 to 0.00989 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.027 to 0.0405 | EVEN, no difference beyond the noise |
| cache hit rate | 0.782 | 0.782 | +0.0% | -5.13e-06 to 6.12e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.66 | 5.66 | -0.0% | -0.0325 to 0.0272 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.73 | -0.1% | -0.0348 to 0.0269 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.36 | -0.1% | -0.014 to 0.012 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.0265 to 0.0419 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.104 | -15.6% | -0.0869 to 0.0484 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 172 | -16.9% | -159 to 89 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.393 | 0.327 | -16.9% | -0.301 to 0.168 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 276 | 272 | -1.5% | -16.3 to 7.76 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 32.6 | 32 | -1.9% | -3.66 to 2.41 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 243 | 240 | -1.5% | -12.7 to 5.41 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.236 | 0.23 | -2.4% | -0.0108 to -0.000421 | shown, not judged |
| host CPU-seconds without steal | 208 | 172 | -16.9% | -159 to 89 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
