# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,918 | 2,915 | -0.1% | -16.4 to 10.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,953 | +0.0% | -3.47 to 3.77 | EVEN, no difference beyond the noise |
| queries a second | 2,953 | 2,953 | +0.0% | -3.47 to 3.77 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.413 | 0.428 | +3.7% | -0.0506 to 0.0813 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.638 | 0.657 | +3.0% | 0.00436 to 0.0343 | LOSS |
| latency, mean (ms) | 0.228 | 0.235 | +3.3% | -0.00577 to 0.0209 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 524 | +2.4% | 5.53 to 19.4 | power given |
| pages holding data, mean (MB) | 464 | 461 | -0.6% | -25.5 to 20 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,968 | 365,381 | -0.4% | -34,484 to 31,310 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.121 | +4.5% | -0.00443 to 0.0148 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 201 | +4.6% | -7.22 to 24.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.144 | 0.15 | +4.7% | -0.00583 to 0.0192 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 6.06 to 25.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
