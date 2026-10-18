# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 297 | 296 | -0.3% | -5.39 to 3.76 | no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.3% | -5.35 to 3.78 | no difference beyond the noise |
| queries a second | 4,751 | 4,738 | -0.3% | -85.5 to 60.5 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.95 | 1.89 | -3.0% | -0.328 to 0.21 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.62 | 3.66 | +1.1% | -0.206 to 0.288 | no difference beyond the noise |
| latency, mean (ms) | 1.29 | 1.28 | -0.8% | -0.0765 to 0.0565 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 385 | -24.8% | -159 to -94.6 | better |
| pages holding data, mean (MB) | 462 | 359 | -22.2% | -124 to -80.7 | better |
| pages read from disk into the pool (misses) | 657,571 | 1,058,917 | +61.0% | 192,402 to 610,289 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.101 | -0.2% | -0.00434 to 0.00385 | no difference beyond the noise |
| host CPU-seconds | 183 | 182 | -0.2% | -7.82 to 6.97 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.35 | 1.35 | +0.0% | -0.0694 to 0.0707 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 4.87 to 12.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
