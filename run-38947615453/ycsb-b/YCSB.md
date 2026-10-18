# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,897 | -0.1% | -4.22 to 0.879 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,902 | 2,900 | -0.1% | -4.05 to 0.785 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.321 | 0.321 | -0.1% | -0.0147 to 0.014 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.458 | 0.461 | +0.7% | -0.00942 to 0.0161 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.195 | 0.197 | +1.4% | -0.00195 to 0.00748 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 486 | -5.2% | -107 to 54.3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 399 | -4.8% | -82.4 to 41.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 699,811 | 723,858 | +3.4% | -106,329 to 154,421 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.17 | -2.6% | -0.103 to 0.0933 | EVEN, no difference beyond the noise |
| host CPU-seconds | 297 | 288 | -3.0% | -209 to 191 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.223 | 0.216 | -3.0% | -0.157 to 0.143 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
