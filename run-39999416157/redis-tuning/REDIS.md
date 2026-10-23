# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `9678c8ad4325`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.2% | 11.3 to 17.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.015 to 0.01 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.799 | +1.2% | 0.00836 to 0.0102 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.0181 to 0.0206 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.3 | +0.4% | -0.13 to 0.171 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.12 | -4.3% | -0.0772 to -0.0231 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.9 | +2.9% | 1.58 to 2.14 | power given |
| memory used, mean (MB) | 61.2 | 62.5 | +2.2% | 1.1 to 1.56 | power given |
| keys evicted | 138,185 | 132,746 | -3.9% | -6,056 to -4,822 | shown, not judged |
| host CPU busy (share of the run) | 0.058 | 0.0692 | +19.4% | -0.0654 to 0.0879 | EVEN, no difference beyond the noise |
| host CPU-seconds | 102 | 123 | +20.6% | -123 to 165 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.192 | 0.229 | +19.1% | -0.232 to 0.306 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 23 to 23 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
