# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.0% | -2.71 to 1.81 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0238 to 0.0173 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00167 to 0.00118 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.76 | +0.1% | -0.014 to 0.0264 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.83 | +0.4% | -0.0334 to 0.075 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.76 | +0.5% | -0.0129 to 0.0311 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62 | -3.1% | -3.78 to -0.19 | GAIN |
| memory used, mean (MB) | 57.2 | 56.1 | -1.8% | -2.81 to 0.699 | EVEN, no difference beyond the noise |
| keys evicted | 71,774 | 71,854 | +0.1% | -335 to 495 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.143 | +19.3% | -0.0218 to 0.068 | EVEN, no difference beyond the noise |
| host CPU-seconds | 78.6 | 96 | +22.2% | -16.6 to 51.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.406 | 0.496 | +22.3% | -0.0848 to 0.266 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
