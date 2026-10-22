# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,265 | 1,282 | +1.4% | 9.87 to 24.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00127 to 0.00243 | EVEN, the same |
| cache hit rate | 0.845 | 0.856 | +1.3% | 0.00683 to 0.0159 | GAIN |
| latency, 95th percentile (ms) | 5.24 | 5.22 | -0.2% | -0.0613 to 0.0365 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.39 | 5.28 | -2.1% | -0.594 to 0.368 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.9 | 0.831 | -7.6% | -0.0985 to -0.0384 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.8 | +1.3% | 0.211 to 1.45 | power given |
| memory used, mean (MB) | 61.3 | 61.6 | +0.6% | -0.591 to 1.29 | EVEN, no difference beyond the noise |
| keys evicted | 103,523 | 96,008 | -7.3% | -10,344 to -4,688 | shown, not judged |
| host CPU busy (share of the run) | 0.0658 | 0.0681 | +3.6% | -0.00196 to 0.00668 | EVEN, no difference beyond the noise |
| host CPU-seconds | 116 | 121 | +4.5% | -2.34 to 12.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.203 | 0.21 | +3.1% | -0.00671 to 0.0195 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20 |  | 17.5 to 22.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
