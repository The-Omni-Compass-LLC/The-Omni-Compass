# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,916 | 2,917 | +0.0% | -10.7 to 12.3 | no difference beyond the noise |
| throughput (transactions a second) | 2,928 | 2,929 | +0.0% | -11.2 to 12.8 | no difference beyond the noise |
| queries a second | 2,928 | 2,929 | +0.0% | -11.2 to 12.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.386 | 0.388 | +0.6% | -0.00771 to 0.0124 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.505 | 0.496 | -1.8% | -0.0314 to 0.0134 | no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.227 | +1.2% | -0.012 to 0.0174 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 362 | -29.3% | -553 to 252 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 337 | -27.1% | -498 to 248 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 262,404 | 396,278 | +51.0% | -240,072 to 507,820 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.127 | +0.9% | -0.00158 to 0.0038 | no difference beyond the noise |
| host CPU-seconds | 140 | 142 | +1.0% | -1.17 to 3.87 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.157 | 0.158 | +0.9% | -0.000709 to 0.00365 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | -2.37 to 17.7 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
