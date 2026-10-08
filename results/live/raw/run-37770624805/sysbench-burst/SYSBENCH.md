# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 288 | 290 | +0.8% | -7.95 to 12.3 | no difference beyond the noise |
| throughput (transactions a second) | 291 | 292 | +0.2% | -4.93 to 5.87 | no difference beyond the noise |
| queries a second | 4,657 | 4,664 | +0.2% | -78.9 to 93.9 | no difference beyond the noise |
| latency, 95th percentile (ms) | 6.17 | 5.99 | -3.0% | -1.02 to 0.657 | no difference beyond the noise |
| latency, 99th percentile (ms) | 8.86 | 7.71 | -13.1% | -4.91 to 2.6 | no difference beyond the noise |
| latency, mean (ms) | 3.62 | 3.53 | -2.4% | -0.437 to 0.26 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 171 | -66.7% | -343 to -340 | better |
| pages holding data, mean (MB) | 438 | 146 | -66.7% | -316 to -269 | better |
| pages read from disk into the pool (misses) | 167,269 | 337,934 | +102.0% | 163,348 to 177,982 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.209 | -1.5% | -0.0214 to 0.0152 | no difference beyond the noise |
| host CPU-seconds | 78.7 | 77.8 | -1.1% | -8.1 to 6.34 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.65 | 2.61 | -1.9% | -0.385 to 0.286 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
