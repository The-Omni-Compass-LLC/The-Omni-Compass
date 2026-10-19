# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,891 | -0.0% | -2.79 to 1.86 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,897 | -0.0% | -2.56 to 1.86 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.428 | 0.421 | -1.6% | -0.012 to -0.00203 | GAIN |
| latency, 99th percentile (ms) | 0.573 | 0.565 | -1.3% | -0.0204 to 0.00508 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.218 | 0.215 | -1.5% | -0.0056 to -0.000856 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 495 | -3.2% | -60.2 to 27 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 402 | 394 | -2.0% | -57.4 to 41.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 252,647 | 267,748 | +6.0% | 8,806 to 21,396 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.174 | -2.8% | -0.113 to 0.103 | EVEN, no difference beyond the noise |
| host CPU-seconds | 123 | 119 | -3.4% | -92.7 to 84.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.223 | -3.4% | -0.174 to 0.159 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | -0.128 to 7.46 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
