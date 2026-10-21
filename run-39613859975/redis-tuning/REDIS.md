# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,195 | +0.9% | 5.81 to 15.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00405 to 0.00634 | EVEN, the same |
| cache hit rate | 0.789 | 0.797 | +0.9% | 0.00378 to 0.0105 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.00197 to 0.00311 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.1% | -0.00146 to 0.0141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.31 | -2.6% | -0.0503 to -0.0185 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.0% | 0.156 to 2.42 | power given |
| memory used, mean (MB) | 61.2 | 62.2 | +1.6% | 0.0215 to 1.91 | power given |
| keys evicted | 138,111 | 134,108 | -2.9% | -6,276 to -1,730 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.13 | +6.2% | -0.037 to 0.0522 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 220 | +7.2% | -71.4 to 101 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.386 | 0.41 | +6.2% | -0.137 to 0.185 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 12.1 to 27.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
