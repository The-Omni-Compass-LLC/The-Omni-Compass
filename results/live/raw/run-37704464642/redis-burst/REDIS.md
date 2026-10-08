# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,046 | 1,192 | +13.9% | 118 to 174 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0664 to 0.127 | no difference beyond the noise |
| cache hit rate | 0.697 | 0.795 | +13.9% | 0.0787 to 0.116 | better |
| latency, 95th percentile (ms) | 5.65 | 5.62 | -0.6% | -0.0497 to -0.0228 | better |
| latency, 99th percentile (ms) | 5.72 | 5.71 | -0.2% | -0.0241 to 0.0049 | no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.23 | -30.1% | -0.625 to -0.431 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 195 | +204.8% | 89.7 to 172 | **WORSE** |
| memory used, mean (MB) | 56.9 | 155 | +171.4% | 77.6 to 118 | **WORSE** |
| keys evicted | 49,932 | 11,192 | -77.6% | -44,262 to -33,217 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.106 | -2.7% | -0.0655 to 0.0596 | no difference beyond the noise |
| host CPU-seconds | 51.4 | 50.3 | -2.2% | -34.8 to 32.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.41 | 0.352 | -14.1% | -0.314 to 0.198 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 30.7 |  | 10.4 to 50.9 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 10.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
