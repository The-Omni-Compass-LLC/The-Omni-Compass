# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,919 | 2,918 | -0.0% | -2.72 to 0.12 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,923 | 2,922 | -0.0% | -2.77 to 0.435 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.302 | 0.314 | +3.9% | -0.0174 to 0.0408 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.49 | 0.497 | +1.5% | -0.0366 to 0.0512 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.117 | 0.119 | +1.9% | -0.000499 to 0.00503 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.2% | -17.8 to -4.88 | GAIN |
| bytes in the cache, mean (MB) | 406 | 398 | -2.1% | -26.8 to 10 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 265,633 | 265,193 | -0.2% | -53,029 to 52,149 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.117 | +5.4% | -0.0106 to 0.0226 | EVEN, no difference beyond the noise |
| host CPU-seconds | 79.4 | 83.9 | +5.7% | -8.39 to 17.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.149 | 0.157 | +5.7% | -0.0156 to 0.0326 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
