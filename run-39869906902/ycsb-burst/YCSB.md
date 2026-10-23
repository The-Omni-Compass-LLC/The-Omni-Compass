# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,937 | -0.1% | -5.9 to 1.34 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,942 | 2,940 | -0.1% | -5.59 to 1.32 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.24 | 0.246 | +2.4% | -0.0103 to 0.0216 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.396 | 0.41 | +3.5% | -0.0102 to 0.0375 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0759 | 0.0773 | +1.9% | -0.00477 to 0.0077 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.7% | -9.61 to -7.87 | GAIN |
| bytes in the cache, mean (MB) | 407 | 396 | -2.6% | -22.8 to 1.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 262,150 | 268,127 | +2.3% | -27,909 to 39,864 | shown, not judged |
| host CPU busy (share of the run) | 0.0935 | 0.0856 | -8.5% | -0.134 to 0.118 | EVEN, no difference beyond the noise |
| host CPU-seconds | 68.7 | 62.3 | -9.2% | -106 to 93.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.128 | 0.116 | -9.2% | -0.197 to 0.174 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
