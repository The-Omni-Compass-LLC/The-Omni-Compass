# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,551 | 5,535 | -0.3% | -81.6 to 49.6 | no difference beyond the noise |
| throughput (operations a second) | 5,570 | 5,552 | -0.3% | -82.6 to 46.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.462 | 0.467 | +1.0% | 0.000872 to 0.00846 | **WORSE** |
| latency, 99th percentile (ms) | 0.7 | 0.695 | -0.7% | -0.0222 to 0.0122 | no difference beyond the noise |
| latency, mean (ms) | 0.266 | 0.268 | +1.0% | -0.000971 to 0.00613 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 324 | -36.8% | -263 to -114 | better |
| bytes in the cache, mean (MB) | 415 | 263 | -36.6% | -215 to -88.8 | better |
| pages read into the cache (misses) | 456,436 | 677,907 | +48.5% | 127,032 to 315,911 | shown, not judged |
| host CPU busy (share of the run) | 0.32 | 0.318 | -0.6% | -0.0138 to 0.0101 | no difference beyond the noise |
| host CPU-seconds | 364 | 361 | -0.9% | -21.3 to 14.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.21 | 0.209 | -0.7% | -0.0111 to 0.00834 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
