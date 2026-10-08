# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,131 | 1,302 | +15.2% | 163 to 180 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00428 to 0.00185 | same |
| cache hit rate | 0.754 | 0.869 | +15.2% | 0.109 to 0.12 | better |
| latency, 95th percentile (ms) | 5.53 | 5.46 | -1.2% | -0.0773 to -0.0583 | better |
| latency, 99th percentile (ms) | 5.59 | 5.58 | -0.2% | -0.0174 to -0.00885 | better |
| latency, mean (ms) | 1.43 | 0.82 | -42.5% | -0.638 to -0.572 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 296 | +362.6% | 228 to 236 | **WORSE** |
| memory used, mean (MB) | 61.1 | 266 | +336.1% | 201 to 210 | **WORSE** |
| keys evicted | 106,664 | 29,399 | -72.4% | -81,227 to -73,303 | shown, not judged |
| host CPU busy (share of the run) | 0.0981 | 0.0905 | -7.8% | -0.0483 to 0.033 | no difference beyond the noise |
| host CPU-seconds | 114 | 106 | -7.6% | -61 to 43.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.337 | 0.27 | -19.8% | -0.215 to 0.0818 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 101 |  | 95.5 to 106 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
