# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 936 | +1.2% | 8.24 to 14.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.27 to 0.278 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00645 to 0.00888 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.1% | -0.0236 to 0.0317 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.34 | 5.39 | +1.0% | -0.116 to 0.224 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.05 | 2.02 | -1.7% | -0.0582 to -0.0112 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.13 to 1.82 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.1 to 1.4 | power given |
| keys evicted | 243,204 | 235,950 | -3.0% | -11,138 to -3,369 | shown, not judged |
| host CPU busy (share of the run) | 0.0608 | 0.0656 | +7.8% | -0.0426 to 0.0521 | EVEN, no difference beyond the noise |
| host CPU-seconds | 107 | 115 | +7.8% | -79.9 to 96.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.257 | 0.274 | +6.5% | -0.195 to 0.228 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.3 |  | 7.08 to 19.6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 128 | 132 | +2.9% | -17.1 to 24.5 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 17.4 | 17.7 | +1.7% | -2.27 to 2.86 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 110 | 113 | +2.6% | -15.3 to 20.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.599 |  | 0.455 to 0.742 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.125 | 0.127 | +1.1% | -0.0114 to 0.0142 | shown, not judged |
| host CPU-seconds without steal | 107 | 115 | +7.8% | -79.9 to 96.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
