# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 191 | -0.9% | -5.03 to 1.7 | no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.3% | -3.49 to 2.38 | no difference beyond the noise |
| queries a second | 3,945 | 3,933 | -0.3% | -69.8 to 47.5 | no difference beyond the noise |
| latency, 95th percentile (ms) | 8.79 | 9.33 | +6.2% | 0.0758 to 1.01 | **WORSE** |
| latency, 99th percentile (ms) | 13.1 | 13.7 | +4.3% | 0.201 to 0.929 | **WORSE** |
| latency, mean (ms) | 5.41 | 5.51 | +1.9% | -0.0985 to 0.3 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 487 | -4.8% | -135 to 85.9 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 427 | -7.4% | -90.7 to 22 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,576 | 695,914 | +13.1% | -144,768 to 305,444 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.224 | +2.0% | -0.00351 to 0.0122 | no difference beyond the noise |
| host CPU-seconds | 354 | 361 | +2.2% | -6.07 to 21.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.02 | 4.14 | +3.1% | -0.0962 to 0.342 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 23.3 |  | 19.5 to 27.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
