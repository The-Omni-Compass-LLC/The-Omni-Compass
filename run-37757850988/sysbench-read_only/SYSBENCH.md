# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.4% | -5.1 to 7.27 | no difference beyond the noise |
| throughput (transactions a second) | 292 | 293 | +0.4% | -4.99 to 7.32 | no difference beyond the noise |
| queries a second | 4,672 | 4,691 | +0.4% | -79.9 to 117 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.25 | 4.3 | +1.2% | -0.0591 to 0.162 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.64 | +0.6% | -0.256 to 0.323 | no difference beyond the noise |
| latency, mean (ms) | 3.22 | 3.25 | +1.1% | -0.0612 to 0.131 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 372 | -27.3% | -508 to 229 | no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 339 | -26.6% | -447 to 202 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 455,556 | 831,679 | +82.6% | -139,844 to 892,090 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.206 | +2.9% | -0.014 to 0.0255 | no difference beyond the noise |
| host CPU-seconds | 223 | 230 | +3.2% | -15.8 to 30.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.48 | 2.55 | +2.8% | -0.132 to 0.273 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.7 |  | -0.497 to 31.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
