# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,683 | 5,681 | -0.0% | -21.4 to 18.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,702 | 5,700 | -0.0% | -22.3 to 19.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.427 | 0.427 | +0.0% | -0.00248 to 0.00248 | EVEN, the same |
| latency, 99th percentile (ms) | 0.685 | 0.685 | +0.0% | -0.0155 to 0.0155 | EVEN, the same |
| latency, mean (ms) | 0.242 | 0.242 | -0.1% | -0.0013 to 0.0008 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.4% | -20.4 to 6.6 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 412 | -1.1% | -16.3 to 7.25 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 682,239 | 685,989 | +0.5% | -9,244 to 16,743 | shown, not judged |
| host CPU busy (share of the run) | 0.319 | 0.318 | -0.3% | -0.0104 to 0.00876 | EVEN, no difference beyond the noise |
| host CPU-seconds | 576 | 574 | -0.3% | -27.4 to 23.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.217 | 0.216 | -0.4% | -0.0108 to 0.00917 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
