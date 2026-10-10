# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,896 | -0.1% | -3.01 to -1.09 | **WORSE** |
| throughput (operations a second) | 2,901 | 2,899 | -0.1% | -2.9 to -0.975 | **WORSE** |
| latency, 95th percentile (ms) | 0.308 | 0.31 | +0.9% | -0.000202 to 0.00554 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.478 | 0.48 | +0.3% | -0.00706 to 0.0104 | no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.198 | +1.5% | -0.00298 to 0.00874 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 465 | -9.3% | -107 to 11.8 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 384 | -8.0% | -88.1 to 21.1 | no difference beyond the noise |
| pages read into the cache (misses) | 691,164 | 787,717 | +14.0% | -10,782 to 203,887 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.17 | +2.8% | -0.0551 to 0.0645 | no difference beyond the noise |
| host CPU-seconds | 280 | 288 | +2.9% | -116 to 132 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.21 | 0.216 | +2.9% | -0.0868 to 0.0992 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | -2.3 to 6.3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
