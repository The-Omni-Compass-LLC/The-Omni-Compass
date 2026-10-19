# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,192 | +0.7% | -0.963 to 16.4 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0174 to 0.0185 | EVEN, the same |
| cache hit rate | 0.79 | 0.795 | +0.7% | -0.00058 to 0.011 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.1% | -0.00473 to 0.0168 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.81 | +0.3% | -0.000116 to 0.0311 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.32 | -1.7% | -0.0586 to 0.0138 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | 0.161 to 1.66 | power given |
| memory used, mean (MB) | 61.2 | 61.8 | +1.0% | -0.0615 to 1.27 | EVEN, no difference beyond the noise |
| keys evicted | 138,050 | 135,913 | -1.5% | -5,486 to 1,214 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.131 | -1.5% | -0.0402 to 0.0364 | EVEN, no difference beyond the noise |
| host CPU-seconds | 224 | 220 | -1.9% | -78.5 to 69.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.42 | 0.409 | -2.6% | -0.15 to 0.129 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.3 |  | 3.79 to 36.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
