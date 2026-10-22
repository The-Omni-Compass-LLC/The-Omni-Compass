# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 938 | +1.3% | 11.5 to 12.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0234 to 0.0181 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00768 to 0.00872 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.7 | +0.0% | -0.0157 to 0.0182 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 5.77 | +0.2% | -0.00874 to 0.0285 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.23 | -1.9% | -0.0499 to -0.0347 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.8 | +2.8% | 0.972 to 2.58 | power given |
| memory used, mean (MB) | 60.7 | 61.7 | +1.6% | 0.481 to 1.51 | power given |
| keys evicted | 243,273 | 238,280 | -2.1% | -12,565 to 2,579 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.151 | -1.2% | -0.0505 to 0.0467 | EVEN, no difference beyond the noise |
| host CPU-seconds | 258 | 255 | -1.3% | -98.3 to 91.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.62 | 0.604 | -2.6% | -0.243 to 0.211 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17 |  | 8.39 to 25.6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
