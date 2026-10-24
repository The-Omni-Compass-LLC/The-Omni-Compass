# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.2% | -6.97 to 5.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.2% | -7.08 to 5.64 | EVEN, no difference beyond the noise |
| queries a second | 4,732 | 4,721 | -0.2% | -113 to 90.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.1 | 4.05 | -1.2% | -0.153 to 0.056 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.6 | -2.9% | -0.458 to 0.118 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.15 | 3.14 | -0.4% | -0.126 to 0.104 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -37.3 to 29.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 461 | -0.1% | -25.8 to 24.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,483 | 632,679 | -3.5% | -105,767 to 60,158 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.187 | +0.1% | -0.015 to 0.0155 | EVEN, no difference beyond the noise |
| host CPU-seconds | 309 | 310 | +0.2% | -24.9 to 26.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.29 | 2.3 | +0.5% | -0.131 to 0.152 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.7 |  | 6.94 to 24.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
