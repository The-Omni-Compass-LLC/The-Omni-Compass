# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `bc2eb38f4ca8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,951 | 2,948 | -0.1% | -36.1 to 30.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,964 | 2,966 | +0.0% | -0.632 to 3.3 | EVEN, no difference beyond the noise |
| queries a second | 2,964 | 2,966 | +0.0% | -0.632 to 3.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.24 | 0.244 | +1.8% | -0.0143 to 0.023 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.388 | 0.407 | +5.0% | -0.0551 to 0.0938 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.393 | 0.513 | +30.5% | -0.97 to 1.21 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 487 | -4.9% | -48.4 to -1.71 | GAIN |
| pages holding data, mean (MB) | 463 | 446 | -3.9% | -54.2 to 18.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,409 | 372,458 | +1.4% | -25,949 to 36,047 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.119 | +1.6% | -0.00792 to 0.0116 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 211 | +1.7% | -13.3 to 20.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.155 | 0.157 | +1.7% | -0.00826 to 0.0136 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 0.929 to 12.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
