# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 293 | -0.4% | -9.57 to 6.97 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.1% | -2.75 to 1.99 | EVEN, no difference beyond the noise |
| queries a second | 4,746 | 4,740 | -0.1% | -44 to 31.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.88 | 2.84 | -1.2% | -0.107 to 0.0392 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.45 | 37.1 | +580.0% | -108 to 171 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.71 | 4.49 | +66.0% | -7.56 to 11.1 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 492 | -3.9% | -127 to 87.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 440 | -4.6% | -150 to 107 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,608 | 691,621 | +5.8% | -219,445 to 295,471 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.173 | -0.9% | -0.00867 to 0.00559 | EVEN, no difference beyond the noise |
| host CPU-seconds | 314 | 312 | -0.9% | -15.4 to 9.82 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.34 | 2.33 | -0.5% | -0.0465 to 0.0251 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 10.9 to 18.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
