# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,894 | -0.1% | -3.25 to -1.08 | **WORSE** |
| throughput (operations a second) | 2,900 | 2,898 | -0.1% | -3.22 to -0.829 | **WORSE** |
| latency, 95th percentile (ms) | 0.33 | 0.337 | +2.1% | -0.00811 to 0.0221 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.489 | 0.496 | +1.5% | -0.00207 to 0.0167 | no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.202 | +0.3% | -0.00752 to 0.0089 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 469 | -8.3% | -125 to 39.6 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 386 | -7.5% | -95.9 to 33 | no difference beyond the noise |
| pages read into the cache (misses) | 690,302 | 764,770 | +10.8% | -99,700 to 248,636 | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.205 | +12.9% | -0.00747 to 0.0544 | no difference beyond the noise |
| host CPU-seconds | 308 | 357 | +16.0% | -12.5 to 111 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.268 | +16.0% | -0.00934 to 0.0832 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
