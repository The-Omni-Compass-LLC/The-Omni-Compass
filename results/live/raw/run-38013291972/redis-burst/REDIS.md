# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -2.51 to 2.13 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00344 to 0.00627 | same |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.00166 to 0.00142 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.0% | -0.0143 to 0.0121 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.81 | +0.1% | -0.0124 to 0.021 | no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.75 | +0.3% | -0.00238 to 0.0118 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.1 | -4.6% | -3.41 to -2.49 | better |
| memory used, mean (MB) | 57.2 | 55.2 | -3.5% | -2.49 to -1.48 | better |
| keys evicted | 71,747 | 71,787 | +0.1% | -391 to 470 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.141 | +2.4% | -0.094 to 0.1 | no difference beyond the noise |
| host CPU-seconds | 92.5 | 94.7 | +2.4% | -74.2 to 78.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.478 | 0.489 | +2.4% | -0.384 to 0.407 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
