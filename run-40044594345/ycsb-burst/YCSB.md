# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,877 | -0.0% | -5.56 to 3.07 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,885 | -0.0% | -3.54 to 2.28 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.456 | 0.46 | +0.9% | -0.000303 to 0.0083 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.638 | 0.646 | +1.3% | -0.0498 to 0.0658 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.219 | +1.5% | -0.00103 to 0.00746 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 500 | -2.4% | -22.2 to -1.98 | GAIN |
| bytes in the cache, mean (MB) | 402 | 393 | -2.2% | -20.7 to 2.94 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 268,572 | 266,937 | -0.6% | -29,058 to 25,788 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.186 | -5.6% | -0.055 to 0.033 | EVEN, no difference beyond the noise |
| host CPU-seconds | 138 | 128 | -6.8% | -45.7 to 26.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.259 | 0.241 | -6.8% | -0.0859 to 0.0506 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
