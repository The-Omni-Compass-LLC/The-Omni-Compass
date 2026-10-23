# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,883 | -0.5% | -51.9 to 22.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,897 | -0.5% | -53.9 to 26.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.324 | 0.329 | +1.6% | -0.0147 to 0.0254 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.526 | 0.53 | +0.8% | -0.0768 to 0.0855 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.177 | 0.187 | +5.6% | -0.00308 to 0.0228 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.2% | -22.3 to -0.651 | GAIN |
| bytes in the cache, mean (MB) | 400 | 393 | -1.7% | -23.1 to 9.49 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 263,214 | 266,972 | +1.4% | -1,700 to 9,217 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.147 | +1.8% | -0.0916 to 0.0969 | EVEN, no difference beyond the noise |
| host CPU-seconds | 103 | 104 | +1.1% | -76.8 to 79.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.193 | 0.197 | +1.6% | -0.146 to 0.153 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
