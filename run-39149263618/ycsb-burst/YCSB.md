# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | +0.0% | -7.4 to 7.65 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,895 | 2,895 | -0.0% | -4.1 to 2.87 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.437 | 0.44 | +0.6% | -0.0246 to 0.0299 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.637 | 0.63 | -1.1% | -0.115 to 0.101 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.225 | +1.3% | -0.00158 to 0.00721 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 480 | -6.3% | -84.3 to 20 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 398 | 379 | -4.7% | -75.7 to 38.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 266,183 | 290,018 | +9.0% | -38,111 to 85,781 | shown, not judged |
| host CPU busy (share of the run) | 0.157 | 0.206 | +31.3% | -0.0126 to 0.111 | EVEN, no difference beyond the noise |
| host CPU-seconds | 104 | 144 | +37.7% | -8.43 to 87.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.196 | 0.27 | +37.7% | -0.0157 to 0.164 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
