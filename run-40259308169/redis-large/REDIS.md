# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,282 | +1.2% | 1.61 to 28.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00887 to 0.00166 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.855 | +1.2% | 0.00103 to 0.0192 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.0% | -0.0155 to 0.0116 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.0% | -0.00277 to 0.00464 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.998 | -5.0% | -0.104 to -0.00161 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.5% | -0.49 to 2.47 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62 | +1.1% | -0.202 to 1.58 | EVEN, no difference beyond the noise |
| keys evicted | 103,497 | 96,906 | -6.4% | -12,722 to -461 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.102 | -10.7% | -0.0464 to 0.022 | EVEN, no difference beyond the noise |
| host CPU-seconds | 191 | 168 | -11.7% | -84.8 to 40.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.334 | 0.292 | -12.7% | -0.151 to 0.0657 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.3 |  | 13.1 to 25.6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 278 | 276 | -0.5% | -4.88 to 2.28 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 36.8 | 36.6 | -0.5% | -1.81 to 1.47 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 241 | 238 | -0.8% | -5.68 to 1.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.918 |  | 0.865 to 0.97 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.231 | 0.226 | -2.0% | -0.01 to 0.000673 | shown, not judged |
| host CPU-seconds without steal | 191 | 168 | -11.7% | -84.8 to 40.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 18.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
