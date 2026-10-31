# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 195 to 211 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.045 to -0.0121 | LOSS |
| cache hit rate | 0.789 | 0.925 | +17.2% | 0.13 to 0.141 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.69 | -0.9% | -0.0552 to -0.0497 | GAIN |
| latency, 99th percentile (ms) | 5.79 | 5.77 | -0.3% | -0.0252 to -0.0142 | GAIN |
| latency, mean (ms) | 1.34 | 0.587 | -56.3% | -0.783 to -0.728 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 351 | +447.9% | 273 to 300 | power given |
| memory used, mean (MB) | 61.2 | 321 | +423.8% | 244 to 275 | power given |
| keys evicted | 138,148 | 2,380 | -98.3% | -139,407 to -132,128 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.134 | -15.4% | -0.055 to 0.00627 | EVEN, no difference beyond the noise |
| host CPU-seconds | 273 | 232 | -15.1% | -104 to 21 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.513 | 0.372 | -27.5% | -0.25 to -0.0323 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 16.2 to 19.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 290 | 250 | -14.1% | -43 to -38.7 | GAIN |
| the server's own CPU-seconds (redis-server) | 34.8 | 30.4 | -12.7% | -5.37 to -3.46 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 255 | 217 | -14.9% | -40.5 to -35.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.62 |  | 1.4 to 1.83 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.252 | 0.241 | -4.2% | -0.015 to -0.0062 | shown, not judged |
| host CPU-seconds without steal | 273 | 232 | -15.1% | -104 to 21 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 12.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
