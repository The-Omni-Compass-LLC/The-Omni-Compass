# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 292 | +0.7% | -7.73 to 11.9 | no difference beyond the noise |
| throughput (transactions a second) | 292 | 294 | +0.6% | -8.5 to 12.2 | no difference beyond the noise |
| queries a second | 4,668 | 4,698 | +0.6% | -136 to 195 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.99 | 5.95 | -0.6% | -0.445 to 0.372 | no difference beyond the noise |
| latency, 99th percentile (ms) | 7.94 | 7.89 | -0.6% | -0.247 to 0.154 | no difference beyond the noise |
| latency, mean (ms) | 3.49 | 3.52 | +1.0% | -0.0294 to 0.0975 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 236 | -53.9% | -649 to 97.8 | no difference beyond the noise |
| pages holding data, mean (MB) | 438 | 200 | -54.4% | -517 to 40.8 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 167,371 | 291,275 | +74.0% | -100,582 to 348,391 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.211 | +3.8% | -0.00358 to 0.0192 | no difference beyond the noise |
| host CPU-seconds | 75.4 | 78.6 | +4.3% | -1.05 to 7.51 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.53 | 2.61 | +3.5% | 0.0343 to 0.144 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | -3.61 to 13.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
