# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `babd7a2ceac0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -0.848 to 0.155 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.057 to 0.0234 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00059 to 0.000144 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.55 | 5.55 | -0.0% | -0.00981 to 0.00463 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.61 | +0.0% | -0.00505 to 0.00822 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.62 | 1.62 | +0.1% | -0.00868 to 0.0114 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.6 | -2.2% | -1.57 to -1.23 | GAIN |
| memory used, mean (MB) | 57.1 | 56.7 | -0.7% | -0.574 to -0.234 | GAIN |
| keys evicted | 71,708 | 72,371 | +0.9% | 519 to 807 | shown, not judged |
| host CPU busy (share of the run) | 0.0937 | 0.0915 | -2.3% | -0.0396 to 0.0354 | EVEN, no difference beyond the noise |
| host CPU-seconds | 64.9 | 63.5 | -2.2% | -30.4 to 27.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.335 | 0.328 | -2.1% | -0.157 to 0.142 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 79.9 | 80 | +0.1% | -0.676 to 0.859 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 10.1 | 10.2 | +0.7% | -0.00505 to 0.138 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 69.7 | 69.5 | -0.4% | -1.05 to 0.537 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.283 |  | 0.238 to 0.329 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0653 | 0.0634 | -2.9% | -0.00324 to -0.000579 | shown, not judged |
| host CPU-seconds without steal | 64.9 | 63.5 | -2.2% | -30.4 to 27.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
