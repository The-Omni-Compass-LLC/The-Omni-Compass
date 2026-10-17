# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,790 | 2,698 | -3.3% | -322 to 139 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,803 | 2,712 | -3.2% | -324 to 143 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.332 | 0.336 | +1.4% | -0.00784 to 0.0172 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.556 | 0.577 | +3.8% | -0.00347 to 0.0455 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.235 | 0.245 | +4.4% | 0.00148 to 0.0192 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.6% | -33.8 to 17.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 395 | 394 | -0.3% | -22.2 to 19.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 260,755 | 240,861 | -7.6% | -68,152 to 28,365 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.158 | -2.3% | -0.069 to 0.0615 | EVEN, no difference beyond the noise |
| host CPU-seconds | 118 | 115 | -3.2% | -57.9 to 50.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.23 | 0.231 | +0.4% | -0.0862 to 0.0881 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.67 |  | 4.23 to 7.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
