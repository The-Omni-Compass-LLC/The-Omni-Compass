# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,882 | -0.1% | -6.54 to 1.83 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,887 | -0.1% | -4.83 to 0.945 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.348 | 0.347 | -0.3% | -0.0184 to 0.0164 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.523 | 0.524 | +0.2% | -0.0365 to 0.0385 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.201 | +0.1% | -0.00554 to 0.00594 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -5.93 to -0.456 | GAIN |
| bytes in the cache, mean (MB) | 418 | 417 | -0.2% | -13.6 to 11.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 699,387 | 712,642 | +1.9% | -139,259 to 165,769 | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.193 | -2.3% | -0.0754 to 0.0662 | EVEN, no difference beyond the noise |
| host CPU-seconds | 341 | 332 | -2.7% | -158 to 140 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.257 | 0.25 | -2.7% | -0.119 to 0.105 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
