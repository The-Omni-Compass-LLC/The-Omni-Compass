# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 831 | 837 | +0.6% | 4.97 to 5.66 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0461 to 0.0086 | EVEN, no difference beyond the noise |
| cache hit rate | 0.555 | 0.559 | +0.7% | 0.00352 to 0.00409 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.1% | -0.0087 to 0.0147 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.37 | 5.46 | +1.7% | 0.0194 to 0.165 | LOSS |
| latency, mean (ms) | 2.37 | 2.36 | -0.6% | -0.0182 to -0.0113 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.5 | +0.8% | 0.505 to 0.505 | power given |
| memory used, mean (MB) | 60.3 | 61 | +1.1% | 0.666 to 0.7 | power given |
| keys evicted | 185,099 | 180,275 | -2.6% | -4,948 to -4,699 | shown, not judged |
| host CPU busy (share of the run) | 0.063 | 0.0702 | +11.4% | -0.0316 to 0.046 | EVEN, no difference beyond the noise |
| host CPU-seconds | 73.8 | 82.5 | +11.8% | -40.3 to 57.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.296 | 0.329 | +11.1% | -0.163 to 0.229 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 87.2 | 89.3 | +2.4% | 0.514 to 3.72 | power given |
| the server's own CPU-seconds (redis-server) | 12.2 | 12.4 | +1.5% | -0.131 to 0.491 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 74.9 | 76.5 | +2.0% | 0.198 to 2.85 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.413 |  | 0.391 to 0.435 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0856 | 0.0835 | -2.5% | -0.00777 to 0.00348 | shown, not judged |
| host CPU-seconds without steal | 73.8 | 82.6 | +11.8% | -40.3 to 57.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
