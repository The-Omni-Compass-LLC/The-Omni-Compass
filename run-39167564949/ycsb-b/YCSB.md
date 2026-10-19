# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,893 | -0.1% | -5.85 to 1.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,896 | -0.1% | -6.07 to 1.89 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.353 | 0.357 | +1.1% | -0.0134 to 0.0214 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.497 | 0.497 | +0.0% | -0.0215 to 0.0215 | EVEN, the same |
| latency, mean (ms) | 0.206 | 0.206 | +0.1% | -0.00328 to 0.00382 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -5.59 to -0.351 | GAIN |
| bytes in the cache, mean (MB) | 416 | 415 | -0.2% | -10.6 to 8.72 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 699,414 | 730,461 | +4.4% | -187,884 to 249,976 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.191 | -5.9% | -0.0609 to 0.0369 | EVEN, no difference beyond the noise |
| host CPU-seconds | 352 | 327 | -7.3% | -129 to 77.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.245 | -7.3% | -0.0968 to 0.0584 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
