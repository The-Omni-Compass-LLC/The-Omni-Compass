# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,896 | -0.0% | -4.73 to 2.11 | no difference beyond the noise |
| throughput (operations a second) | 2,901 | 2,900 | -0.0% | -4.55 to 1.86 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.31 | 0.31 | +0.1% | -0.018 to 0.0186 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.487 | 0.487 | +0.1% | -0.00346 to 0.00413 | no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.195 | +0.2% | -0.0105 to 0.0112 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 486 | -5.0% | -125 to 73.3 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 400 | -4.4% | -87.5 to 50.5 | no difference beyond the noise |
| pages read into the cache (misses) | 702,592 | 731,599 | +4.1% | -172,524 to 230,537 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.17 | +7.1% | -0.0187 to 0.0413 | no difference beyond the noise |
| host CPU-seconds | 266 | 289 | +8.6% | -34.7 to 80.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.2 | 0.217 | +8.6% | -0.026 to 0.0603 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
