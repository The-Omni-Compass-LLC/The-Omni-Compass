# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,290 | +1.8% | 19.4 to 25.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00263 to 0.00267 | EVEN, the same |
| cache hit rate | 0.845 | 0.86 | +1.8% | 0.0129 to 0.0169 | GAIN |
| latency, 95th percentile (ms) | 5.6 | 5.58 | -0.3% | -0.0232 to -0.00567 | GAIN |
| latency, 99th percentile (ms) | 5.7 | 5.7 | -0.0% | -0.0108 to 0.00518 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.981 | 0.899 | -8.3% | -0.0839 to -0.0793 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.4% | -0.684 to 3.77 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.4 | +1.8% | -0.262 to 2.44 | EVEN, no difference beyond the noise |
| keys evicted | 103,178 | 93,244 | -9.6% | -11,592 to -8,277 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.107 | -5.6% | -0.045 to 0.0324 | EVEN, no difference beyond the noise |
| host CPU-seconds | 202 | 190 | -6.0% | -89 to 64.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.355 | 0.328 | -7.7% | -0.16 to 0.106 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20 |  | 17.5 to 22.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
