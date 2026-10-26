# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `babd7a2ceac0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 935 | +1.0% | -6.44 to 24.8 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0357 to 0.049 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.623 | +1.0% | -0.00427 to 0.0166 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.0121 to 0.0176 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | -0.0146 to 0.0359 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.23 | -1.4% | -0.0769 to 0.0156 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.8% | -0.286 to 2.63 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 61.5 | +1.3% | -0.203 to 1.84 | EVEN, no difference beyond the noise |
| keys evicted | 243,212 | 241,242 | -0.8% | -4,437 to 496 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.148 | +1.0% | -0.0256 to 0.0286 | EVEN, no difference beyond the noise |
| host CPU-seconds | 247 | 250 | +1.2% | -52.7 to 58.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.592 | 0.593 | +0.3% | -0.141 to 0.144 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15.3 |  | 12.5 to 18.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 309 | 310 | +0.3% | -7.52 to 9.25 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 35.2 | 35.7 | +1.2% | -0.978 to 1.84 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 273 | 273 | -0.2% | -7.49 to 6.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.943 |  | 0.899 to 0.986 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.237 | 0.233 | -1.8% | -0.0382 to 0.0297 | shown, not judged |
| host CPU-seconds without steal | 247 | 250 | +1.2% | -52.7 to 58.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
