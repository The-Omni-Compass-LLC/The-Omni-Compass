# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,858 | 2,858 | +0.0% | -3.7 to 3.72 | no difference beyond the noise |
| throughput (operations a second) | 2,863 | 2,863 | -0.0% | -2.91 to 2.9 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.407 | 0.403 | -1.1% | -0.0147 to 0.00537 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.55 | 0.542 | -1.4% | -0.0277 to 0.0124 | no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.216 | +0.5% | -0.0109 to 0.0131 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 259 | -49.5% | -253 to -253 | better |
| bytes in the cache, mean (MB) | 418 | 214 | -48.7% | -215 to -192 | better |
| pages read into the cache (misses) | 486,224 | 712,413 | +46.5% | 213,039 to 239,338 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.204 | -3.8% | -0.087 to 0.0707 | no difference beyond the noise |
| host CPU-seconds | 241 | 229 | -5.0% | -121 to 97.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.259 | -5.0% | -0.138 to 0.11 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
