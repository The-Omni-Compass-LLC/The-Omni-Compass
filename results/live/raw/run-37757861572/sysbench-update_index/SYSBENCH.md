# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 42.8 | 42.7 | -0.1% | -32 to 31.9 | no difference beyond the noise |
| throughput (transactions a second) | 973 | 975 | +0.2% | -16.4 to 21.1 | no difference beyond the noise |
| queries a second | 973 | 975 | +0.2% | -16.4 to 21.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 468 | 362 | -22.7% | -1,304 to 1,091 | no difference beyond the noise |
| latency, 99th percentile (ms) | 958 | 814 | -15.0% | -2,854 to 2,567 | no difference beyond the noise |
| latency, mean (ms) | 94.3 | 79.6 | -15.6% | -221 to 191 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 660 | +28.8% | 21.7 to 273 | **WORSE** |
| pages holding data, mean (MB) | 452 | 505 | +11.8% | -11.1 to 118 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 140,255 | 135,328 | -3.5% | -23,650 to 13,795 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.134 | +1.7% | -0.0101 to 0.0147 | no difference beyond the noise |
| host CPU-seconds | 158 | 161 | +1.7% | -13.3 to 18.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 13.3 | 12.3 | -7.5% | -14.4 to 12.4 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 22.3 |  | 18.5 to 26.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
