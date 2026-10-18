# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 927 | +0.1% | -9.45 to 11 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.024 to 0.00966 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.618 | +0.1% | -0.00623 to 0.00739 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.00103 to 0.00632 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.2% | 0.00191 to 0.0212 | **WORSE** |
| latency, mean (ms) | 2.26 | 2.26 | -0.0% | -0.0396 to 0.039 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.8% | -0.601 to 2.86 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 60.9 | +0.4% | -0.342 to 0.834 | no difference beyond the noise |
| keys evicted | 243,139 | 243,876 | +0.3% | 391 to 1,084 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.134 | -8.7% | -0.0446 to 0.0192 | no difference beyond the noise |
| host CPU-seconds | 247 | 222 | -10.1% | -86.2 to 36.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.592 | 0.532 | -10.2% | -0.211 to 0.0901 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 17.7 to 26.3 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
