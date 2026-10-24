# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,902 | -0.1% | -7.66 to 3.2 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,911 | -0.1% | -5.37 to 1.25 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.22 | 0.223 | +1.2% | -0.011 to 0.0163 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.422 | 0.425 | +0.8% | -0.0411 to 0.0478 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.166 | 0.167 | +0.8% | -0.0035 to 0.00605 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -7.02 to -1.35 | GAIN |
| bytes in the cache, mean (MB) | 418 | 416 | -0.5% | -3.38 to -0.844 | GAIN |
| pages read into the cache (misses) | 675,963 | 684,895 | +1.3% | -14,214 to 32,077 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.182 | -2.8% | -0.0519 to 0.0414 | EVEN, no difference beyond the noise |
| host CPU-seconds | 334 | 321 | -3.9% | -115 to 89.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.25 | 0.241 | -3.8% | -0.0867 to 0.0676 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
