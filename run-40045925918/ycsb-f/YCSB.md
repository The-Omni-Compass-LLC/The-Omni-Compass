# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,686 | 5,674 | -0.2% | -44 to 20.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,703 | 5,691 | -0.2% | -43.9 to 20.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.429 | 0.428 | -0.4% | -0.00792 to 0.00459 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.641 | 0.638 | -0.4% | -0.0192 to 0.0139 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.247 | 0.246 | -0.6% | -0.00245 to -0.000646 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -6.06 to -1.27 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.4% | -4.77 to 1.67 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 685,858 | 684,401 | -0.2% | -19,787 to 16,873 | shown, not judged |
| host CPU busy (share of the run) | 0.33 | 0.325 | -1.6% | -0.0409 to 0.0303 | EVEN, no difference beyond the noise |
| host CPU-seconds | 598 | 585 | -2.2% | -101 to 74.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.225 | 0.221 | -2.1% | -0.0371 to 0.0277 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
