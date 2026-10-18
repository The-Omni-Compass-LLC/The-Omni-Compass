# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,922 | 2,921 | -0.0% | -11.8 to 8.98 | no difference beyond the noise |
| throughput (transactions a second) | 2,931 | 2,930 | -0.0% | -12.5 to 10.3 | no difference beyond the noise |
| queries a second | 2,931 | 2,930 | -0.0% | -12.5 to 10.3 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.374 | 0.374 | +0.0% | -0.0348 to 0.0348 | same |
| latency, 99th percentile (ms) | 0.482 | 0.479 | -0.6% | -0.0568 to 0.0508 | no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.212 | +0.8% | -0.0146 to 0.0179 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 437 | -14.6% | -398 to 249 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 398 | -13.8% | -358 to 230 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 262,148 | 336,355 | +28.3% | -217,662 to 366,075 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.112 | +1.9% | -0.0141 to 0.0184 | no difference beyond the noise |
| host CPU-seconds | 122 | 125 | +2.2% | -15.8 to 21.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.136 | 0.139 | +2.2% | -0.0175 to 0.0235 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 1.08 to 13.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
