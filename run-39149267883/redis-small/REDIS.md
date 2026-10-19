# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 10.6 to 13.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0556 to 0.0357 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00673 to 0.00921 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.1% | -0.0314 to 0.0227 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.74 | +0.1% | -0.0306 to 0.0364 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.21 | -2.0% | -0.0654 to -0.0255 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 0.978 to 1.78 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.867 to 1.46 | power given |
| keys evicted | 243,123 | 236,726 | -2.6% | -14,894 to 2,100 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.136 | -2.6% | -0.00771 to 0.000427 | EVEN, no difference beyond the noise |
| host CPU-seconds | 234 | 227 | -2.9% | -14.9 to 1.23 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.561 | 0.538 | -4.1% | -0.0432 to -0.00334 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 15.3 |  | 9.08 to 21.6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
