# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,192 | +0.7% | 0.95 to 15.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0113 to 0.00291 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.795 | +0.7% | 0.00102 to 0.00971 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.0194 to 0.00987 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.81 | +0.0% | -0.0259 to 0.0302 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.32 | -2.2% | -0.0692 to 0.00985 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | 0.532 to 1.32 | power given |
| memory used, mean (MB) | 61.2 | 61.9 | +1.2% | 0.463 to 0.992 | power given |
| keys evicted | 138,192 | 135,396 | -2.0% | -5,723 to 131 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.116 | -7.1% | -0.0427 to 0.0248 | EVEN, no difference beyond the noise |
| host CPU-seconds | 209 | 192 | -7.9% | -79.6 to 46.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.392 | 0.359 | -8.6% | -0.154 to 0.0867 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 16.3 |  | 8.74 to 23.9 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 291 | 288 | -0.9% | -8.32 to 3.16 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 35.6 | 35.8 | +0.5% | -0.0359 to 0.363 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 255 | 251 | -1.4% | -9.23 to 1.88 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.935 |  | 0.877 to 0.994 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.235 | 0.231 | -1.7% | -0.0176 to 0.00966 | shown, not judged |
| host CPU-seconds without steal | 209 | 192 | -7.9% | -79.6 to 46.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
