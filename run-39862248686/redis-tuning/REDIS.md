# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,193 | +0.8% | 1.26 to 17.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0113 to 0.00794 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.000872 to 0.0114 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.7 | +0.1% | -0.0315 to 0.0428 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.2% | -0.0369 to 0.0633 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.33 | 1.3 | -2.3% | -0.0685 to 0.00796 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.7% | 0.256 to 1.88 | power given |
| memory used, mean (MB) | 61.2 | 62 | +1.2% | 0.273 to 1.25 | power given |
| keys evicted | 138,130 | 135,085 | -2.2% | -6,246 to 157 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.113 | -2.0% | -0.0108 to 0.00622 | EVEN, no difference beyond the noise |
| host CPU-seconds | 195 | 190 | -2.4% | -22.6 to 13.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.365 | 0.354 | -3.1% | -0.0433 to 0.0205 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 5.85 to 32.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
