# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,282 | +1.4% | 9.78 to 25 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.038 to 0.0197 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.856 | +1.4% | 0.00583 to 0.017 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.23 | +0.1% | -0.0117 to 0.0179 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.27 | +0.2% | -0.00016 to 0.0261 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.89 | 0.835 | -6.2% | -0.0813 to -0.03 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.4 | +0.6% | -0.25 to 0.996 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.2 | -0.1% | -0.296 to 0.17 | EVEN, no difference beyond the noise |
| keys evicted | 103,618 | 96,130 | -7.2% | -11,233 to -3,744 | shown, not judged |
| host CPU busy (share of the run) | 0.0471 | 0.0578 | +22.7% | -0.00358 to 0.025 | EVEN, no difference beyond the noise |
| host CPU-seconds | 81.9 | 102 | +24.0% | -7.03 to 46.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.144 | 0.176 | +22.4% | -0.0148 to 0.0792 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
