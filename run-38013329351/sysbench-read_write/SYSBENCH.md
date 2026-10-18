# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 192 | +0.2% | -1.9 to 2.66 | no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.5% | -3.77 to 1.95 | no difference beyond the noise |
| queries a second | 3,948 | 3,930 | -0.5% | -75.5 to 39.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 8.58 | 7.63 | -11.1% | -6.86 to 4.95 | no difference beyond the noise |
| latency, 99th percentile (ms) | 38 | 30.3 | -20.2% | -34.5 to 19.2 | no difference beyond the noise |
| latency, mean (ms) | 4.79 | 4.71 | -1.6% | -1.72 to 1.56 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 410 | -19.9% | -189 to -14.6 | better |
| pages holding data, mean (MB) | 462 | 369 | -20.0% | -160 to -24.8 | better |
| pages read from disk into the pool (misses) | 614,990 | 881,367 | +43.3% | -66,106 to 598,860 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.19 | +2.4% | -0.00123 to 0.0103 | no difference beyond the noise |
| host CPU-seconds | 329 | 337 | +2.4% | -2.26 to 18.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.76 | 3.85 | +2.2% | -0.0514 to 0.215 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | 7.6 to 19.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
