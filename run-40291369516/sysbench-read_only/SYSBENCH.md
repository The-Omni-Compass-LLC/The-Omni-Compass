# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.2% | -4.56 to 3.54 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.2% | -4.58 to 3.52 | EVEN, no difference beyond the noise |
| queries a second | 4,727 | 4,718 | -0.2% | -73.2 to 56.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.2 | 4.15 | -1.2% | -0.158 to 0.0576 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.09 | 5.95 | -2.4% | -0.298 to 0.00881 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.18 | 3.17 | -0.3% | -0.0272 to 0.00542 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 568 | +11.0% | 3.09 to 110 | power given |
| pages holding data, mean (MB) | 462 | 518 | +12.3% | 19 to 94.4 | power given |
| pages read from disk into the pool (misses) | 657,161 | 482,971 | -26.5% | -248,602 to -99,778 | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.188 | -0.4% | -0.00245 to 0.000848 | EVEN, no difference beyond the noise |
| host CPU-seconds | 312 | 311 | -0.4% | -3.46 to 0.904 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.31 | 2.31 | -0.2% | -0.0232 to 0.0124 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 11.8 to 17.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
