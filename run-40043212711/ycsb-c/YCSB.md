# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,888 | -0.0% | -3.88 to 1.45 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,892 | -0.0% | -3.88 to 1.53 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.302 | 0.306 | +1.3% | 0.00152 to 0.00648 | LOSS |
| latency, 99th percentile (ms) | 0.471 | 0.463 | -1.7% | -0.0218 to 0.00583 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.189 | -0.5% | -0.0021 to 0.000357 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 478 | -6.7% | -108 to 40 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 396 | -5.1% | -79.6 to 36.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 650,187 | 796,726 | +22.5% | 74,537 to 218,540 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.179 | -12.2% | -0.0809 to 0.031 | EVEN, no difference beyond the noise |
| host CPU-seconds | 363 | 309 | -14.9% | -175 to 66.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.272 | 0.232 | -14.9% | -0.131 to 0.0499 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | -0.484 to 4.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
