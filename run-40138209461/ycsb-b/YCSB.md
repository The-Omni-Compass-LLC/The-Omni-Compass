# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `96ebf29137fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,878 | -0.1% | -9.44 to 3.85 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,886 | -0.1% | -8.82 to 2.73 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.347 | 0.36 | +3.7% | -0.0415 to 0.0675 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.626 | 0.625 | -0.1% | -0.0168 to 0.0155 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.202 | +1.1% | -0.00637 to 0.0108 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.5% | -4.94 to -0.244 | GAIN |
| bytes in the cache, mean (MB) | 417 | 416 | -0.2% | -3.64 to 2.26 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 720,790 | 713,789 | -1.0% | -49,108 to 35,107 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.192 | -3.7% | -0.0965 to 0.0819 | EVEN, no difference beyond the noise |
| host CPU-seconds | 351 | 330 | -5.8% | -217 to 176 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.249 | -5.8% | -0.164 to 0.133 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
