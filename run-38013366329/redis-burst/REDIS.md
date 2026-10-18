# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.1% | -1.87 to 0.422 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00909 to 0.0136 | no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00118 to 0.000324 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.1% | -0.00888 to 0.0157 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.2% | 0.00563 to 0.0187 | **WORSE** |
| latency, mean (ms) | 1.74 | 1.75 | +0.5% | -0.00271 to 0.0203 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 60.9 | -4.8% | -3.22 to -2.88 | better |
| memory used, mean (MB) | 57.2 | 55 | -3.7% | -2.36 to -1.91 | better |
| keys evicted | 71,739 | 71,864 | +0.2% | -54.8 to 304 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.136 | +9.0% | -0.0342 to 0.0568 | no difference beyond the noise |
| host CPU-seconds | 83.5 | 91.8 | +9.9% | -26.6 to 43.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.431 | 0.474 | +10.0% | -0.137 to 0.223 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
