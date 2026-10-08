# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,920 | 2,915 | -0.2% | -19 to 7.64 | no difference beyond the noise |
| throughput (transactions a second) | 2,931 | 2,928 | -0.1% | -10.2 to 3.96 | no difference beyond the noise |
| queries a second | 2,931 | 2,928 | -0.1% | -10.2 to 3.96 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.369 | 0.376 | +1.9% | -0.0104 to 0.0244 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.487 | 0.499 | +2.5% | -0.0222 to 0.0462 | no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.212 | +3.0% | -0.00686 to 0.0191 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 548 | +7.1% | -550 to 623 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 470 | +1.7% | -401 to 417 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 262,474 | 294,252 | +12.1% | -271,652 to 335,209 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.106 | +1.5% | -0.00384 to 0.00697 | no difference beyond the noise |
| host CPU-seconds | 116 | 118 | +1.6% | -4.58 to 8.32 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.13 | 0.132 | +1.8% | -0.00427 to 0.00898 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.33 |  | 0.609 to 18.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
