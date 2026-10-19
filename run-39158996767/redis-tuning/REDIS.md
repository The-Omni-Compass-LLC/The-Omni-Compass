# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,191 | +0.6% | 2.23 to 13 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00332 to 0.00316 | EVEN, the same |
| cache hit rate | 0.789 | 0.794 | +0.6% | 0.0011 to 0.00904 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.0% | -0.00362 to 0.00614 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.2% | 0.00495 to 0.0129 | LOSS |
| latency, mean (ms) | 1.35 | 1.33 | -1.9% | -0.0516 to 0.000528 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.6 | +1.0% | -0.349 to 1.59 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 61.6 | +0.6% | -0.42 to 1.21 | EVEN, no difference beyond the noise |
| keys evicted | 138,331 | 136,283 | -1.5% | -5,230 to 1,133 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.13 | +6.8% | -0.0567 to 0.0732 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 219 | +7.5% | -109 to 140 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.382 | 0.408 | +6.8% | -0.209 to 0.262 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 8.46 to 30.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
