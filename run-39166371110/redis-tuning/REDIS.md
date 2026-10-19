# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,197 | +1.1% | 4.39 to 21 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.006 to 0.00569 | EVEN, the same |
| cache hit rate | 0.79 | 0.798 | +1.1% | 0.00312 to 0.0137 | GAIN |
| latency, 95th percentile (ms) | 5.2 | 5.2 | +0.0% | -0.00293 to 0.00373 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.00609 to 0.00761 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.15 | 1.1 | -3.8% | -0.0735 to -0.0139 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.8 | +2.9% | 0.0628 to 3.6 | power given |
| memory used, mean (MB) | 61.2 | 62.5 | +2.2% | 0.213 to 2.46 | power given |
| keys evicted | 137,976 | 133,127 | -3.5% | -8,435 to -1,262 | shown, not judged |
| host CPU busy (share of the run) | 0.0465 | 0.0543 | +16.7% | -0.0592 to 0.0748 | EVEN, no difference beyond the noise |
| host CPU-seconds | 81.9 | 96.4 | +17.8% | -108 to 137 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.154 | 0.179 | +16.6% | -0.203 to 0.254 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 15.9 to 27.4 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
