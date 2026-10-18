# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,281 | +1.1% | 7.43 to 21.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000692 to 0.00211 | EVEN, the same |
| cache hit rate | 0.845 | 0.855 | +1.1% | 0.00518 to 0.0142 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.75 | -0.1% | -0.0146 to 0.0088 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.83 | +0.0% | -0.0151 to 0.0209 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 1.01 | -5.0% | -0.0734 to -0.0325 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.3 | +0.5% | -0.997 to 1.66 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.3 | +0.0% | -0.772 to 0.828 | EVEN, no difference beyond the noise |
| keys evicted | 103,421 | 97,098 | -6.1% | -9,374 to -3,272 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.116 | -6.5% | -0.0186 to 0.00258 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 193 | -7.2% | -35 to 5.15 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.364 | 0.334 | -8.2% | -0.0659 to 0.00587 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 21 to 21 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
