# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 291 | -0.2% | -1.64 to 0.196 | no difference beyond the noise |
| throughput (transactions a second) | 291 | 291 | -0.2% | -1.63 to 0.277 | no difference beyond the noise |
| queries a second | 4,663 | 4,652 | -0.2% | -26.1 to 4.43 | no difference beyond the noise |
| latency, 95th percentile (ms) | 2.7 | 2.68 | -0.6% | -0.0884 to 0.0551 | no difference beyond the noise |
| latency, 99th percentile (ms) | 4.15 | 4.1 | -1.2% | -0.159 to 0.058 | no difference beyond the noise |
| latency, mean (ms) | 1.88 | 1.86 | -0.6% | -0.067 to 0.044 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 385 | -24.7% | -493 to 240 | no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 337 | -26.9% | -413 to 165 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 458,240 | 800,796 | +74.8% | -150,858 to 835,969 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.155 | -0.6% | -0.00599 to 0.00402 | no difference beyond the noise |
| host CPU-seconds | 192 | 190 | -0.6% | -7.4 to 4.98 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.13 | 2.12 | -0.4% | -0.0708 to 0.0552 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | -4.42 to 20.4 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
