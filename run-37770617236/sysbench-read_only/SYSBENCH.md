# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.2% | -1.31 to 2.63 | no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.3% | -1.02 to 2.6 | no difference beyond the noise |
| queries a second | 4,685 | 4,698 | +0.3% | -16.3 to 41.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 3.68 | 3.75 | +1.8% | 0.067 to 0.067 | **WORSE** |
| latency, 99th percentile (ms) | 5.09 | 5.06 | -0.6% | -0.379 to 0.317 | no difference beyond the noise |
| latency, mean (ms) | 2.75 | 2.81 | +2.3% | 0.0144 to 0.112 | **WORSE** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 258 | -49.5% | -476 to -31.4 | better |
| pages holding data, mean (MB) | 461 | 220 | -52.4% | -356 to -128 | better |
| pages read from disk into the pool (misses) | 456,881 | 1,035,506 | +126.6% | 377,919 to 779,329 | shown, not judged |
| host CPU busy (share of the run) | 0.222 | 0.226 | +2.0% | -0.00389 to 0.0126 | no difference beyond the noise |
| host CPU-seconds | 266 | 271 | +2.0% | -5.2 to 15.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.96 | 3.01 | +1.7% | -0.058 to 0.159 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 3.43 to 16.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
