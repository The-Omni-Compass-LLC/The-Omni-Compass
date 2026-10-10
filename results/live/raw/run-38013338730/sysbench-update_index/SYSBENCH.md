# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 327 | 329 | +0.5% | -123 to 127 | no difference beyond the noise |
| throughput (transactions a second) | 989 | 988 | -0.1% | -2.04 to 0.902 | no difference beyond the noise |
| queries a second | 989 | 988 | -0.1% | -2.04 to 0.902 | no difference beyond the noise |
| latency, 95th percentile (ms) | 2.7 | 2.45 | -9.3% | -0.49 to -0.0143 | better |
| latency, 99th percentile (ms) | 5.25 | 5.15 | -1.8% | -0.791 to 0.603 | no difference beyond the noise |
| latency, mean (ms) | 0.982 | 1.02 | +3.6% | -0.332 to 0.402 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 342 | -33.3% | -272 to -68.5 | better |
| pages holding data, mean (MB) | 454 | 274 | -39.7% | -270 to -90 | better |
| pages read from disk into the pool (misses) | 188,643 | 301,104 | +59.6% | 68,969 to 155,953 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.113 | +4.6% | -0.017 to 0.027 | no difference beyond the noise |
| host CPU-seconds | 190 | 199 | +4.7% | -29.3 to 47.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.35 | 1.34 | -0.8% | -0.923 to 0.901 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 12.5 to 18.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
