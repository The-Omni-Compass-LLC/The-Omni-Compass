# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,288 | +1.7% | 18.7 to 23.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00174 to 0.00268 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.7% | 0.0124 to 0.0159 | GAIN |
| latency, 95th percentile (ms) | 5.62 | 5.59 | -0.6% | -0.0679 to 0.00279 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.72 | -0.2% | -0.0377 to 0.0135 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.981 | 0.898 | -8.5% | -0.0935 to -0.073 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.5% | 0.579 to 1.4 | power given |
| memory used, mean (MB) | 61.3 | 62 | +1.1% | 0.249 to 1.08 | power given |
| keys evicted | 103,420 | 94,114 | -9.0% | -10,456 to -8,156 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.105 | +1.5% | -0.0614 to 0.0644 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 186 | +2.5% | -120 to 129 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.319 | 0.321 | +0.8% | -0.213 to 0.218 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
