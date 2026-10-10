# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.5% | -2.5 to -0.16 | **WORSE** |
| throughput (transactions a second) | 296 | 294 | -0.4% | -2.76 to 0.198 | no difference beyond the noise |
| queries a second | 4,728 | 4,708 | -0.4% | -44.1 to 3.17 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.23 | 4.18 | -1.2% | -0.16 to 0.0583 | no difference beyond the noise |
| latency, 99th percentile (ms) | 6.13 | 6.06 | -1.2% | -0.489 to 0.343 | no difference beyond the noise |
| latency, mean (ms) | 3.2 | 3.19 | -0.5% | -0.0906 to 0.0566 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 517 | +1.0% | -127 to 138 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 463 | +0.4% | -119 to 122 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,923 | 616,884 | -6.0% | -323,993 to 245,915 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.189 | -0.8% | -0.00699 to 0.00414 | no difference beyond the noise |
| host CPU-seconds | 314 | 312 | -0.6% | -10.6 to 6.65 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.32 | -0.2% | -0.0592 to 0.0514 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 |  | 13.2 to 23.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
