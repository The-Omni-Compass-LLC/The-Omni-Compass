# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,665 | 5,673 | +0.2% | -40.6 to 57.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,683 | 5,691 | +0.1% | -40.1 to 55.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.437 | 0.436 | -0.4% | -0.0111 to 0.00774 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.673 | 0.668 | -0.7% | -0.0226 to 0.0133 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.25 | 0.249 | -0.4% | -0.00878 to 0.00691 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.3% | -20.5 to 6.9 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 412 | -1.0% | -13.6 to 5.38 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 682,202 | 692,171 | +1.5% | -3,868 to 23,807 | shown, not judged |
| host CPU busy (share of the run) | 0.333 | 0.329 | -1.3% | -0.0186 to 0.0103 | EVEN, no difference beyond the noise |
| host CPU-seconds | 604 | 593 | -1.9% | -47.2 to 24.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.228 | 0.224 | -2.1% | -0.0177 to 0.00823 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
