# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 187 | 190 | +1.4% | -0.557 to 5.92 | no difference beyond the noise |
| throughput (transactions a second) | 195 | 194 | -0.6% | -3.41 to 1.17 | no difference beyond the noise |
| queries a second | 3,900 | 3,877 | -0.6% | -68.2 to 23.3 | no difference beyond the noise |
| latency, 95th percentile (ms) | 10 | 8.58 | -14.4% | -1.92 to -0.982 | better |
| latency, 99th percentile (ms) | 15.2 | 12.8 | -15.5% | -5.82 to 1.11 | no difference beyond the noise |
| latency, mean (ms) | 5.95 | 5.56 | -6.5% | -1.16 to 0.386 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 942 | +84.1% | 81 to 780 | **WORSE** |
| pages holding data, mean (MB) | 461 | 797 | +73.0% | 121 to 552 | **WORSE** |
| pages read from disk into the pool (misses) | 434,006 | 193,175 | -55.5% | -363,149 to -118,513 | shown, not judged |
| host CPU busy (share of the run) | 0.231 | 0.215 | -6.9% | -0.0319 to -0.000215 | better |
| host CPU-seconds | 250 | 233 | -7.0% | -33.9 to -0.926 | better |
| host CPU-seconds per 1,000 transactions inside the line | 4.34 | 3.98 | -8.3% | -0.58 to -0.136 | better |
| buffer pool size changes written (the knob's moves) | 0 | 26.3 |  | 24.9 to 27.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
