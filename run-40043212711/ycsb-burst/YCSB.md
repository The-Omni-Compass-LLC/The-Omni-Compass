# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,877 | -0.1% | -7.11 to 1.29 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,886 | -0.1% | -5.24 to 1.91 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.503 | 0.507 | +0.7% | -0.00384 to 0.0105 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.652 | 0.668 | +2.5% | -0.0185 to 0.0505 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.224 | +0.7% | 0.000728 to 0.00237 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.2% | -18.8 to -3.34 | GAIN |
| bytes in the cache, mean (MB) | 397 | 397 | -0.0% | -13.8 to 13.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 260,515 | 271,870 | +4.4% | -1,269 to 23,979 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.191 | -8.9% | -0.0722 to 0.0348 | EVEN, no difference beyond the noise |
| host CPU-seconds | 149 | 132 | -11.6% | -67.6 to 33 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.281 | 0.249 | -11.5% | -0.127 to 0.062 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
