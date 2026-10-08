# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.29 | 6.75 | +7.2% | -4.57 to 5.48 | no difference beyond the noise |
| throughput (transactions a second) | 979 | 976 | -0.3% | -11.4 to 5.33 | no difference beyond the noise |
| queries a second | 979 | 976 | -0.3% | -11.4 to 5.33 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.73 | 2.06 | +19.2% | 0.0939 to 0.57 | **WORSE** |
| latency, 99th percentile (ms) | 3 | 4.82 | +60.6% | 1.44 to 2.2 | **WORSE** |
| latency, mean (ms) | 1.09 | 1.45 | +33.1% | 0.0612 to 0.658 | **WORSE** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 701 | +36.9% | -304 to 682 | no difference beyond the noise |
| pages holding data, mean (MB) | 450 | 546 | +21.4% | -171 to 364 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 139,508 | 124,289 | -10.9% | -100,220 to 69,782 | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.229 | +76.6% | -0.0734 to 0.273 | no difference beyond the noise |
| host CPU-seconds | 134 | 239 | +78.0% | -78.9 to 289 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 70 | 135 | +92.9% | -147 to 277 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 25.7 |  | 9.13 to 42.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
