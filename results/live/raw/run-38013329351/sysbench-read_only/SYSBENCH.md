# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.1% | -0.653 to 0.272 | no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.1% | -0.631 to 0.304 | no difference beyond the noise |
| queries a second | 4,719 | 4,716 | -0.1% | -10.1 to 4.86 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.15 | 4.08 | -1.8% | -0.262 to 0.113 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.54 | 5.47 | -1.2% | -0.45 to 0.316 | no difference beyond the noise |
| latency, mean (ms) | 3.24 | 3.22 | -0.6% | -0.125 to 0.0883 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 443 | -13.4% | -208 to 70.6 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 401 | -13.2% | -153 to 31.4 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,814 | 826,435 | +26.4% | -213,355 to 558,597 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.197 | -0.2% | -0.0129 to 0.012 | no difference beyond the noise |
| host CPU-seconds | 327 | 327 | -0.1% | -22.7 to 22.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.42 | 2.42 | -0.0% | -0.162 to 0.161 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 1.04 to 19 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
