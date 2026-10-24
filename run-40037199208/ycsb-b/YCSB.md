# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,913 | 2,910 | -0.1% | -7.53 to 1.62 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,917 | 2,914 | -0.1% | -6.62 to 1.23 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.204 | 0.206 | +1.1% | -0.0104 to 0.0151 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.39 | 0.392 | +0.7% | -0.016 to 0.0213 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.141 | 0.144 | +1.6% | -0.00633 to 0.011 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 488 | -4.7% | -106 to 58.2 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 421 | 401 | -4.6% | -89.8 to 51.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 748,011 | 732,717 | -2.0% | -263,333 to 232,745 | shown, not judged |
| host CPU busy (share of the run) | 0.166 | 0.169 | +2.1% | -0.107 to 0.114 | EVEN, no difference beyond the noise |
| host CPU-seconds | 305 | 309 | +1.1% | -245 to 251 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.229 | 0.231 | +1.1% | -0.183 to 0.188 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
