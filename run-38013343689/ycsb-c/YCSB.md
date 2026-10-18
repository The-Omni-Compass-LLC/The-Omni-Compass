# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,890 | -0.1% | -3.57 to -2.02 | **WORSE** |
| throughput (operations a second) | 2,899 | 2,896 | -0.1% | -2.7 to -2.36 | **WORSE** |
| latency, 95th percentile (ms) | 0.342 | 0.345 | +0.9% | -0.00991 to 0.0159 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.517 | 0.518 | +0.1% | -0.0205 to 0.0218 | no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.205 | +0.6% | -0.00101 to 0.00338 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 486 | -5.1% | -105 to 52.5 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 399 | -4.1% | -78.8 to 44.8 | no difference beyond the noise |
| pages read into the cache (misses) | 721,790 | 715,451 | -0.9% | -171,954 to 159,276 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.176 | -1.8% | -0.0435 to 0.0372 | no difference beyond the noise |
| host CPU-seconds | 306 | 298 | -2.7% | -90.8 to 74.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.23 | 0.224 | -2.7% | -0.0682 to 0.0559 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | -0.128 to 7.46 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
