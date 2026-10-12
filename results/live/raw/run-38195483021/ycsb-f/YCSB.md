# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,582 | 5,565 | -0.3% | -73.7 to 38.5 | no difference beyond the noise |
| throughput (operations a second) | 5,601 | 5,584 | -0.3% | -72.9 to 39.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.45 | 0.455 | +1.0% | -0.0197 to 0.0291 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.685 | 0.695 | +1.5% | -0.0365 to 0.0565 | no difference beyond the noise |
| latency, mean (ms) | 0.259 | 0.261 | +0.8% | -0.0114 to 0.0157 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -14.8 to 2.88 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 414 | 409 | -1.1% | -11.6 to 2.37 | no difference beyond the noise |
| pages read into the cache (misses) | 455,571 | 466,323 | +2.4% | -11,283 to 32,788 | shown, not judged |
| host CPU busy (share of the run) | 0.309 | 0.318 | +2.8% | -0.0152 to 0.0327 | no difference beyond the noise |
| host CPU-seconds | 351 | 362 | +3.1% | -22.6 to 44.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.202 | 0.208 | +3.3% | -0.0149 to 0.0284 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
