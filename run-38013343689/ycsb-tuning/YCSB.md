# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,904 | -0.1% | -5.11 to 1.2 | no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,913 | -0.1% | -6.32 to 2.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.316 | 0.319 | +1.1% | -0.0108 to 0.0175 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.54 | 0.549 | +1.8% | -0.00284 to 0.0222 | no difference beyond the noise |
| latency, mean (ms) | 0.149 | 0.148 | -0.1% | -0.00141 to 0.00123 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 467 | -8.9% | -120 to 29.1 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 383 | -8.4% | -91.8 to 22 | no difference beyond the noise |
| pages read into the cache (misses) | 682,918 | 738,387 | +8.1% | -55,427 to 166,365 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.206 | +6.5% | -0.0554 to 0.0806 | no difference beyond the noise |
| host CPU-seconds | 355 | 385 | +8.3% | -130 to 189 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.267 | 0.289 | +8.3% | -0.0978 to 0.142 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
