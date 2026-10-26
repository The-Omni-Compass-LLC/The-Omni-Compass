# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,191 | +0.6% | -1.62 to 16 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0034 to 0.00417 | EVEN, the same |
| cache hit rate | 0.79 | 0.794 | +0.6% | -0.000974 to 0.0106 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.1% | -0.0121 to 0.0181 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.2% | -0.0106 to 0.0283 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.32 | -1.6% | -0.0624 to 0.0199 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.5% | -0.382 to 2.33 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 61.9 | +1.1% | -0.308 to 1.67 | EVEN, no difference beyond the noise |
| keys evicted | 138,050 | 135,880 | -1.6% | -6,734 to 2,395 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.134 | +27.5% | -0.0405 to 0.0984 | EVEN, no difference beyond the noise |
| host CPU-seconds | 173 | 228 | +31.7% | -76.5 to 186 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.325 | 0.425 | +30.9% | -0.148 to 0.349 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 6.41 to 30.9 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 283 | 286 | +1.1% | -3.9 to 10 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 34.6 | 35.1 | +1.3% | -0.681 to 1.59 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 248 | 250 | +0.7% | -4.23 to 7.58 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.929 |  | 0.881 to 0.977 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.231 | 0.229 | -0.6% | -0.00635 to 0.00346 | shown, not judged |
| host CPU-seconds without steal | 173 | 228 | +31.7% | -76.5 to 186 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
