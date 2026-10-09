# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,862 | 2,862 | -0.0% | -3.31 to 2.15 | no difference beyond the noise |
| throughput (operations a second) | 2,866 | 2,866 | -0.0% | -3.04 to 1.86 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.387 | 0.39 | +0.6% | -0.00146 to 0.00613 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.505 | 0.508 | +0.5% | -0.0139 to 0.0192 | no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.207 | +2.3% | 0.00335 to 0.00574 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 389 | -24.0% | -124 to -122 | better |
| bytes in the cache, mean (MB) | 415 | 320 | -22.8% | -101 to -88.5 | better |
| pages read into the cache (misses) | 454,017 | 588,209 | +29.6% | 102,327 to 166,057 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.212 | +7.6% | -0.0557 to 0.0855 | no difference beyond the noise |
| host CPU-seconds | 224 | 244 | +8.8% | -81.9 to 121 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.254 | 0.276 | +8.8% | -0.0927 to 0.137 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
