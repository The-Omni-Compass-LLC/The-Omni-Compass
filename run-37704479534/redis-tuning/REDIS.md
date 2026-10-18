# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,131 | 1,304 | +15.3% | 162 to 184 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000687 to 0.00354 | same |
| cache hit rate | 0.754 | 0.869 | +15.3% | 0.108 to 0.123 | better |
| latency, 95th percentile (ms) | 5.55 | 5.48 | -1.3% | -0.0898 to -0.0582 | better |
| latency, 99th percentile (ms) | 5.61 | 5.59 | -0.3% | -0.0213 to -0.0163 | better |
| latency, mean (ms) | 1.43 | 0.814 | -43.2% | -0.66 to -0.577 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 297 | +364.0% | 231 to 235 | **WORSE** |
| memory used, mean (MB) | 61.1 | 267 | +337.7% | 204 to 209 | **WORSE** |
| keys evicted | 106,679 | 29,909 | -72.0% | -78,173 to -75,367 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.0883 | -17.8% | -0.0797 to 0.0414 | no difference beyond the noise |
| host CPU-seconds | 126 | 103 | -18.3% | -101 to 54.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.371 | 0.263 | -29.1% | -0.324 to 0.107 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 98.7 |  | 97.2 to 100 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
