# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.3% | -0.768 to 2.76 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.3% | -0.773 to 2.74 | EVEN, no difference beyond the noise |
| queries a second | 4,703 | 4,719 | +0.3% | -12.4 to 43.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.25 | 4.18 | -1.8% | -0.0785 to -0.0735 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.67 | -2.4% | -0.289 to 0.0127 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.27 | 3.25 | -0.8% | -0.0781 to 0.0281 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 558 | +9.0% | -51 to 143 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 501 | +8.4% | -19.7 to 97.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 652,231 | 529,367 | -18.8% | -343,379 to 97,651 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.197 | -0.2% | -0.00767 to 0.0068 | EVEN, no difference beyond the noise |
| host CPU-seconds | 327 | 326 | -0.2% | -13.8 to 12.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.43 | 2.42 | -0.6% | -0.125 to 0.0966 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 2.17 to 29.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
