# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,193 | +0.8% | 5.46 to 14.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0144 to 0.00573 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.796 | +0.9% | 0.00378 to 0.00968 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.0% | -0.0294 to 0.0297 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.85 | +0.7% | -0.0465 to 0.123 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.33 | -2.1% | -0.0444 to -0.0127 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | -0.219 to 2.67 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.1 | +1.5% | 0.0863 to 1.73 | power given |
| keys evicted | 138,220 | 134,500 | -2.7% | -5,706 to -1,734 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.132 | -2.3% | -0.0202 to 0.0139 | EVEN, no difference beyond the noise |
| host CPU-seconds | 228 | 221 | -2.7% | -38 to 25.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.427 | 0.412 | -3.5% | -0.0733 to 0.0435 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 14 to 24 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
