# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 100 | 95.7 | -4.3% | -20.6 to 12 | no difference beyond the noise |
| throughput (transactions a second) | 195 | 196 | +0.6% | -2.64 to 5.15 | no difference beyond the noise |
| queries a second | 3,904 | 3,929 | +0.6% | -52.7 to 103 | no difference beyond the noise |
| latency, 95th percentile (ms) | 321 | 245 | -23.8% | -248 to 95.5 | no difference beyond the noise |
| latency, 99th percentile (ms) | 755 | 454 | -39.8% | -727 to 125 | no difference beyond the noise |
| latency, mean (ms) | 68.5 | 55.5 | -19.0% | -36.9 to 10.8 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 831 | +62.3% | 220 to 418 | **WORSE** |
| pages holding data, mean (MB) | 460 | 675 | +46.8% | 58.7 to 372 | **WORSE** |
| pages read from disk into the pool (misses) | 431,327 | 241,571 | -44.0% | -386,312 to 6,801 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.185 | -4.6% | -0.0153 to -0.00242 | better |
| host CPU-seconds | 233 | 222 | -4.5% | -17.2 to -3.88 | better |
| host CPU-seconds per 1,000 transactions inside the line | 7.6 | 7.6 | -0.0% | -1.05 to 1.04 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 21.7 |  | 16.5 to 26.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 2.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
