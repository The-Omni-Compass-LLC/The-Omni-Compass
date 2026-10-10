# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -2.71 to 1.01 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0251 to 0.0249 | same |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00167 to 0.000621 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.0% | -0.0229 to 0.026 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.81 | +0.1% | -0.0201 to 0.0366 | no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.75 | +0.4% | -0.00313 to 0.0172 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.7 | -3.7% | -5.47 to 0.791 | no difference beyond the noise |
| memory used, mean (MB) | 57.2 | 55.6 | -2.7% | -3.66 to 0.544 | no difference beyond the noise |
| keys evicted | 71,725 | 71,882 | +0.2% | -146 to 460 | shown, not judged |
| host CPU busy (share of the run) | 0.131 | 0.138 | +5.5% | -0.00731 to 0.0217 | no difference beyond the noise |
| host CPU-seconds | 87.3 | 92.8 | +6.4% | -5.12 to 16.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.45 | 0.479 | +6.4% | -0.0257 to 0.0837 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.67 |  | 2.93 to 14.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 8.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
