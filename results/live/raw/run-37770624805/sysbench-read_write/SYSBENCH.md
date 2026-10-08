# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 189 | 190 | +0.5% | -0.956 to 3.01 | no difference beyond the noise |
| throughput (transactions a second) | 196 | 194 | -0.6% | -3.62 to 1.28 | no difference beyond the noise |
| queries a second | 3,910 | 3,887 | -0.6% | -72.4 to 25.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 9.51 | 8.44 | -11.3% | -2.53 to 0.375 | no difference beyond the noise |
| latency, 99th percentile (ms) | 14.7 | 14.8 | +0.3% | -5.53 to 5.61 | no difference beyond the noise |
| latency, mean (ms) | 5.69 | 5.6 | -1.5% | -0.7 to 0.53 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 917 | +79.2% | 119 to 692 | **WORSE** |
| pages holding data, mean (MB) | 463 | 789 | +70.4% | 188 to 464 | **WORSE** |
| pages read from disk into the pool (misses) | 435,307 | 239,067 | -45.1% | -268,345 to -124,136 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.215 | -5.3% | -0.027 to 0.00271 | no difference beyond the noise |
| host CPU-seconds | 246 | 234 | -5.2% | -29.3 to 3.55 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.23 | 3.99 | -5.7% | -0.564 to 0.0776 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 24.7 |  | 18.9 to 30.4 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
