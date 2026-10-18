# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,849 | 2,851 | +0.1% | -3.19 to 6.68 | no difference beyond the noise |
| throughput (operations a second) | 2,859 | 2,860 | +0.0% | -2.57 to 4.39 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.468 | 0.456 | -2.6% | -0.043 to 0.0183 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.708 | 0.683 | -3.4% | -0.0797 to 0.031 | no difference beyond the noise |
| latency, mean (ms) | 0.239 | 0.236 | -1.2% | -0.0194 to 0.0135 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.1% | -5.68 to -5.68 | better |
| bytes in the cache, mean (MB) | 397 | 392 | -1.2% | -14.5 to 5.06 | no difference beyond the noise |
| pages read into the cache (misses) | 188,142 | 181,759 | -3.4% | -31,834 to 19,069 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.195 | -8.0% | -0.0701 to 0.0361 | no difference beyond the noise |
| host CPU-seconds | 97.1 | 87.7 | -9.7% | -38.1 to 19.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.276 | 0.249 | -9.7% | -0.109 to 0.0552 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
