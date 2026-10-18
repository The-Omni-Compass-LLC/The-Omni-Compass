# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 831 | 1,048 | +26.0% | 214 to 219 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0397 to 0.0248 | no difference beyond the noise |
| cache hit rate | 0.555 | 0.699 | +26.0% | 0.143 to 0.146 | better |
| latency, 95th percentile (ms) | 5.51 | 5.48 | -0.6% | -0.0452 to -0.0158 | better |
| latency, 99th percentile (ms) | 5.57 | 5.56 | -0.2% | -0.013 to -0.00623 | better |
| latency, mean (ms) | 2.47 | 1.71 | -30.9% | -0.785 to -0.744 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 269 | +319.9% | 196 to 213 | **WORSE** |
| memory used, mean (MB) | 60.3 | 210 | +248.4% | 150 to 150 | **WORSE** |
| keys evicted | 185,132 | 18,693 | -89.9% | -167,219 to -165,659 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.106 | -2.6% | -0.0693 to 0.0636 | no difference beyond the noise |
| host CPU-seconds | 127 | 125 | -1.5% | -87.7 to 83.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.507 | 0.397 | -21.8% | -0.412 to 0.191 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 49.7 |  | 37.4 to 61.9 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 12.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
