# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,911 | 2,908 | -0.1% | -11.9 to 4.16 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,917 | 2,914 | -0.1% | -11 to 4.19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.24 | 0.243 | +1.5% | -0.0199 to 0.0273 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.481 | 0.489 | +1.7% | -0.0364 to 0.0531 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.129 | 0.133 | +2.8% | -0.000925 to 0.0081 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.4% | -16 to 1.92 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 415 | -1.0% | -12.2 to 3.94 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 683,485 | 690,548 | +1.0% | -14,233 to 28,359 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.197 | +22.5% | 0.0117 to 0.0607 | power given |
| host CPU-seconds | 286 | 365 | +27.6% | 25.1 to 133 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.214 | 0.274 | +27.7% | 0.0185 to 0.1 | power given |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
