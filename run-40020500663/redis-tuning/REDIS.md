# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,181 | 1,195 | +1.1% | 9.63 to 16.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00907 to 0.00179 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.0064 to 0.0111 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.0% | -0.00504 to 0.00228 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.32 | 5.32 | -0.1% | -0.0422 to 0.0335 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 1.14 | -3.8% | -0.0589 to -0.0318 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 1.17 to 2.01 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.9% | 0.985 to 1.32 | power given |
| keys evicted | 138,312 | 133,229 | -3.7% | -6,694 to -3,472 | shown, not judged |
| host CPU busy (share of the run) | 0.0649 | 0.0679 | +4.6% | -0.0367 to 0.0426 | EVEN, no difference beyond the noise |
| host CPU-seconds | 114 | 120 | +5.1% | -68.4 to 80 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.215 | 0.223 | +4.0% | -0.13 to 0.147 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
