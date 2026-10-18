# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,926 | 2,924 | -0.1% | -5.56 to 2.46 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,933 | 2,931 | -0.1% | -5.86 to 1.51 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.251 | 0.252 | +0.3% | -0.00507 to 0.0064 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.434 | 0.429 | -1.0% | -0.0115 to 0.00284 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.109 | 0.109 | -0.7% | -0.0089 to 0.00732 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -16.2 to 4.08 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 415 | -0.8% | -12.8 to 6.47 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 682,891 | 695,415 | +1.8% | -15,465 to 40,513 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.134 | -1.2% | -0.0713 to 0.068 | EVEN, no difference beyond the noise |
| host CPU-seconds | 246 | 242 | -1.9% | -149 to 140 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.184 | 0.181 | -2.0% | -0.112 to 0.105 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
