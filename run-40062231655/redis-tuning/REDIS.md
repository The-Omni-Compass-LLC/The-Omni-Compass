# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,197 | +1.1% | 10.8 to 15.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00215 to 0.000618 | EVEN, the same |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.00713 to 0.0102 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.51 | -0.1% | -0.025 to 0.0144 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.59 | -0.0% | -0.0127 to 0.011 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.19 | -3.8% | -0.0642 to -0.0304 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 66 | +3.1% | 0.726 to 3.24 | power given |
| memory used, mean (MB) | 61.2 | 62.5 | +2.2% | 0.37 to 2.34 | power given |
| keys evicted | 138,136 | 133,370 | -3.5% | -6,552 to -2,980 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.102 | -4.9% | -0.0253 to 0.0149 | EVEN, no difference beyond the noise |
| host CPU-seconds | 189 | 179 | -5.3% | -50.2 to 30.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.355 | 0.332 | -6.4% | -0.097 to 0.0519 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 15.4 to 28.6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
