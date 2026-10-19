# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,286 | +1.5% | 12.7 to 24.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00238 to 0.00337 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.5% | 0.00845 to 0.0168 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.51 | -0.2% | -0.0178 to -0.00464 | GAIN |
| latency, 99th percentile (ms) | 5.62 | 5.62 | -0.0% | -0.0132 to 0.0123 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.964 | 0.897 | -6.9% | -0.0848 to -0.0485 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.7 | +1.1% | -0.493 to 1.88 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.6 | +0.5% | -0.695 to 1.34 | EVEN, no difference beyond the noise |
| keys evicted | 103,361 | 94,999 | -8.1% | -11,355 to -5,369 | shown, not judged |
| host CPU busy (share of the run) | 0.0999 | 0.107 | +6.9% | -0.00883 to 0.0227 | EVEN, no difference beyond the noise |
| host CPU-seconds | 175 | 188 | +7.9% | -16.1 to 43.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.306 | 0.325 | +6.3% | -0.0316 to 0.0703 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 18.7 to 27.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
