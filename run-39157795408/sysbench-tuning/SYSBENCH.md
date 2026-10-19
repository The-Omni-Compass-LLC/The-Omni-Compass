# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,938 | 2,940 | +0.1% | -2.23 to 5.81 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,951 | -0.0% | -5.04 to 2.75 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,951 | -0.0% | -5.04 to 2.75 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.354 | 0.338 | -4.6% | -0.0378 to 0.00509 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.549 | 0.527 | -4.1% | -0.0346 to -0.0101 | GAIN |
| latency, mean (ms) | 0.215 | 0.21 | -2.4% | -0.0102 to -1.46e-05 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 492 | -4.0% | -118 to 76.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 441 | -5.0% | -99.4 to 53.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,554 | 390,022 | +6.4% | -113,387 to 160,322 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.107 | -4.2% | -0.0108 to 0.0015 | EVEN, no difference beyond the noise |
| host CPU-seconds | 185 | 178 | -4.2% | -18.5 to 3.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.138 | 0.132 | -4.2% | -0.0137 to 0.00208 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9 |  | 4.03 to 14 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
