# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,934 | -0.0% | -1.51 to -0.717 | LOSS |
| throughput (operations a second) | 2,938 | 2,937 | -0.0% | -2.29 to 0.394 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.252 | 0.256 | +1.5% | -0.015 to 0.0223 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.411 | 0.411 | -0.1% | -0.0377 to 0.037 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0813 | 0.0814 | +0.2% | -0.00484 to 0.0051 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.7% | -9.36 to -8.36 | GAIN |
| bytes in the cache, mean (MB) | 405 | 401 | -1.1% | -23.2 to 14.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 264,600 | 269,228 | +1.7% | -1,978 to 11,234 | shown, not judged |
| host CPU busy (share of the run) | 0.0881 | 0.119 | +35.2% | -0.0863 to 0.148 | EVEN, no difference beyond the noise |
| host CPU-seconds | 64.6 | 89.7 | +38.8% | -70.7 to 121 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.121 | 0.167 | +38.8% | -0.132 to 0.226 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
