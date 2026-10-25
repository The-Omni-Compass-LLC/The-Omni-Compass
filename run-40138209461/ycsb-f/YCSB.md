# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `96ebf29137fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,838 | 5,833 | -0.1% | -10.6 to 1.41 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,847 | 5,842 | -0.1% | -10.5 to 0.358 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.169 | 0.167 | -1.2% | -0.0244 to 0.0204 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.398 | 0.383 | -3.7% | -0.06 to 0.0306 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0864 | 0.0857 | -0.9% | -0.00398 to 0.00251 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.5% | -19.1 to 3.63 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 414 | -1.4% | -15.1 to 3.76 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 696,666 | 704,012 | +1.1% | -24,756 to 39,447 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.131 | -2.3% | -0.0804 to 0.0743 | EVEN, no difference beyond the noise |
| host CPU-seconds | 245 | 238 | -2.9% | -171 to 157 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0914 | 0.0888 | -2.9% | -0.0639 to 0.0587 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
