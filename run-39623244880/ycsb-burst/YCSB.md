# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,882 | -0.0% | -3.69 to 2.87 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | -0.0% | -3.58 to 3.21 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.421 | 0.422 | +0.3% | -0.00384 to 0.0065 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.571 | 0.57 | -0.1% | -0.0344 to 0.0331 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.214 | +1.9% | -0.00503 to 0.013 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 499 | -2.6% | -26.2 to -0.331 | GAIN |
| bytes in the cache, mean (MB) | 400 | 394 | -1.6% | -20.2 to 7.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 272,631 | 273,811 | +0.4% | -12,024 to 14,384 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.232 | +12.6% | -0.102 to 0.154 | EVEN, no difference beyond the noise |
| host CPU-seconds | 147 | 169 | +15.3% | -93.9 to 139 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.276 | 0.318 | +15.3% | -0.177 to 0.261 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
