# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,867 | 2,864 | -0.1% | -10.8 to 5.87 | no difference beyond the noise |
| throughput (operations a second) | 2,874 | 2,872 | -0.1% | -11.2 to 6.85 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.491 | 0.494 | +0.7% | -0.00184 to 0.0085 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.701 | 0.704 | +0.3% | -0.00771 to 0.0124 | no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.216 | +3.7% | 0.00475 to 0.0105 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 304 | -40.6% | -385 to -31.4 | better |
| bytes in the cache, mean (MB) | 397 | 244 | -38.6% | -296 to -10.6 | better |
| pages read into the cache (misses) | 179,920 | 261,693 | +45.5% | -13,021 to 176,568 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.229 | +16.4% | -0.0216 to 0.086 | no difference beyond the noise |
| host CPU-seconds | 94.4 | 114 | +20.6% | -14.7 to 53.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.268 | 0.323 | +20.7% | -0.0418 to 0.152 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
