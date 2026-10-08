# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.09 | 2.39 | -22.7% | -4.05 to 2.65 | no difference beyond the noise |
| throughput (transactions a second) | 976 | 976 | +0.0% | -2.64 to 2.69 | no difference beyond the noise |
| queries a second | 976 | 976 | +0.0% | -2.64 to 2.69 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.99 | 2.15 | +7.8% | -0.348 to 0.66 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.71 | 4 | +8.1% | -0.0843 to 0.682 | no difference beyond the noise |
| latency, mean (ms) | 1.15 | 1.17 | +2.5% | -0.118 to 0.176 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 547 | +6.9% | -79.9 to 151 | no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 440 | -1.9% | -74.4 to 56.9 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 139,278 | 147,884 | +6.2% | -34,472 to 51,685 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.175 | +25.5% | -0.0525 to 0.123 | no difference beyond the noise |
| host CPU-seconds | 144 | 181 | +25.7% | -54.5 to 129 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 226 | 273 | +20.8% | -253 to 347 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 24.3 |  | 14.9 to 33.7 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
