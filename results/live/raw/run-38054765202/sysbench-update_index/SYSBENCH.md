# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 93 | 88 | -5.4% | -88.7 to 78.7 | no difference beyond the noise |
| throughput (transactions a second) | 988 | 984 | -0.4% | -14.6 to 6.74 | no difference beyond the noise |
| queries a second | 988 | 984 | -0.4% | -14.6 to 6.74 | no difference beyond the noise |
| latency, 95th percentile (ms) | 187 | 285 | +52.4% | -447 to 643 | no difference beyond the noise |
| latency, 99th percentile (ms) | 534 | 830 | +55.6% | -2,106 to 2,700 | no difference beyond the noise |
| latency, mean (ms) | 38.8 | 57.8 | +48.9% | -109 to 147 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 440 | -14.0% | -126 to -17.1 | better |
| pages holding data, mean (MB) | 453 | 360 | -20.6% | -163 to -24 | better |
| pages read from disk into the pool (misses) | 190,418 | 253,477 | +33.1% | 20,508 to 105,611 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.128 | -3.1% | -0.033 to 0.0249 | no difference beyond the noise |
| host CPU-seconds | 236 | 228 | -3.2% | -62 to 47.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.64 | 5.94 | +5.3% | -5.71 to 6.3 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 23.3 |  | 18.2 to 28.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
