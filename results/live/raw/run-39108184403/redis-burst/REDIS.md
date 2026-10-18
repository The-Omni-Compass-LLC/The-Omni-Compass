# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -2.13 to 0.0127 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0267 to 0.0134 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.000828 to -0.000291 | LOSS |
| latency, 95th percentile (ms) | 5.73 | 5.73 | +0.0% | -0.00807 to 0.0109 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.2% | 0.00392 to 0.018 | LOSS |
| latency, mean (ms) | 1.73 | 1.74 | +0.3% | -0.00177 to 0.0129 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.4 | -2.5% | -1.8 to -1.34 | GAIN |
| memory used, mean (MB) | 57.2 | 56.5 | -1.2% | -0.926 to -0.453 | GAIN |
| keys evicted | 71,693 | 71,860 | +0.2% | 109 to 225 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.142 | -7.7% | -0.0557 to 0.0319 | EVEN, no difference beyond the noise |
| host CPU-seconds | 106 | 96.3 | -9.2% | -45 to 25.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.547 | 0.497 | -9.1% | -0.231 to 0.132 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
