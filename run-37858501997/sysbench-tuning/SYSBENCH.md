# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,923 | 2,921 | -0.1% | -11.5 to 8.23 | no difference beyond the noise |
| throughput (transactions a second) | 2,930 | 2,929 | -0.0% | -17 to 15.2 | no difference beyond the noise |
| queries a second | 2,930 | 2,929 | -0.0% | -17 to 15.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.365 | 0.363 | -0.5% | -0.0106 to 0.00661 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.467 | 0.464 | -0.6% | -0.0347 to 0.0287 | no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.203 | +0.8% | -0.00124 to 0.00461 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 626 | +22.2% | -430 to 658 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 528 | +14.3% | -350 to 482 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 262,586 | 219,665 | -16.3% | -365,074 to 279,232 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.103 | -0.1% | -0.00689 to 0.00669 | no difference beyond the noise |
| host CPU-seconds | 115 | 115 | -0.1% | -8.45 to 8.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.128 | 0.128 | -0.0% | -0.00974 to 0.00969 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 |  | 0.744 to 15.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
