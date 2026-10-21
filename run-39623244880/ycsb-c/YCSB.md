# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,908 | +0.1% | -12 to 16.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,912 | +0.1% | -9.4 to 12.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.188 | 0.187 | -0.7% | -0.0065 to 0.00384 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.357 | 0.357 | -0.1% | -0.0126 to 0.0119 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.146 | 0.141 | -3.8% | -0.0194 to 0.00835 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -9.07 to 2.93 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 416 | -0.6% | -12.7 to 7.79 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 714,025 | 675,732 | -5.4% | -140,308 to 63,722 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.156 | +8.0% | -0.0498 to 0.0729 | EVEN, no difference beyond the noise |
| host CPU-seconds | 258 | 282 | +9.2% | -103 to 151 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.194 | 0.211 | +9.1% | -0.0772 to 0.112 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
