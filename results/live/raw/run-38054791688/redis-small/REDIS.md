# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 925 | -0.0% | -10.9 to 10.1 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0114 to 0.000292 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.617 | -0.0% | -0.00722 to 0.00672 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.52 | 5.51 | -0.2% | -0.0255 to 0.00138 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.58 | -0.1% | -0.0209 to 0.00622 | no difference beyond the noise |
| latency, mean (ms) | 2.15 | 2.14 | -0.2% | -0.0416 to 0.0331 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 69.2 | +8.2% | 0.512 to 9.94 | **WORSE** |
| memory used, mean (MB) | 60.7 | 63.5 | +4.6% | -3.16 to 8.7 | no difference beyond the noise |
| keys evicted | 243,151 | 247,083 | +1.6% | 977 to 6,888 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.109 | -2.4% | -0.0135 to 0.00811 | no difference beyond the noise |
| host CPU-seconds | 196 | 191 | -2.4% | -25.4 to 16 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.47 | 0.459 | -2.3% | -0.0601 to 0.0381 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 27.3 |  | 25.9 to 28.8 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
