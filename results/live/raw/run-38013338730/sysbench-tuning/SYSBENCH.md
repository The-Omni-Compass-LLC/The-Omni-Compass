# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,948 | -0.0% | -6.65 to 5.4 | no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,954 | -0.0% | -5.77 to 5.36 | no difference beyond the noise |
| queries a second | 2,954 | 2,954 | -0.0% | -5.77 to 5.36 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.334 | 0.332 | -0.6% | -0.0106 to 0.00661 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.456 | +0.0% | 0 to 0 | same |
| latency, mean (ms) | 0.203 | 0.206 | +1.4% | -0.000846 to 0.00642 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 447 | -12.7% | -165 to 34.2 | no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 407 | -12.2% | -141 to 28.2 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,251 | 455,445 | +24.0% | -76,456 to 252,845 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.104 | +3.0% | -0.000168 to 0.00626 | no difference beyond the noise |
| host CPU-seconds | 168 | 173 | +3.2% | -0.425 to 11.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.124 | 0.128 | +3.2% | -0.000391 to 0.00841 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 0.0313 to 9.97 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
