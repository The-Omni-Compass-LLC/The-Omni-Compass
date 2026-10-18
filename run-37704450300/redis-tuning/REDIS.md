# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,131 | 1,304 | +15.3% | 161 to 186 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00538 to 0.00855 | no difference beyond the noise |
| cache hit rate | 0.754 | 0.87 | +15.3% | 0.107 to 0.124 | better |
| latency, 95th percentile (ms) | 5.62 | 5.57 | -1.0% | -0.092 to -0.018 | better |
| latency, 99th percentile (ms) | 5.69 | 5.67 | -0.3% | -0.0433 to 0.00656 | no difference beyond the noise |
| latency, mean (ms) | 1.46 | 0.836 | -42.9% | -0.674 to -0.584 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 299 | +366.6% | 233 to 236 | **WORSE** |
| memory used, mean (MB) | 61.1 | 269 | +340.6% | 207 to 209 | **WORSE** |
| keys evicted | 106,700 | 28,696 | -73.1% | -80,859 to -75,148 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.097 | -18.4% | -0.0402 to -0.00364 | better |
| host CPU-seconds | 141 | 114 | -19.1% | -52.2 to -1.44 | better |
| host CPU-seconds per 1,000 requests inside the line | 0.414 | 0.29 | -29.9% | -0.191 to -0.0561 | better |
| ceiling changes written (the knob's moves) | 0 | 97 |  | 92.7 to 101 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
