# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.8% | 2.32 to 17.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00846 to 0.00831 | EVEN, the same |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.00177 to 0.0116 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% | -0.0493 to 0.03 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.8 | -0.1% | -0.0599 to 0.0524 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.31 | -2.7% | -0.0799 to 0.00601 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | -0.323 to 3.25 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.3 | +1.7% | -0.045 to 2.17 | EVEN, no difference beyond the noise |
| keys evicted | 138,252 | 134,561 | -2.7% | -7,014 to -369 | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.121 | -5.4% | -0.0126 to -0.0012 | GAIN |
| host CPU-seconds | 215 | 202 | -5.7% | -23.8 to -0.736 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.403 | 0.377 | -6.5% | -0.0462 to -0.00622 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 12.6 to 24.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
