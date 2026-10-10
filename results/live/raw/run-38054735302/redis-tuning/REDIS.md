# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,241 | +4.8% | 47.8 to 65.3 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0136 to 0.0152 | same |
| cache hit rate | 0.79 | 0.827 | +4.8% | 0.0318 to 0.0435 | better |
| latency, 95th percentile (ms) | 5.56 | 5.54 | -0.2% | -0.131 to 0.106 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.66 | 5.67 | +0.0% | -0.0585 to 0.064 | no difference beyond the noise |
| latency, mean (ms) | 1.23 | 1.04 | -15.9% | -0.231 to -0.161 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 78.9 | +23.3% | 9.11 to 20.7 | **WORSE** |
| memory used, mean (MB) | 61.2 | 73.2 | +19.5% | 9.9 to 14 | **WORSE** |
| keys evicted | 137,972 | 114,195 | -17.2% | -26,056 to -21,500 | shown, not judged |
| host CPU busy (share of the run) | 0.0974 | 0.0853 | -12.4% | -0.0291 to 0.00507 | no difference beyond the noise |
| host CPU-seconds | 173 | 150 | -13.4% | -54.6 to 8.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.324 | 0.268 | -17.4% | -0.113 to -7.46e-05 | better |
| ceiling changes written (the knob's moves) | 0 | 38.7 |  | 28.6 to 48.7 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
