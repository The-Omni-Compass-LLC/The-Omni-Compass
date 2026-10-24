# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.2% | -0.683 to 1.93 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.3% | -0.776 to 2.68 | EVEN, no difference beyond the noise |
| queries a second | 4,708 | 4,723 | +0.3% | -12.4 to 42.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.15 | 5.09 | -1.2% | -0.415 to 0.294 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.21 | 7.26 | +0.6% | -0.324 to 0.417 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.33 | 3.32 | -0.2% | -0.12 to 0.104 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 554 | +8.2% | 9.31 to 74.9 | power given |
| pages holding data, mean (MB) | 451 | 486 | +7.9% | 17.3 to 54.2 | power given |
| pages read from disk into the pool (misses) | 245,212 | 213,586 | -12.9% | -39,845 to -23,407 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.196 | +1.3% | -0.00784 to 0.013 | EVEN, no difference beyond the noise |
| host CPU-seconds | 107 | 108 | +1.5% | -4.31 to 7.47 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.38 | 2.41 | +1.3% | -0.099 to 0.16 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 5.9 to 8.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
