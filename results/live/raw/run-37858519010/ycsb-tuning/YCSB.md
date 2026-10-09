# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,840 | 2,839 | -0.0% | -34.2 to 33.4 | no difference beyond the noise |
| throughput (operations a second) | 2,849 | 2,848 | -0.1% | -35.8 to 32.7 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.383 | 0.385 | +0.7% | -0.0025 to 0.00784 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.579 | 0.57 | -1.6% | -0.028 to 0.00931 | no difference beyond the noise |
| latency, mean (ms) | 0.221 | 0.223 | +0.9% | -0.00354 to 0.00773 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 399 | -22.1% | -155 to -71.6 | better |
| bytes in the cache, mean (MB) | 415 | 327 | -21.2% | -121 to -54.8 | better |
| pages read into the cache (misses) | 454,820 | 570,978 | +25.5% | 63,355 to 168,961 | shown, not judged |
| host CPU busy (share of the run) | 0.283 | 0.28 | -1.0% | -0.0426 to 0.037 | no difference beyond the noise |
| host CPU-seconds | 341 | 335 | -1.7% | -70.3 to 58.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.389 | 0.383 | -1.8% | -0.0846 to 0.0709 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
