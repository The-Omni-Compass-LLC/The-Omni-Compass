# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,193 | +0.8% | 1.82 to 17.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00731 to 0.00658 | EVEN, the same |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.00167 to 0.0115 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.0286 to 0.017 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.81 | +0.0% | -0.0209 to 0.026 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.32 | -2.5% | -0.0607 to -0.00802 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.7% | -0.25 to 2.38 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 61.9 | +1.2% | -0.0536 to 1.54 | EVEN, no difference beyond the noise |
| keys evicted | 138,257 | 134,915 | -2.4% | -7,211 to 527 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.118 | -11.3% | -0.0331 to 0.00313 | EVEN, no difference beyond the noise |
| host CPU-seconds | 224 | 196 | -12.5% | -63.3 to 7.46 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.42 | 0.364 | -13.2% | -0.122 to 0.0113 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.3 |  | 11.9 to 30.7 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
