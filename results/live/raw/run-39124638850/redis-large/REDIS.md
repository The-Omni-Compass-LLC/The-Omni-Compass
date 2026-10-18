# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,283 | +1.3% | 6.18 to 26.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00464 to 0.00433 | EVEN, the same |
| cache hit rate | 0.845 | 0.856 | +1.3% | 0.00415 to 0.018 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.0% | -0.0138 to 0.00874 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.1% | -0.00587 to 0.0183 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.997 | -5.4% | -0.0862 to -0.0267 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.6 | -0.6% | -4.71 to 3.99 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 60.5 | -1.3% | -5.03 to 3.44 | EVEN, no difference beyond the noise |
| keys evicted | 103,611 | 96,556 | -6.8% | -12,161 to -1,950 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.117 | +9.5% | -0.0276 to 0.0478 | EVEN, no difference beyond the noise |
| host CPU-seconds | 176 | 195 | +11.0% | -50.9 to 89.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.308 | 0.337 | +9.5% | -0.0898 to 0.149 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28.3 |  | 12.6 to 44.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
