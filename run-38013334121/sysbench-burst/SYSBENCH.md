# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 294 | +0.7% | 1.16 to 3.14 | better |
| throughput (transactions a second) | 293 | 295 | +0.8% | 0.15 to 4.34 | better |
| queries a second | 4,687 | 4,723 | +0.8% | 2.4 to 69.5 | better |
| latency, 95th percentile (ms) | 5.25 | 5.25 | -0.0% | -0.408 to 0.407 | no difference beyond the noise |
| latency, 99th percentile (ms) | 7.34 | 7.34 | +0.0% | -0.989 to 0.989 | same |
| latency, mean (ms) | 3.36 | 3.4 | +1.1% | -0.0331 to 0.107 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 502 | -1.9% | -24.8 to 5.36 | no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 418 | -6.5% | -54.9 to -3.4 | better |
| pages read from disk into the pool (misses) | 244,343 | 245,843 | +0.6% | -5,970 to 8,969 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.201 | +3.6% | -0.00201 to 0.016 | no difference beyond the noise |
| host CPU-seconds | 107 | 111 | +3.8% | -1.09 to 9.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.4 | 2.48 | +3.1% | -0.041 to 0.189 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
