# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `babd7a2ceac0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,285 | +1.4% | 6.92 to 29.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00972 to 0.00381 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.857 | +1.4% | 0.00458 to 0.0194 | GAIN |
| latency, 95th percentile (ms) | 5.49 | 5.48 | -0.3% | -0.0298 to 2.33e-05 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | -0.0% | -0.0144 to 0.0123 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.956 | 0.891 | -6.7% | -0.0984 to -0.0301 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.5 | +0.8% | -0.684 to 1.7 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.6 | +0.5% | -0.846 to 1.46 | EVEN, no difference beyond the noise |
| keys evicted | 103,441 | 95,579 | -7.6% | -12,839 to -2,885 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.0917 | -11.2% | -0.0256 to 0.00249 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 160 | -12.1% | -48.2 to 4.17 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.32 | 0.277 | -13.4% | -0.0864 to 0.00103 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 190 | 188 | -1.0% | -2.3 to -1.62 | GAIN |
| the server's own CPU-seconds (redis-server) | 25.9 | 25.6 | -1.1% | -0.935 to 0.388 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 164 | 161 | -1.5% | -2.72 to -2.04 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.698 |  | 0.66 to 0.735 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.164 | 0.16 | -2.8% | -0.00983 to 0.00079 | shown, not judged |
| host CPU-seconds without steal | 182 | 160 | -12.1% | -48.2 to 4.15 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
