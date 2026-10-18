# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,108 | 4,970 | -2.7% | -499 to 224 | no difference beyond the noise |
| throughput (operations a second) | 5,131 | 4,993 | -2.7% | -497 to 220 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.36 | 0.362 | +0.6% | -0.000535 to 0.0052 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.61 | 0.609 | -0.1% | -0.0441 to 0.0428 | no difference beyond the noise |
| latency, mean (ms) | 0.246 | 0.257 | +4.5% | -0.00804 to 0.0303 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 379 | -25.9% | -156 to -110 | better |
| bytes in the cache, mean (MB) | 409 | 309 | -24.4% | -117 to -83 | better |
| pages read into the cache (misses) | 415,673 | 521,046 | +25.3% | 7,115 to 203,631 | shown, not judged |
| host CPU busy (share of the run) | 0.259 | 0.24 | -7.5% | -0.0308 to -0.00823 | better |
| host CPU-seconds | 319 | 290 | -9.1% | -43.5 to -14.4 | better |
| host CPU-seconds per 1,000 operations inside the line | 0.202 | 0.188 | -6.6% | -0.029 to 0.00223 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
