# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,859 | 2,858 | -0.0% | -5.18 to 2.9 | no difference beyond the noise |
| throughput (operations a second) | 2,866 | 2,865 | -0.0% | -5.09 to 2.28 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.453 | 0.455 | +0.4% | -0.0129 to 0.0162 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.599 | 0.598 | -0.3% | -0.0144 to 0.0111 | no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.209 | +0.7% | -0.0099 to 0.0128 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.5% | -21.6 to 5.79 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 415 | 410 | -1.3% | -21.4 to 10.7 | no difference beyond the noise |
| pages read into the cache (misses) | 470,117 | 472,905 | +0.6% | -195,373 to 200,949 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.193 | -3.5% | -0.0383 to 0.0244 | no difference beyond the noise |
| host CPU-seconds | 229 | 219 | -4.6% | -54.6 to 33.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.26 | 0.248 | -4.6% | -0.0622 to 0.0385 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
