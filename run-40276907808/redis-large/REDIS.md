# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,289 | +1.7% | 20.2 to 23.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00122 to 0.0014 | EVEN, the same |
| cache hit rate | 0.844 | 0.859 | +1.7% | 0.0135 to 0.0159 | GAIN |
| latency, 95th percentile (ms) | 5.64 | 5.63 | -0.1% | -0.0179 to 0.00391 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.1% | -0.00371 to 0.0105 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.989 | 0.912 | -7.8% | -0.0837 to -0.0709 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | -0.629 to 2.44 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.9 | +1.0% | -0.483 to 1.73 | EVEN, no difference beyond the noise |
| keys evicted | 103,689 | 94,017 | -9.3% | -10,468 to -8,877 | shown, not judged |
| host CPU busy (share of the run) | 0.0999 | 0.116 | +16.6% | -0.00562 to 0.0387 | EVEN, no difference beyond the noise |
| host CPU-seconds | 174 | 207 | +18.9% | -10.5 to 76.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.306 | 0.357 | +16.8% | -0.023 to 0.126 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 207 | 207 | -0.1% | -5.04 to 4.49 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 25.6 | 25.5 | -0.2% | -0.302 to 0.188 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 182 | 181 | -0.5% | -5.49 to 3.54 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.757 |  | 0.738 to 0.776 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.205 | 0.204 | -0.6% | -0.0117 to 0.00909 | shown, not judged |
| host CPU-seconds without steal | 174 | 207 | +18.9% | -10.5 to 76.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
