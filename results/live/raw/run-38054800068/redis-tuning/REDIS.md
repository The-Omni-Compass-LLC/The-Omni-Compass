# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,254 | +5.9% | 59.5 to 80.7 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00184 to 0.00183 | same |
| cache hit rate | 0.79 | 0.836 | +5.9% | 0.0397 to 0.0539 | better |
| latency, 95th percentile (ms) | 5.2 | 5.2 | -0.1% | -0.00567 to -0.000714 | better |
| latency, 99th percentile (ms) | 5.22 | 5.22 | -0.0% | -0.00695 to 0.00475 | no difference beyond the noise |
| latency, mean (ms) | 1.14 | 0.902 | -21.0% | -0.273 to -0.205 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 86.1 | +34.5% | 16.8 to 27.4 | **WORSE** |
| memory used, mean (MB) | 61.2 | 79.6 | +30.1% | 12.3 to 24.5 | **WORSE** |
| keys evicted | 137,987 | 107,544 | -22.1% | -35,718 to -25,169 | shown, not judged |
| host CPU busy (share of the run) | 0.0416 | 0.0517 | +24.3% | -0.023 to 0.0432 | no difference beyond the noise |
| host CPU-seconds | 72.8 | 91.5 | +25.8% | -41.8 to 79.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.137 | 0.162 | +18.7% | -0.0833 to 0.134 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 38.7 |  | 22.9 to 54.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
