# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,883 | -0.1% | -2.57 to -1.26 | LOSS |
| throughput (operations a second) | 2,890 | 2,888 | -0.1% | -2.29 to -1.33 | LOSS |
| latency, 95th percentile (ms) | 0.338 | 0.34 | +0.6% | -0.000484 to 0.00448 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.526 | 0.525 | -0.2% | -0.00597 to 0.00397 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.2 | +0.2% | -0.00353 to 0.00426 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.1% | -15.2 to 3.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 416 | -0.5% | -7.94 to 4.11 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 698,860 | 717,724 | +2.7% | -110,863 to 148,590 | shown, not judged |
| host CPU busy (share of the run) | 0.217 | 0.203 | -6.8% | -0.0653 to 0.0359 | EVEN, no difference beyond the noise |
| host CPU-seconds | 386 | 353 | -8.5% | -149 to 83.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.29 | 0.266 | -8.5% | -0.112 to 0.0624 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
