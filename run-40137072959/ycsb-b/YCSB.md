# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,885 | -0.0% | -2.38 to 0.0613 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,888 | -0.0% | -2.71 to 0.665 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.342 | 0.346 | +1.2% | -0.00738 to 0.0154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.512 | 0.515 | +0.7% | -0.0024 to 0.00907 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.202 | +1.1% | -0.00361 to 0.00803 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -16.4 to 4.49 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 412 | -1.6% | -8.7 to -5.04 | GAIN |
| pages read into the cache (misses) | 734,887 | 694,868 | -5.4% | -82,139 to 2,101 | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.18 | -11.2% | -0.0746 to 0.0293 | EVEN, no difference beyond the noise |
| host CPU-seconds | 352 | 303 | -13.9% | -160 to 61.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.228 | -13.9% | -0.12 to 0.0464 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
