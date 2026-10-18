# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,342 | +5.9% | -21.7 to 171 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00234 to 0.0017 | same |
| cache hit rate | 0.845 | 0.895 | +5.9% | -0.0143 to 0.114 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.72 | -0.4% | -0.0703 to 0.0289 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.81 | -0.1% | -0.0318 to 0.0251 | no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.775 | -26.1% | -0.635 to 0.0868 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 73.1 | +14.2% | -5.72 to 24 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 67.6 | +10.3% | -5.37 to 18 | no difference beyond the noise |
| keys evicted | 103,236 | 70,109 | -32.1% | -76,806 to 10,551 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.107 | -10.2% | -0.0368 to 0.0127 | no difference beyond the noise |
| host CPU-seconds | 199 | 178 | -10.6% | -65.2 to 23.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.348 | 0.294 | -15.5% | -0.152 to 0.0436 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 45.3 |  | 25.1 to 65.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
