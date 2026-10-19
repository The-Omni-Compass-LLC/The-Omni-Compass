# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,876 | -0.2% | -21.1 to 9.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,887 | -0.2% | -19.5 to 8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.374 | 0.373 | -0.3% | -0.0204 to 0.0184 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.597 | 0.596 | -0.1% | -0.053 to 0.0523 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.23 | 0.228 | -0.8% | -0.015 to 0.0113 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -5.34 to -2.08 | GAIN |
| bytes in the cache, mean (MB) | 417 | 416 | -0.2% | -3.87 to 2.45 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 674,402 | 680,339 | +0.9% | -18,383 to 30,256 | shown, not judged |
| host CPU busy (share of the run) | 0.239 | 0.239 | +0.0% | -0.0543 to 0.0545 | EVEN, no difference beyond the noise |
| host CPU-seconds | 410 | 411 | +0.3% | -120 to 122 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.309 | 0.31 | +0.5% | -0.0898 to 0.093 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
