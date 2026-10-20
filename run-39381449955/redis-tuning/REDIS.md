# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,197 | +1.1% | 8.96 to 16.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.024 to 0.00684 | EVEN, no difference beyond the noise |
| cache hit rate | 0.79 | 0.798 | +1.1% | 0.00573 to 0.011 | GAIN |
| latency, 95th percentile (ms) | 5.65 | 5.66 | +0.2% | -0.0289 to 0.0526 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.73 | +0.2% | -0.00758 to 0.0338 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.29 | 1.25 | -2.9% | -0.0684 to -0.00553 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 66 | +3.1% | 0.713 to 3.25 | power given |
| memory used, mean (MB) | 61.2 | 62.5 | +2.2% | 0.455 to 2.22 | power given |
| keys evicted | 137,977 | 133,161 | -3.5% | -6,582 to -3,051 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.122 | +0.1% | -0.0472 to 0.0473 | EVEN, no difference beyond the noise |
| host CPU-seconds | 213 | 212 | -0.4% | -92.5 to 90.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.4 | 0.394 | -1.5% | -0.176 to 0.165 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
