# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 291 | -0.6% | -7.22 to 3.79 | no difference beyond the noise |
| throughput (transactions a second) | 293 | 291 | -0.6% | -7.16 to 3.73 | no difference beyond the noise |
| queries a second | 4,683 | 4,655 | -0.6% | -115 to 59.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.79 | 4.91 | +2.4% | -0.133 to 0.363 | no difference beyond the noise |
| latency, 99th percentile (ms) | 6.1 | 6.17 | +1.2% | -0.562 to 0.706 | no difference beyond the noise |
| latency, mean (ms) | 2.85 | 2.93 | +2.9% | 0.0617 to 0.106 | **WORSE** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 171 | -66.7% | -343 to -340 | better |
| pages holding data, mean (MB) | 440 | 149 | -66.2% | -317 to -265 | better |
| pages read from disk into the pool (misses) | 169,349 | 334,300 | +97.4% | 161,067 to 168,835 | shown, not judged |
| host CPU busy (share of the run) | 0.223 | 0.226 | +1.6% | 0.000105 to 0.00716 | **WORSE** |
| host CPU-seconds | 89.4 | 90.8 | +1.6% | 0.0404 to 2.89 | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 2.97 | 3.04 | +2.2% | 0.0135 to 0.12 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
