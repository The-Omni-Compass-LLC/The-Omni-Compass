# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.0% | -1.7 to 1.06 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00782 to 0.00149 | no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.0011 to 0.000718 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.63 | 5.63 | +0.0% | -0.00662 to 0.00917 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.71 | +0.1% | 0.00216 to 0.0119 | **WORSE** |
| latency, mean (ms) | 1.65 | 1.66 | +0.3% | -0.0059 to 0.0151 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62 | -3.2% | -4.59 to 0.53 | no difference beyond the noise |
| memory used, mean (MB) | 57.2 | 55.9 | -2.2% | -2.84 to 0.364 | no difference beyond the noise |
| keys evicted | 71,692 | 71,755 | +0.1% | -179 to 305 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.125 | +8.0% | -0.0401 to 0.0587 | no difference beyond the noise |
| host CPU-seconds | 82.4 | 89.7 | +8.7% | -33.6 to 48 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.425 | 0.463 | +8.8% | -0.173 to 0.248 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.67 |  | 2.93 to 14.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 8.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
