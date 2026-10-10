# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4.83 | 5.4 | +11.8% | -2.03 to 3.18 | no difference beyond the noise |
| throughput (transactions a second) | 985 | 983 | -0.2% | -5 to 1.22 | no difference beyond the noise |
| queries a second | 985 | 983 | -0.2% | -5 to 1.22 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.67 | 1.63 | -2.6% | -0.291 to 0.206 | no difference beyond the noise |
| latency, 99th percentile (ms) | 2.91 | 2.9 | -0.6% | -0.321 to 0.284 | no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1.04 | -1.5% | -0.0977 to 0.0651 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 506 | -1.1% | -170 to 159 | no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 436 | -3.8% | -180 to 146 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,611 | 204,897 | +8.1% | -102,901 to 133,474 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.121 | -4.5% | -0.0446 to 0.0332 | no difference beyond the noise |
| host CPU-seconds | 196 | 187 | -4.3% | -67.3 to 50.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 93 | 75.8 | -18.5% | -103 to 68.4 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17.3 |  | 1.36 to 33.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
