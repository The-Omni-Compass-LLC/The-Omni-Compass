# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,920 | 2,924 | +0.1% | -1.63 to 7.77 | no difference beyond the noise |
| throughput (transactions a second) | 2,928 | 2,929 | +0.0% | -6.22 to 8.77 | no difference beyond the noise |
| queries a second | 2,928 | 2,929 | +0.0% | -6.22 to 8.77 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.374 | 0.359 | -4.2% | -0.0707 to 0.0393 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.474 | 0.453 | -4.4% | -0.114 to 0.0715 | no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.2 | -2.9% | -0.037 to 0.0249 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 575 | +12.2% | -379 to 505 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 499 | +7.9% | -284 to 357 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 262,671 | 242,790 | -7.6% | -259,721 to 219,958 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.1 | -5.0% | -0.0323 to 0.0217 | no difference beyond the noise |
| host CPU-seconds | 117 | 111 | -5.0% | -36.2 to 24.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.131 | 0.124 | -5.1% | -0.0407 to 0.0274 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 1.43 to 14.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
