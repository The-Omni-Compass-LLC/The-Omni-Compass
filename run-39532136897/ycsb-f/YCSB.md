# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `4181e5728b93`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,775 | 5,766 | -0.2% | -25.2 to 7.74 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,789 | 5,781 | -0.1% | -23.6 to 6.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.289 | 0.294 | +1.6% | -0.00946 to 0.0188 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.527 | 0.533 | +1.1% | -0.0143 to 0.0263 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.147 | 0.148 | +0.7% | -0.00484 to 0.00685 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.1% | -6.73 to -4.91 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.7% | -3.55 to -2.21 | GAIN |
| pages read into the cache (misses) | 680,061 | 690,264 | +1.5% | -4,379 to 24,785 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.218 | -0.6% | -0.0449 to 0.0421 | EVEN, no difference beyond the noise |
| host CPU-seconds | 401 | 399 | -0.5% | -97.8 to 93.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.15 | 0.15 | -0.5% | -0.0368 to 0.0353 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
