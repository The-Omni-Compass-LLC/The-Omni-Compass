# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1.73 | 1.53 | -11.6% | -1.68 to 1.28 | no difference beyond the noise |
| throughput (transactions a second) | 975 | 975 | +0.0% | -5.46 to 6.01 | no difference beyond the noise |
| queries a second | 975 | 975 | +0.0% | -5.46 to 6.01 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.89 | 1.92 | +1.6% | -0.198 to 0.259 | no difference beyond the noise |
| latency, 99th percentile (ms) | 4.55 | 5.29 | +16.1% | 0.0293 to 1.44 | **WORSE** |
| latency, mean (ms) | 1.18 | 1.2 | +2.0% | -0.0409 to 0.0868 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 577 | +12.7% | 13.7 to 116 | **WORSE** |
| pages holding data, mean (MB) | 450 | 476 | +5.9% | -41.8 to 94.5 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 138,999 | 142,763 | +2.7% | -12,264 to 19,792 | shown, not judged |
| host CPU busy (share of the run) | 0.148 | 0.147 | -1.0% | -0.0326 to 0.0298 | no difference beyond the noise |
| host CPU-seconds | 153 | 152 | -0.9% | -33.1 to 30.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 325 | 349 | +7.5% | -231 to 280 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 22.7 |  | 19.8 to 25.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
