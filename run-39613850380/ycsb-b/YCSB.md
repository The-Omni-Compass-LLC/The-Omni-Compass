# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,885 | -0.1% | -3.49 to -0.401 | LOSS |
| throughput (operations a second) | 2,891 | 2,890 | -0.1% | -2.54 to -0.829 | LOSS |
| latency, 95th percentile (ms) | 0.327 | 0.33 | +0.8% | -0.0117 to 0.017 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.491 | 0.496 | +1.2% | -0.0179 to 0.0293 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.196 | -0.3% | -0.00409 to 0.00274 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -21 to 9.14 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 413 | -0.9% | -19.8 to 12.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 704,718 | 713,234 | +1.2% | -83,828 to 100,860 | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.18 | -9.3% | -0.0715 to 0.0348 | EVEN, no difference beyond the noise |
| host CPU-seconds | 345 | 306 | -11.3% | -155 to 76.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.259 | 0.23 | -11.2% | -0.116 to 0.0579 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
