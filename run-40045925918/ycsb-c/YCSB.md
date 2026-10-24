# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,882 | -0.2% | -8.95 to 0.104 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,887 | -0.1% | -8.22 to -0.0629 | LOSS |
| latency, 95th percentile (ms) | 0.31 | 0.316 | +2.0% | 0.00116 to 0.0115 | LOSS |
| latency, 99th percentile (ms) | 0.508 | 0.515 | +1.3% | -0.0192 to 0.0325 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.192 | 0.196 | +2.1% | -0.000185 to 0.00814 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 490 | -4.2% | -107 to 63.2 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 406 | -3.1% | -79.2 to 53.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 698,407 | 747,594 | +7.0% | -134,891 to 233,265 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.194 | -4.4% | -0.0274 to 0.00976 | EVEN, no difference beyond the noise |
| host CPU-seconds | 360 | 338 | -6.0% | -66.1 to 23.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.27 | 0.254 | -5.9% | -0.0494 to 0.0173 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
