# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,870 | 2,870 | -0.0% | -206 to 205 | no difference beyond the noise |
| throughput (operations a second) | 2,875 | 2,875 | -0.0% | -204 to 203 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.243 | 0.248 | +1.9% | 0.0018 to 0.00754 | **WORSE** |
| latency, 99th percentile (ms) | 0.378 | 0.382 | +1.1% | -0.00817 to 0.0168 | no difference beyond the noise |
| latency, mean (ms) | 0.181 | 0.196 | +8.5% | -0.018 to 0.0486 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 487 | -5.0% | -106 to 54.6 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 414 | 393 | -5.0% | -85.9 to 44.5 | no difference beyond the noise |
| pages read into the cache (misses) | 697,486 | 706,826 | +1.3% | -157,972 to 176,652 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.14 | -6.1% | -0.0744 to 0.0564 | no difference beyond the noise |
| host CPU-seconds | 269 | 250 | -7.0% | -154 to 117 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.204 | 0.19 | -7.0% | -0.111 to 0.0828 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
