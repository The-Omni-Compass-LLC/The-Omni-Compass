# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.1% | -2.75 to 2 | no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.1% | -3.36 to 2.75 | no difference beyond the noise |
| queries a second | 4,715 | 4,710 | -0.1% | -53.8 to 43.9 | no difference beyond the noise |
| latency, 95th percentile (ms) | 2.15 | 2.14 | -0.5% | -0.31 to 0.288 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.73 | 3.86 | +3.5% | -0.775 to 1.03 | no difference beyond the noise |
| latency, mean (ms) | 1.38 | 1.33 | -3.6% | -0.233 to 0.132 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 225 | -56.1% | -491 to -83.1 | better |
| pages holding data, mean (MB) | 462 | 212 | -54.2% | -430 to -70.4 | better |
| pages read from disk into the pool (misses) | 457,974 | 1,108,461 | +142.0% | 95,329 to 1,205,644 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.108 | -4.4% | -0.0224 to 0.0125 | no difference beyond the noise |
| host CPU-seconds | 136 | 130 | -4.4% | -27.2 to 15.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.51 | 1.45 | -4.3% | -0.308 to 0.179 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | -1.45 to 13.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
