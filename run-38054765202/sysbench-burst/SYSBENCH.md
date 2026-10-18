# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.2% | -1.82 to 3.18 | no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.2% | -1.18 to 2.47 | no difference beyond the noise |
| queries a second | 4,697 | 4,707 | +0.2% | -18.9 to 39.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.12 | 5 | -2.4% | -0.597 to 0.353 | no difference beyond the noise |
| latency, 99th percentile (ms) | 7 | 6.91 | -1.2% | -0.558 to 0.392 | no difference beyond the noise |
| latency, mean (ms) | 3.25 | 3.27 | +0.7% | -0.101 to 0.148 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 484 | -5.5% | -67.9 to 12.1 | no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 414 | -7.5% | -107 to 39.3 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,343 | 243,156 | -0.1% | -25,106 to 24,730 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.19 | +2.3% | -0.00762 to 0.0161 | no difference beyond the noise |
| host CPU-seconds | 102 | 105 | +2.4% | -4.3 to 9.22 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.28 | 2.33 | +2.2% | -0.104 to 0.204 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | 0.495 to 14.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
