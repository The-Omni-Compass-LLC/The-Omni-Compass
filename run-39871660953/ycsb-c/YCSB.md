# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,943 | 2,941 | -0.1% | -4.28 to 0.822 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,945 | 2,943 | -0.1% | -4.32 to 0.768 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.083 | 0.0827 | -0.4% | -0.00413 to 0.00346 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.267 | 0.265 | -0.9% | -0.0075 to 0.00284 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0547 | 0.0545 | -0.4% | -0.00207 to 0.00162 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -4.93 to -1.08 | GAIN |
| bytes in the cache, mean (MB) | 425 | 419 | -1.3% | -15.5 to 4.47 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 727,262 | 707,392 | -2.7% | -74,798 to 35,057 | shown, not judged |
| host CPU busy (share of the run) | 0.0633 | 0.0776 | +22.6% | -0.0177 to 0.0463 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 141 | +24.5% | -35.4 to 90.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0846 | 0.105 | +24.5% | -0.0263 to 0.0677 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
