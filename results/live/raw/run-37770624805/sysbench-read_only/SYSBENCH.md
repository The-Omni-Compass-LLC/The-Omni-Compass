# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 291 | +0.2% | -0.668 to 1.6 | no difference beyond the noise |
| throughput (transactions a second) | 291 | 291 | +0.2% | -0.665 to 1.64 | no difference beyond the noise |
| queries a second | 4,653 | 4,661 | +0.2% | -10.6 to 26.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 3.13 | 3.23 | +3.0% | -0.201 to 0.392 | no difference beyond the noise |
| latency, 99th percentile (ms) | 4.33 | 4.35 | +0.6% | -0.27 to 0.318 | no difference beyond the noise |
| latency, mean (ms) | 2.33 | 2.37 | +1.5% | -0.105 to 0.175 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 248 | -51.7% | -469 to -59.6 | better |
| pages holding data, mean (MB) | 462 | 232 | -49.7% | -435 to -24 | better |
| pages read from disk into the pool (misses) | 457,414 | 1,018,254 | +122.6% | 231,021 to 890,657 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.196 | +1.3% | -0.00857 to 0.0137 | no difference beyond the noise |
| host CPU-seconds | 236 | 239 | +1.3% | -10.4 to 16.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.62 | 2.65 | +1.1% | -0.127 to 0.187 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
