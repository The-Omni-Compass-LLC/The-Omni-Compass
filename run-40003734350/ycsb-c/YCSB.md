# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,884 | -0.1% | -5.19 to 1.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,888 | -0.1% | -4.09 to -0.36 | LOSS |
| latency, 95th percentile (ms) | 0.312 | 0.309 | -0.9% | -0.0282 to 0.0228 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.506 | 0.509 | +0.5% | -0.0276 to 0.0323 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.193 | +1.7% | -0.00486 to 0.0114 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.1% | -20.1 to 9.23 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 416 | -0.5% | -17.2 to 13.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 684,663 | 710,310 | +3.7% | -108,498 to 159,792 | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.207 | -3.0% | -0.132 to 0.119 | EVEN, no difference beyond the noise |
| host CPU-seconds | 387 | 369 | -4.6% | -301 to 266 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.291 | 0.278 | -4.6% | -0.227 to 0.2 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
