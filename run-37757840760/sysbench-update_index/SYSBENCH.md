# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1.38 | 2.28 | +65.2% | -1.43 to 3.23 | no difference beyond the noise |
| throughput (transactions a second) | 975 | 976 | +0.1% | -5.91 to 7.79 | no difference beyond the noise |
| queries a second | 975 | 976 | +0.1% | -5.91 to 7.79 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.8 | 1.84 | +2.3% | -0.518 to 0.6 | no difference beyond the noise |
| latency, 99th percentile (ms) | 2.96 | 3.19 | +8.1% | -0.869 to 1.35 | no difference beyond the noise |
| latency, mean (ms) | 1.11 | 1.12 | +1.0% | -0.163 to 0.185 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 615 | +20.0% | -162 to 367 | no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 500 | +11.3% | -105 to 207 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 138,795 | 123,169 | -11.3% | -40,290 to 9,038 | shown, not judged |
| host CPU busy (share of the run) | 0.151 | 0.181 | +19.7% | -0.133 to 0.193 | no difference beyond the noise |
| host CPU-seconds | 156 | 188 | +20.1% | -139 to 201 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 441 | 276 | -37.5% | -977 to 646 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 25.7 |  | 16.9 to 34.4 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
