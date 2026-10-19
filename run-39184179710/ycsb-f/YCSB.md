# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,715 | 5,701 | -0.3% | -51.6 to 22.4 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,733 | 5,718 | -0.3% | -51.1 to 21.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.404 | 0.403 | -0.2% | -0.00939 to 0.00806 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.659 | 0.653 | -0.9% | -0.0284 to 0.0164 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.218 | 0.218 | -0.1% | -0.00417 to 0.00357 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -6.66 to -1.07 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.5% | -4.62 to 0.455 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 689,260 | 690,616 | +0.2% | -15,767 to 18,479 | shown, not judged |
| host CPU busy (share of the run) | 0.301 | 0.301 | +0.0% | -0.0372 to 0.0373 | EVEN, no difference beyond the noise |
| host CPU-seconds | 549 | 550 | +0.1% | -91.2 to 92.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.207 | 0.207 | +0.2% | -0.0356 to 0.0365 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
