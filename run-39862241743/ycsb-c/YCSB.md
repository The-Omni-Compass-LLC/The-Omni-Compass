# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,941 | 2,937 | -0.2% | -9.42 to 0.531 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,943 | 2,938 | -0.1% | -8.83 to 0.233 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.086 | 0.093 | +8.1% | -0.00791 to 0.0219 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.282 | 0.286 | +1.5% | -0.0464 to 0.0551 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0555 | 0.0594 | +7.0% | -0.00253 to 0.0103 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 469 | -8.3% | -126 to 41.4 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 387 | -7.5% | -102 to 39.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 651,352 | 760,032 | +16.7% | -120,158 to 337,517 | shown, not judged |
| host CPU busy (share of the run) | 0.0791 | 0.0952 | +20.4% | -0.0131 to 0.0453 | EVEN, no difference beyond the noise |
| host CPU-seconds | 144 | 175 | +21.6% | -25.9 to 88 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.107 | 0.131 | +21.6% | -0.0194 to 0.0658 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | -1.46 to 6.13 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
