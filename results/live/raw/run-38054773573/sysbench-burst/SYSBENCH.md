# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 289 | 288 | -0.0% | -4.49 to 4.38 | no difference beyond the noise |
| throughput (transactions a second) | 292 | 291 | -0.2% | -7.14 to 6.14 | no difference beyond the noise |
| queries a second | 4,672 | 4,664 | -0.2% | -114 to 98.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.23 | 4.1 | -2.9% | -0.659 to 0.411 | no difference beyond the noise |
| latency, 99th percentile (ms) | 31.5 | 14 | -55.5% | -132 to 96.8 | no difference beyond the noise |
| latency, mean (ms) | 3.79 | 2.71 | -28.4% | -5.39 to 3.24 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 283 | -44.8% | -368 to -91.1 | better |
| pages holding data, mean (MB) | 441 | 244 | -44.7% | -329 to -65.4 | better |
| pages read from disk into the pool (misses) | 243,999 | 363,652 | +49.0% | -33,972 to 273,279 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.164 | -0.6% | -0.00403 to 0.00202 | no difference beyond the noise |
| host CPU-seconds | 101 | 100 | -0.6% | -2.45 to 1.31 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.27 | 2.26 | -0.5% | -0.0566 to 0.032 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | 0.872 to 8.46 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
