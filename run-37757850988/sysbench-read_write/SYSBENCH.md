# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 192 | +1.3% | -2.1 to 7.14 | no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.1% | -3.93 to 3.6 | no difference beyond the noise |
| queries a second | 3,915 | 3,912 | -0.1% | -78.5 to 72 | no difference beyond the noise |
| latency, 95th percentile (ms) | 9.33 | 8.26 | -11.5% | -3.16 to 1.01 | no difference beyond the noise |
| latency, 99th percentile (ms) | 13.6 | 11.9 | -12.9% | -5.22 to 1.71 | no difference beyond the noise |
| latency, mean (ms) | 5.56 | 5.31 | -4.6% | -0.595 to 0.0814 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 803 | +56.8% | -99.8 to 682 | no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 709 | +53.8% | -103 to 599 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 435,904 | 252,039 | -42.2% | -479,681 to 111,951 | shown, not judged |
| host CPU busy (share of the run) | 0.226 | 0.212 | -6.3% | -0.0393 to 0.0108 | no difference beyond the noise |
| host CPU-seconds | 245 | 229 | -6.4% | -43.1 to 12 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.19 | 3.87 | -7.5% | -0.871 to 0.241 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 24.7 |  | 18.9 to 30.4 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
