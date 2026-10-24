# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,874 | 2,876 | +0.1% | -8.67 to 13.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,887 | +0.1% | -9.59 to 13.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.373 | 0.377 | +1.0% | -0.00781 to 0.0151 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.638 | 0.639 | +0.1% | -0.00968 to 0.011 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.221 | 0.223 | +0.6% | -0.00817 to 0.0109 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.3% | -20.3 to 6.65 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 413 | -0.9% | -16 to 8.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 676,658 | 689,756 | +1.9% | -3,204 to 29,399 | shown, not judged |
| host CPU busy (share of the run) | 0.246 | 0.256 | +3.8% | -0.0507 to 0.0692 | EVEN, no difference beyond the noise |
| host CPU-seconds | 431 | 449 | +4.2% | -116 to 152 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.325 | 0.338 | +4.1% | -0.0876 to 0.114 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
