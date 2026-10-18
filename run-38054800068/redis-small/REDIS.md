# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 927 | +0.1% | -10.3 to 12.5 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0121 to 0.0128 | same |
| cache hit rate | 0.617 | 0.618 | +0.1% | -0.00684 to 0.00842 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.68 | 5.68 | +0.0% | -0.00336 to 0.00663 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.2% | 0.00197 to 0.0178 | **WORSE** |
| latency, mean (ms) | 2.26 | 2.26 | -0.1% | -0.0453 to 0.0409 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | -0.266 to 2.74 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 60.9 | +0.4% | -0.351 to 0.832 | no difference beyond the noise |
| keys evicted | 243,257 | 243,837 | +0.2% | 52.2 to 1,108 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.148 | +7.7% | 0.00339 to 0.0177 | **WORSE** |
| host CPU-seconds | 229 | 250 | +9.1% | 7.03 to 34.5 | **WORSE** |
| host CPU-seconds per 1,000 requests inside the line | 0.55 | 0.599 | +9.0% | 0.00922 to 0.0893 | **WORSE** |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 20.5 to 25.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
