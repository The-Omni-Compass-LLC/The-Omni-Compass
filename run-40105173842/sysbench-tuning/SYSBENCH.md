# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,959 | 2,958 | -0.0% | -7.09 to 4.91 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,965 | +0.0% | -1.79 to 2.45 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,965 | +0.0% | -1.79 to 2.45 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.197 | 0.2 | +1.9% | -0.0308 to 0.0381 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.338 | 0.336 | -0.6% | -0.0622 to 0.0582 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0941 | 0.0936 | -0.5% | -0.026 to 0.0252 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 534 | +4.3% | -81.9 to 126 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 486 | +4.9% | -76.1 to 122 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,601 | 331,555 | -9.8% | -157,801 to 85,709 | shown, not judged |
| host CPU busy (share of the run) | 0.0736 | 0.0691 | -6.1% | -0.0221 to 0.0132 | EVEN, no difference beyond the noise |
| host CPU-seconds | 132 | 124 | -6.1% | -39.6 to 23.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0979 | 0.092 | -6.0% | -0.0295 to 0.0177 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 0.0626 to 19.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
