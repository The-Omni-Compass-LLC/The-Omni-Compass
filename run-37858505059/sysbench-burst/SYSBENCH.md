# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 290 | -0.5% | -5.99 to 2.83 | no difference beyond the noise |
| throughput (transactions a second) | 291 | 290 | -0.5% | -5.86 to 2.85 | no difference beyond the noise |
| queries a second | 4,661 | 4,637 | -0.5% | -93.8 to 45.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.54 | 4.54 | +0.0% | -0.408 to 0.412 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.84 | 5.77 | -1.2% | -0.368 to 0.229 | no difference beyond the noise |
| latency, mean (ms) | 2.82 | 2.87 | +1.7% | -0.0096 to 0.105 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 231 | -54.9% | -306 to -256 | better |
| pages holding data, mean (MB) | 438 | 194 | -55.7% | -269 to -219 | better |
| pages read from disk into the pool (misses) | 167,008 | 294,013 | +76.0% | 89,110 to 164,900 | shown, not judged |
| host CPU busy (share of the run) | 0.222 | 0.226 | +1.5% | 0.000403 to 0.00638 | **WORSE** |
| host CPU-seconds | 89.3 | 90.7 | +1.6% | 0.231 to 2.56 | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 2.98 | 3.04 | +2.1% | 0.0448 to 0.081 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 0.798 to 6.54 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
