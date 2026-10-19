# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,918 | 2,903 | -0.5% | -69.7 to 39.4 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,923 | 2,906 | -0.6% | -70.7 to 38.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.233 | 0.241 | +3.3% | -0.0168 to 0.0322 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.379 | 0.386 | +1.7% | -0.00307 to 0.0157 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.154 | 0.167 | +8.0% | -0.0302 to 0.0549 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.57 to -1.9 | GAIN |
| bytes in the cache, mean (MB) | 420 | 420 | -0.2% | -6.66 to 5.09 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 698,221 | 732,629 | +4.9% | -83,529 to 152,347 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.152 | -0.3% | -0.0625 to 0.0617 | EVEN, no difference beyond the noise |
| host CPU-seconds | 274 | 272 | -0.7% | -125 to 121 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.205 | 0.204 | -0.4% | -0.0936 to 0.0919 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
