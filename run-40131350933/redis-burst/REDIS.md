# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -1.79 to 0.0645 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.031 to 0.0536 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.1% | -0.00106 to -4.48e-05 | LOSS |
| latency, 95th percentile (ms) | 5.65 | 5.65 | +0.0% | -0.0116 to 0.0155 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.72 | +0.1% | -0.0139 to 0.0297 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.67 | 1.68 | +0.4% | -0.00888 to 0.0213 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.1 | -3.0% | -3.63 to -0.251 | GAIN |
| memory used, mean (MB) | 57.2 | 56.1 | -1.9% | -2.85 to 0.706 | EVEN, no difference beyond the noise |
| keys evicted | 71,615 | 71,774 | +0.2% | 24.9 to 294 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.114 | -9.2% | -0.0433 to 0.0201 | EVEN, no difference beyond the noise |
| host CPU-seconds | 89.1 | 79.9 | -10.3% | -34.4 to 16 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.46 | 0.413 | -10.3% | -0.177 to 0.0831 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
