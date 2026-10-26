# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `babd7a2ceac0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.2% | 10.5 to 17.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.016 to 0.0029 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.799 | +1.2% | 0.00866 to 0.0105 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.0% | -0.0106 to 0.00992 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.29 | +0.2% | -0.0224 to 0.0419 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.13 | -3.8% | -0.0669 to -0.0219 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 66.1 | +3.2% | 1.23 to 2.9 | power given |
| memory used, mean (MB) | 61.2 | 62.7 | +2.4% | 0.826 to 2.16 | power given |
| keys evicted | 138,258 | 132,610 | -4.1% | -6,275 to -5,020 | shown, not judged |
| host CPU busy (share of the run) | 0.0606 | 0.0636 | +4.9% | -0.0346 to 0.0405 | EVEN, no difference beyond the noise |
| host CPU-seconds | 107 | 112 | +5.0% | -64.6 to 75.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.201 | 0.208 | +3.7% | -0.124 to 0.139 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 122 | 124 | +1.4% | -4.27 to 7.59 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 17.1 | 17.2 | +0.5% | -0.33 to 0.503 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 105 | 106 | +1.0% | -4.84 to 6.87 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.563 |  | 0.433 to 0.694 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.126 | 0.123 | -2.7% | -0.0205 to 0.0137 | shown, not judged |
| host CPU-seconds without steal | 107 | 112 | +5.0% | -64.6 to 75.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
