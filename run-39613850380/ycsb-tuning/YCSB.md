# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,878 | +0.0% | -7.56 to 7.76 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,887 | +0.0% | -6.1 to 6.84 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.35 | 0.348 | -0.7% | -0.0198 to 0.0151 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.536 | 0.539 | +0.6% | -0.0207 to 0.0267 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.214 | -0.9% | -0.00849 to 0.00478 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -1.9% | -24.9 to 5.22 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 411 | -1.5% | -16.3 to 3.37 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 677,346 | 689,251 | +1.8% | -6,197 to 30,007 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.236 | -6.0% | -0.03 to 5.85e-08 | EVEN, no difference beyond the noise |
| host CPU-seconds | 441 | 407 | -7.9% | -64.4 to -5.13 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.332 | 0.306 | -7.9% | -0.0493 to -0.00334 | GAIN |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
