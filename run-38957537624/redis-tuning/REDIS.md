# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,198 | +1.2% | 12.7 to 16 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00468 to 0.00192 | EVEN, the same |
| cache hit rate | 0.789 | 0.799 | +1.2% | 0.00854 to 0.0106 | GAIN |
| latency, 95th percentile (ms) | 5.54 | 5.53 | -0.1% | -0.0361 to 0.0235 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.61 | -0.0% | -0.0234 to 0.0178 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.25 | 1.19 | -4.2% | -0.0656 to -0.0397 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.8 | +2.8% | 1.57 to 1.98 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +2.1% | 1.08 to 1.43 | power given |
| keys evicted | 138,160 | 132,529 | -4.1% | -6,320 to -4,942 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.0962 | -6.6% | -0.0399 to 0.0263 | EVEN, no difference beyond the noise |
| host CPU-seconds | 181 | 168 | -7.3% | -78 to 51.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.34 | 0.311 | -8.4% | -0.15 to 0.0932 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 23 to 23 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
