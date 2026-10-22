# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,193 | +1.0% | 6.81 to 16.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00396 to 0.0185 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.797 | +1.0% | 0.00472 to 0.0107 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.22 | -0.0% | -0.0187 to 0.0157 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.31 | 5.31 | -0.1% | -0.18 to 0.174 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 1.14 | -3.3% | -0.0638 to -0.0143 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.6% | 1.19 to 2.13 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +1.9% | 1.02 to 1.34 | power given |
| keys evicted | 138,213 | 133,839 | -3.2% | -6,406 to -2,342 | shown, not judged |
| host CPU busy (share of the run) | 0.0557 | 0.0714 | +28.2% | 0.00106 to 0.0303 | power given |
| host CPU-seconds | 96.9 | 126 | +30.5% | 1.49 to 57.7 | power given |
| host CPU-seconds per 1,000 requests inside the line | 0.182 | 0.235 | +29.2% | 0.00202 to 0.105 | power given |
| ceiling changes written (the knob's moves) | 0 | 20.3 |  | 12.7 to 27.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
