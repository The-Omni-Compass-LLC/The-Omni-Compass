# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,888 | -0.1% | -3.19 to -0.0189 | LOSS |
| throughput (operations a second) | 2,893 | 2,891 | -0.1% | -3.74 to 0.324 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.311 | 0.315 | +1.3% | -0.00496 to 0.013 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.469 | 0.47 | +0.1% | -0.0118 to 0.0132 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.191 | +0.4% | -7.51e-05 to 0.00151 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -5.44 to -0.85 | GAIN |
| bytes in the cache, mean (MB) | 418 | 417 | -0.2% | -7.52 to 5.76 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 695,218 | 697,457 | +0.3% | -81,534 to 86,012 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.211 | +10.9% | -0.0163 to 0.0579 | EVEN, no difference beyond the noise |
| host CPU-seconds | 332 | 376 | +13.2% | -35.8 to 124 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.249 | 0.282 | +13.2% | -0.027 to 0.0931 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | -0.128 to 7.46 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
