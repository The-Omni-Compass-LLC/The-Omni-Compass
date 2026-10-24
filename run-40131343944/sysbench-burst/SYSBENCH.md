# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 284 | -2.0% | -22.8 to 11.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.1% | -5.91 to 5.29 | EVEN, no difference beyond the noise |
| queries a second | 4,726 | 4,721 | -0.1% | -94.6 to 84.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.06 | 5.1 | +25.5% | -3.28 to 5.36 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 28.7 | 128 | +345.3% | -30 to 228 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.98 | 6.55 | +119.9% | -0.909 to 8.05 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 478 | -6.6% | -86.9 to 19.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 432 | -3.4% | -70.1 to 39.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 246,297 | 247,730 | +0.6% | -20,566 to 23,433 | shown, not judged |
| host CPU busy (share of the run) | 0.162 | 0.164 | +1.2% | -0.00458 to 0.0086 | EVEN, no difference beyond the noise |
| host CPU-seconds | 96.9 | 98.1 | +1.3% | -2.54 to 5.06 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.19 | 2.27 | +3.4% | -0.0429 to 0.19 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 5.23 to 8.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
