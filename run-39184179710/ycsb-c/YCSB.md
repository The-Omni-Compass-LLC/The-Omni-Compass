# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,936 | 2,934 | -0.1% | -7.64 to 2.74 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,936 | -0.1% | -7.83 to 2.92 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.203 | 0.198 | -2.5% | -0.00748 to -0.00252 | GAIN |
| latency, 99th percentile (ms) | 0.34 | 0.325 | -4.2% | -0.0374 to 0.00875 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0777 | 0.0776 | -0.2% | -0.00411 to 0.00388 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -3.52 to -0.879 | GAIN |
| bytes in the cache, mean (MB) | 421 | 420 | -0.2% | -13.5 to 11.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 720,420 | 729,810 | +1.3% | -102,388 to 121,168 | shown, not judged |
| host CPU busy (share of the run) | 0.0913 | 0.0857 | -6.1% | -0.107 to 0.0962 | EVEN, no difference beyond the noise |
| host CPU-seconds | 166 | 154 | -7.1% | -214 to 190 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.124 | 0.115 | -7.1% | -0.159 to 0.142 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
