# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 292 | -0.6% | -6.75 to 3.09 | no difference beyond the noise |
| throughput (transactions a second) | 294 | 292 | -0.6% | -6.75 to 3.33 | no difference beyond the noise |
| queries a second | 4,701 | 4,674 | -0.6% | -108 to 53.3 | no difference beyond the noise |
| latency, 95th percentile (ms) | 3.66 | 3.59 | -1.8% | -0.0682 to -0.0625 | better |
| latency, 99th percentile (ms) | 4.85 | 4.82 | -0.6% | -0.363 to 0.303 | no difference beyond the noise |
| latency, mean (ms) | 2.75 | 2.73 | -0.7% | -0.0646 to 0.0276 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 517 | +1.0% | -395 to 406 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 464 | +0.5% | -337 to 342 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 456,915 | 531,776 | +16.4% | -515,573 to 665,294 | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.219 | -1.2% | -0.00308 to -0.0022 | better |
| host CPU-seconds | 266 | 263 | -1.2% | -3.69 to -2.61 | better |
| host CPU-seconds per 1,000 transactions inside the line | 2.94 | 2.93 | -0.6% | -0.0711 to 0.0378 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.7 |  | -0.89 to 28.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
