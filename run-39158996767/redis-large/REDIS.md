# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% | 11 to 29.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000191 to 0.00152 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.6% | 0.00732 to 0.0202 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.73 | -0.1% | -0.0138 to 0.00217 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.0% | -0.00907 to 0.00969 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.975 | -7.0% | -0.11 to -0.036 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | 0.0994 to 2.27 | power given |
| memory used, mean (MB) | 61.3 | 62.2 | +1.4% | 0.304 to 1.41 | power given |
| keys evicted | 103,524 | 94,462 | -8.8% | -13,391 to -4,734 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.117 | -1.5% | -0.0219 to 0.0183 | EVEN, no difference beyond the noise |
| host CPU-seconds | 199 | 196 | -1.6% | -42.3 to 36.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.35 | 0.339 | -3.1% | -0.0767 to 0.0549 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.7 |  | 16.9 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
