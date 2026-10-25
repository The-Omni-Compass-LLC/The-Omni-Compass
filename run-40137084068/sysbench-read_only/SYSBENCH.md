# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.3% | -8.03 to 6.18 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.3% | -7.81 to 6.07 | EVEN, no difference beyond the noise |
| queries a second | 4,730 | 4,716 | -0.3% | -125 to 97.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.05 | 4.03 | -0.6% | -0.129 to 0.0804 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.54 | 5.5 | -0.6% | -0.177 to 0.11 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.15 | 3.14 | -0.2% | -0.0304 to 0.018 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 603 | +17.8% | -68.2 to 251 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 519 | +12.5% | -36 to 152 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,464 | 484,262 | -26.1% | -417,649 to 75,244 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.187 | -0.1% | -0.00824 to 0.00781 | EVEN, no difference beyond the noise |
| host CPU-seconds | 309 | 309 | -0.0% | -13.4 to 13.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.29 | 2.3 | +0.3% | -0.0378 to 0.0497 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18 |  | 8.06 to 27.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
