# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 922 | -0.4% | -5.45 to -2.31 | **WORSE** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.039 to 0.0173 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.615 | -0.4% | -0.00347 to -0.00156 | **WORSE** |
| latency, 95th percentile (ms) | 5.69 | 5.69 | -0.0% | -0.00526 to 0.00276 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.1% | 0.00159 to 0.0122 | **WORSE** |
| latency, mean (ms) | 2.26 | 2.28 | +0.7% | 0.00903 to 0.0211 | **WORSE** |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.9 | -0.1% | -0.492 to 0.327 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 60.4 | -0.4% | -0.78 to 0.26 | no difference beyond the noise |
| keys evicted | 243,201 | 246,020 | +1.2% | -1,822 to 7,458 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.131 | -8.3% | -0.023 to -0.000643 | better |
| host CPU-seconds | 240 | 217 | -9.5% | -44.3 to -1.51 | better |
| host CPU-seconds per 1,000 requests inside the line | 0.577 | 0.524 | -9.1% | -0.103 to -0.00206 | better |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 13.6 to 31.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
