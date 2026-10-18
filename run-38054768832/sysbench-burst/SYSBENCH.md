# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 292 | +0.1% | -5.01 to 5.76 | no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.2% | -5.02 to 5.97 | no difference beyond the noise |
| queries a second | 4,707 | 4,715 | +0.2% | -80.4 to 95.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.77 | 5.74 | -0.6% | -0.429 to 0.359 | no difference beyond the noise |
| latency, 99th percentile (ms) | 8.38 | 8.43 | +0.6% | -0.519 to 0.624 | no difference beyond the noise |
| latency, mean (ms) | 3.37 | 3.38 | +0.0% | -0.0613 to 0.0645 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 466 | -9.1% | -103 to 10.1 | no difference beyond the noise |
| pages holding data, mean (MB) | 448 | 387 | -13.6% | -99.4 to -22.3 | better |
| pages read from disk into the pool (misses) | 244,732 | 258,457 | +5.6% | -26,007 to 53,457 | shown, not judged |
| host CPU busy (share of the run) | 0.188 | 0.192 | +2.2% | 0.00173 to 0.00663 | **WORSE** |
| host CPU-seconds | 104 | 106 | +2.6% | 0.732 to 4.56 | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.38 | +2.3% | 0.00595 to 0.1 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 2.7 to 11.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
