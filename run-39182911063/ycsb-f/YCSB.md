# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `bc2eb38f4ca8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,818 | 5,812 | -0.1% | -19.8 to 8.22 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,829 | 5,824 | -0.1% | -20.1 to 9.95 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.223 | 0.224 | +0.7% | -0.00213 to 0.00546 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.416 | 0.427 | +2.6% | -0.0102 to 0.0322 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.112 | 0.112 | +0.1% | -0.00245 to 0.00261 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -4.71 to -3.27 | GAIN |
| bytes in the cache, mean (MB) | 418 | 417 | -0.3% | -2.19 to -0.312 | GAIN |
| pages read into the cache (misses) | 697,229 | 702,949 | +0.8% | -11,841 to 23,280 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.147 | -5.3% | -0.0499 to 0.0333 | EVEN, no difference beyond the noise |
| host CPU-seconds | 281 | 264 | -6.2% | -106 to 71.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.105 | 0.0986 | -6.2% | -0.0397 to 0.0266 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
