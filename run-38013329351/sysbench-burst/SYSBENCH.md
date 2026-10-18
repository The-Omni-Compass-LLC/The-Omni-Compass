# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.3% | -6.1 to 4.21 | no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.4% | -5.72 to 3.25 | no difference beyond the noise |
| queries a second | 4,724 | 4,704 | -0.4% | -91.5 to 52.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.37 | 5.31 | -1.2% | -0.746 to 0.621 | no difference beyond the noise |
| latency, 99th percentile (ms) | 7.48 | 7.3 | -2.3% | -1.54 to 1.19 | no difference beyond the noise |
| latency, mean (ms) | 3.44 | 3.46 | +0.8% | -0.0942 to 0.15 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 495 | -3.3% | -52.2 to 18.4 | no difference beyond the noise |
| pages holding data, mean (MB) | 445 | 411 | -7.5% | -70.1 to 3.23 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,617 | 250,676 | +2.9% | -13,304 to 27,420 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.208 | +1.9% | 0.000758 to 0.00719 | **WORSE** |
| host CPU-seconds | 113 | 115 | +2.3% | 1 to 4.08 | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 2.51 | 2.57 | +2.5% | 0.00909 to 0.117 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
