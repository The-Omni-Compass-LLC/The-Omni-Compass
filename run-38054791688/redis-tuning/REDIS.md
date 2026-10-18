# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,248 | +5.4% | 43.9 to 84.9 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0151 to 0.0196 | no difference beyond the noise |
| cache hit rate | 0.789 | 0.832 | +5.4% | 0.0292 to 0.0567 | better |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.2% | -0.0183 to -4.65e-05 | better |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.0% | -0.0108 to 0.0124 | no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.11 | -17.6% | -0.308 to -0.167 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 82.7 | +29.2% | 1.96 to 35.4 | **WORSE** |
| memory used, mean (MB) | 61.2 | 75.7 | +23.7% | 3.68 to 25.3 | **WORSE** |
| keys evicted | 138,098 | 110,491 | -20.0% | -37,995 to -17,219 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.114 | -6.2% | -0.0326 to 0.0176 | no difference beyond the noise |
| host CPU-seconds | 204 | 191 | -6.1% | -60.9 to 36 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.382 | 0.34 | -10.9% | -0.127 to 0.0432 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 46 |  | 17.3 to 74.7 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
