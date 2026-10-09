# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,769 | 5,760 | -0.1% | -26.1 to 8.95 | no difference beyond the noise |
| throughput (operations a second) | 5,783 | 5,772 | -0.2% | -32.6 to 12 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.264 | 0.262 | -0.6% | -0.00454 to 0.0012 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.471 | 0.454 | -3.5% | -0.0516 to 0.0189 | no difference beyond the noise |
| latency, mean (ms) | 0.12 | 0.12 | +0.2% | -0.00704 to 0.00757 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 327 | -36.1% | -186 to -183 | better |
| bytes in the cache, mean (MB) | 417 | 266 | -36.2% | -152 to -150 | better |
| pages read into the cache (misses) | 476,953 | 686,067 | +43.8% | 182,801 to 235,428 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.169 | +2.1% | -0.0616 to 0.0685 | no difference beyond the noise |
| host CPU-seconds | 199 | 203 | +2.0% | -90.4 to 98.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.112 | 0.114 | +2.0% | -0.0507 to 0.0553 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
