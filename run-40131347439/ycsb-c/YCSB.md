# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,881 | -0.0% | -6.14 to 4.49 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,885 | -0.0% | -5.31 to 3.68 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.324 | 0.324 | -0.1% | -0.00792 to 0.00726 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.508 | 0.507 | -0.3% | -0.0182 to 0.0156 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.196 | 0.199 | +1.3% | -0.00262 to 0.00785 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -20.6 to 10.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 419 | -0.0% | -21.3 to 21 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 680,001 | 695,688 | +2.3% | -5,747 to 37,121 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.231 | +12.5% | -0.0705 to 0.122 | EVEN, no difference beyond the noise |
| host CPU-seconds | 363 | 418 | +15.1% | -158 to 268 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.314 | +15.1% | -0.119 to 0.201 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
