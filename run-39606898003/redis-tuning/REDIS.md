# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,197 | +1.1% | 6.15 to 19.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00413 to 0.00314 | EVEN, the same |
| cache hit rate | 0.79 | 0.798 | +1.1% | 0.00442 to 0.0125 | GAIN |
| latency, 95th percentile (ms) | 5.59 | 5.58 | -0.2% | -0.0347 to 0.0107 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.68 | 5.69 | +0.0% | -0.0249 to 0.0289 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.27 | 1.22 | -3.7% | -0.0672 to -0.0269 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.7% | 1.15 to 2.27 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.8% | 0.286 to 1.94 | power given |
| keys evicted | 138,051 | 133,443 | -3.3% | -8,507 to -709 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.104 | -3.6% | -0.0172 to 0.00932 | EVEN, no difference beyond the noise |
| host CPU-seconds | 188 | 181 | -3.9% | -33.2 to 18.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.353 | 0.335 | -4.9% | -0.0668 to 0.0322 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.7 |  | 21.2 to 24.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 26.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
