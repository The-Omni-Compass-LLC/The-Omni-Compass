# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,903 | 2,902 | -0.0% | -6.14 to 3.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,908 | 2,907 | -0.0% | -6.03 to 3.96 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.301 | 0.301 | -0.1% | -0.014 to 0.0133 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.484 | 0.484 | +0.1% | -0.0478 to 0.0491 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.154 | 0.154 | +0.1% | -0.00294 to 0.00331 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -5.92 to -0.677 | GAIN |
| bytes in the cache, mean (MB) | 419 | 417 | -0.3% | -13.5 to 10.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 695,062 | 696,672 | +0.2% | -86,856 to 90,076 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.176 | +5.9% | -0.036 to 0.0557 | EVEN, no difference beyond the noise |
| host CPU-seconds | 301 | 322 | +7.0% | -77.2 to 119 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.226 | 0.242 | +7.0% | -0.0577 to 0.0892 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
