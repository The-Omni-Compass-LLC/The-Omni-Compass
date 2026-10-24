# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,935 | -0.0% | -3.3 to 2.79 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,938 | -0.0% | -4.29 to 3.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.234 | 0.239 | +2.3% | -0.00226 to 0.0129 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.406 | 0.415 | +2.1% | -0.0321 to 0.0488 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.08 | 0.0813 | +1.6% | -0.000744 to 0.00337 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.5% | -12.7 to -2.49 | GAIN |
| bytes in the cache, mean (MB) | 408 | 401 | -1.6% | -19.1 to 6.36 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 263,170 | 275,392 | +4.6% | -5,516 to 29,961 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.0824 | -25.3% | -0.171 to 0.115 | EVEN, no difference beyond the noise |
| host CPU-seconds | 82.4 | 59.5 | -27.9% | -139 to 92.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.154 | 0.111 | -27.9% | -0.259 to 0.173 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
