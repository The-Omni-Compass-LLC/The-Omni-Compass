# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,880 | -0.0% | -3.54 to 3.09 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | -0.0% | -3.65 to 3.11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.432 | 0.433 | +0.2% | -0.0189 to 0.0209 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.592 | 0.599 | +1.1% | -0.0157 to 0.0291 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.213 | 0.214 | +0.3% | -0.00534 to 0.00676 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.5% | -8.49 to -6.5 | GAIN |
| bytes in the cache, mean (MB) | 398 | 400 | +0.4% | -11.5 to 14.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 263,638 | 271,026 | +2.8% | -14,595 to 29,371 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.19 | -13.9% | -0.101 to 0.0396 | EVEN, no difference beyond the noise |
| host CPU-seconds | 159 | 131 | -17.7% | -92.6 to 36.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.299 | 0.246 | -17.7% | -0.174 to 0.068 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
