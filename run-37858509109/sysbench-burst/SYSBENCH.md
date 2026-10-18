# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.6% | -5.12 to 1.86 | no difference beyond the noise |
| throughput (transactions a second) | 294 | 292 | -0.6% | -4.71 to 0.994 | no difference beyond the noise |
| queries a second | 4,699 | 4,669 | -0.6% | -75.4 to 15.9 | no difference beyond the noise |
| latency, 95th percentile (ms) | 3.37 | 3.19 | -5.3% | -0.194 to -0.16 | better |
| latency, 99th percentile (ms) | 4.82 | 4.43 | -8.1% | -0.701 to -0.0772 | better |
| latency, mean (ms) | 1.51 | 1.5 | -0.8% | -0.0849 to 0.0601 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 262 | -48.9% | -371 to -129 | better |
| pages holding data, mean (MB) | 440 | 213 | -51.5% | -296 to -157 | better |
| pages read from disk into the pool (misses) | 168,336 | 274,614 | +63.1% | 56,688 to 155,868 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.112 | +0.3% | -0.00546 to 0.00609 | no difference beyond the noise |
| host CPU-seconds | 45.2 | 45.3 | +0.2% | -2.36 to 2.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.51 | 1.52 | +0.8% | -0.0643 to 0.0894 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | 1.46 to 7.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
