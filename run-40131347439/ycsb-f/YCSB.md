# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,683 | 5,671 | -0.2% | -43.9 to 19.2 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,701 | 5,689 | -0.2% | -40.8 to 17.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.421 | 0.433 | +3.0% | -0.00846 to 0.0338 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.638 | 0.66 | +3.5% | -0.00423 to 0.0489 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.242 | 0.247 | +2.4% | -0.00759 to 0.0191 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -5.86 to -1.92 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.4% | -4.72 to 1.08 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 680,861 | 684,814 | +0.6% | -10,010 to 17,916 | shown, not judged |
| host CPU busy (share of the run) | 0.318 | 0.332 | +4.4% | -0.0139 to 0.0419 | EVEN, no difference beyond the noise |
| host CPU-seconds | 570 | 601 | +5.5% | -30 to 92.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.227 | +5.7% | -0.0118 to 0.0361 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
