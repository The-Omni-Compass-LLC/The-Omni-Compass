# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -2.15 to 0.782 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0393 to 0.0215 | no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00138 to 0.000474 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.62 | 5.63 | +0.2% | -0.0435 to 0.066 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.67 | 5.68 | +0.2% | -0.0306 to 0.0493 | no difference beyond the noise |
| latency, mean (ms) | 1.65 | 1.67 | +0.8% | -0.0316 to 0.0568 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.2 | -4.3% | -2.95 to -2.56 | better |
| memory used, mean (MB) | 57.2 | 55.3 | -3.2% | -1.95 to -1.69 | better |
| keys evicted | 71,660 | 71,788 | +0.2% | -159 to 415 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.107 | +5.3% | -0.0296 to 0.0404 | no difference beyond the noise |
| host CPU-seconds | 70 | 73.9 | +5.6% | -22.1 to 30 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.361 | 0.382 | +5.7% | -0.114 to 0.155 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
