# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 291 | -0.2% | -5.38 to 4.01 | no difference beyond the noise |
| throughput (transactions a second) | 293 | 292 | -0.2% | -5.09 to 3.94 | no difference beyond the noise |
| queries a second | 4,681 | 4,672 | -0.2% | -81.4 to 63 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.36 | 4.49 | +3.0% | -0.0907 to 0.354 | no difference beyond the noise |
| latency, 99th percentile (ms) | 6.02 | 6.28 | +4.3% | -0.0529 to 0.567 | no difference beyond the noise |
| latency, mean (ms) | 3.25 | 3.31 | +1.7% | 0.0397 to 0.0729 | **WORSE** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 326 | -36.3% | -541 to 170 | no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 290 | -37.4% | -458 to 111 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 456,009 | 879,257 | +92.8% | 97,100 to 749,396 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.206 | +3.0% | 0.00325 to 0.00892 | **WORSE** |
| host CPU-seconds | 223 | 231 | +3.5% | 4.21 to 11.4 | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 2.48 | 2.57 | +3.7% | 0.0205 to 0.165 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 13.7 |  | 3.32 to 24 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
