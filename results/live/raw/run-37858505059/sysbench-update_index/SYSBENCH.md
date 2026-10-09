# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0.00108 | 0 | -100.0% | -0.0057 to 0.00355 | no difference beyond the noise |
| throughput (transactions a second) | 968 | 967 | -0.1% | -7.49 to 5.99 | no difference beyond the noise |
| queries a second | 968 | 967 | -0.1% | -7.49 to 5.99 | no difference beyond the noise |
| latency, 95th percentile (ms) | 2.05 | 2.06 | +0.4% | -0.375 to 0.39 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.57 | 3.75 | +5.2% | -1.38 to 1.75 | no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.4 | +3.3% | -0.354 to 0.443 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 490 | -4.3% | -31.5 to -12.9 | better |
| pages holding data, mean (MB) | 449 | 408 | -9.1% | -70.5 to -11.1 | better |
| pages read from disk into the pool (misses) | 139,387 | 164,549 | +18.1% | 10,195 to 40,129 | shown, not judged |
| host CPU busy (share of the run) | 0.217 | 0.215 | -1.2% | -0.0347 to 0.0295 | no difference beyond the noise |
| host CPU-seconds | 262 | 259 | -1.2% | -42 to 35.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 262,043 | 258,903 | -1.2% | -42,033 to 35,753 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17.7 |  | 16.2 to 19.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
