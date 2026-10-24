# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,933 | 2,931 | -0.1% | -9.44 to 4.95 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,935 | -0.1% | -7.24 to 3.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.156 | 0.169 | +8.6% | 0.00574 to 0.0209 | LOSS |
| latency, 99th percentile (ms) | 0.375 | 0.391 | +4.2% | -0.000875 to 0.0322 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0818 | 0.0835 | +2.0% | -0.00402 to 0.00734 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -5.91 to -1.48 | GAIN |
| bytes in the cache, mean (MB) | 419 | 418 | -0.3% | -4.65 to 2.26 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 693,867 | 689,096 | -0.7% | -38,902 to 29,359 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.114 | +6.9% | -0.0849 to 0.0996 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 205 | +7.2% | -170 to 198 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.143 | 0.154 | +7.2% | -0.127 to 0.148 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
