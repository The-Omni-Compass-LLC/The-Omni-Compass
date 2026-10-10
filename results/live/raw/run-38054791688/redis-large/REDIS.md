# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,358 | +7.1% | 81.7 to 97.8 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00176 to 0.00147 | same |
| cache hit rate | 0.845 | 0.905 | +7.1% | 0.0545 to 0.0652 | better |
| latency, 95th percentile (ms) | 5.53 | 5.45 | -1.4% | -0.106 to -0.0477 | better |
| latency, 99th percentile (ms) | 5.65 | 5.62 | -0.5% | -0.0376 to -0.021 | better |
| latency, mean (ms) | 0.958 | 0.635 | -33.7% | -0.35 to -0.295 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 77.9 | +21.7% | 11 to 16.7 | **WORSE** |
| memory used, mean (MB) | 61.3 | 70.3 | +14.7% | 5.31 to 12.7 | **WORSE** |
| keys evicted | 103,134 | 63,197 | -38.7% | -43,810 to -36,064 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.102 | -2.6% | -0.0406 to 0.0352 | no difference beyond the noise |
| host CPU-seconds | 188 | 184 | -2.4% | -80.5 to 71.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.329 | 0.3 | -8.8% | -0.161 to 0.103 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 47.7 |  | 35.4 to 59.9 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 18.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
