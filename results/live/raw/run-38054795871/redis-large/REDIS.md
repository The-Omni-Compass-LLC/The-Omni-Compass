# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,348 | +6.7% | 64.1 to 105 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0127 to 0.00179 | no difference beyond the noise |
| cache hit rate | 0.844 | 0.901 | +6.7% | 0.0421 to 0.0707 | better |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.2% | -0.0255 to 0.00311 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.24 | -0.2% | -0.0292 to 0.00909 | no difference beyond the noise |
| latency, mean (ms) | 0.894 | 0.601 | -32.7% | -0.368 to -0.217 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 76.4 | +19.4% | 4.31 to 20.6 | **WORSE** |
| memory used, mean (MB) | 61.3 | 69.5 | +13.4% | 5.2 to 11.2 | **WORSE** |
| keys evicted | 103,742 | 66,177 | -36.2% | -46,844 to -28,287 | shown, not judged |
| host CPU busy (share of the run) | 0.0581 | 0.0594 | +2.3% | -0.00875 to 0.0114 | no difference beyond the noise |
| host CPU-seconds | 102 | 105 | +2.9% | -16.1 to 22 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.18 | 0.174 | -3.7% | -0.0303 to 0.017 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 45.3 |  | 15 to 75.7 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
