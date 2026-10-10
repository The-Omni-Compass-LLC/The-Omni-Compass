# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | +0.1% | -2.92 to 3.25 | no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.1% | -2.92 to 3.24 | no difference beyond the noise |
| queries a second | 4,702 | 4,705 | +0.1% | -46.7 to 51.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 2.4 | 2.38 | -1.2% | -0.0904 to 0.0331 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.75 | 3.7 | -1.2% | -0.298 to 0.209 | no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.74 | -0.4% | -0.0213 to 0.00828 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 305 | -40.4% | -227 to -187 | better |
| pages holding data, mean (MB) | 462 | 283 | -38.7% | -202 to -155 | better |
| pages read from disk into the pool (misses) | 653,474 | 1,288,459 | +97.2% | 529,894 to 740,076 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.139 | -0.2% | -0.00236 to 0.00173 | no difference beyond the noise |
| host CPU-seconds | 254 | 253 | -0.3% | -4.68 to 3.35 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.88 | 1.87 | -0.3% | -0.0325 to 0.0208 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | -0.00979 to 20.7 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
