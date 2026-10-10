# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,950 | 2,948 | -0.1% | -14.1 to 10.9 | no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,951 | -0.0% | -14 to 11.8 | no difference beyond the noise |
| queries a second | 2,952 | 2,951 | -0.0% | -14 to 11.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.332 | 0.324 | -2.4% | -0.0308 to 0.0148 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.432 | 0.424 | -1.9% | -0.0468 to 0.0302 | no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.201 | -0.1% | -0.00985 to 0.00949 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 450 | -12.0% | -110 to -13.3 | better |
| pages holding data, mean (MB) | 464 | 406 | -12.4% | -101 to -14.5 | better |
| pages read from disk into the pool (misses) | 365,499 | 452,894 | +23.9% | -25,925 to 200,714 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.103 | +0.8% | -0.0083 to 0.00993 | no difference beyond the noise |
| host CPU-seconds | 169 | 171 | +1.0% | -13.5 to 16.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.125 | 0.126 | +1.0% | -0.00943 to 0.012 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.7 |  | 5.41 to 17.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
