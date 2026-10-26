# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,197 | +1.2% | 12.3 to 16.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.01 to 0.00216 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.799 | +1.2% | 0.00798 to 0.0108 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 5.52 | -0.0% | -0.0161 to 0.0128 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.0% | -0.00745 to 0.0112 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.19 | -4.0% | -0.0584 to -0.0414 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.6% | 1.64 to 1.75 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +1.9% | 1.15 to 1.24 | power given |
| keys evicted | 138,297 | 132,793 | -4.0% | -6,447 to -4,561 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.102 | -1.9% | -0.017 to 0.013 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 179 | -2.1% | -32.9 to 25.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.343 | 0.332 | -3.2% | -0.0653 to 0.0432 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 23 to 23 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 192 | 192 | -0.2% | -1.46 to 0.712 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 24.3 | 24.4 | +0.1% | -0.472 to 0.505 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 168 | 167 | -0.7% | -1.62 to -0.604 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.725 |  | 0.626 to 0.824 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.166 | 0.163 | -1.9% | -0.00809 to 0.00189 | shown, not judged |
| host CPU-seconds without steal | 182 | 179 | -2.1% | -32.9 to 25.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
