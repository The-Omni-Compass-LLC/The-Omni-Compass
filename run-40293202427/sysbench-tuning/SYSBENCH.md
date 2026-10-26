# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,947 | 2,950 | +0.1% | -1.99 to 6.82 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,956 | +0.1% | -0.653 to 6 | EVEN, no difference beyond the noise |
| queries a second | 2,953 | 2,956 | +0.1% | -0.653 to 6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.32 | 0.318 | -0.6% | -0.0106 to 0.00661 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.451 | -1.2% | -0.0168 to 0.00614 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.2 | +0.9% | -0.0027 to 0.00613 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 566 | +10.6% | -99.5 to 208 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 489 | +5.3% | -68.6 to 118 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,544 | 325,093 | -11.5% | -162,746 to 77,845 | shown, not judged |
| host CPU busy (share of the run) | 0.0975 | 0.0993 | +1.9% | -0.00288 to 0.00666 | EVEN, no difference beyond the noise |
| host CPU-seconds | 162 | 165 | +2.0% | -4.79 to 11.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.12 | 0.122 | +1.9% | -0.00382 to 0.00849 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.7 |  | -4.78 to 30.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
