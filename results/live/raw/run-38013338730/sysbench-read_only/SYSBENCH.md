# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 297 | 296 | -0.3% | -1.29 to -0.198 | **WORSE** |
| throughput (transactions a second) | 297 | 296 | -0.2% | -1.3 to -0.139 | **WORSE** |
| queries a second | 4,753 | 4,741 | -0.2% | -20.9 to -2.23 | **WORSE** |
| latency, 95th percentile (ms) | 1.83 | 1.78 | -2.9% | -0.144 to 0.0364 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.64 | 3.6 | -1.2% | -0.37 to 0.286 | no difference beyond the noise |
| latency, mean (ms) | 1.21 | 1.22 | +0.5% | -0.0184 to 0.0308 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 348 | -32.0% | -232 to -95.5 | better |
| pages holding data, mean (MB) | 462 | 319 | -30.8% | -211 to -73.2 | better |
| pages read from disk into the pool (misses) | 654,588 | 1,204,655 | +84.0% | 342,596 to 757,538 | shown, not judged |
| host CPU busy (share of the run) | 0.0956 | 0.096 | +0.4% | -0.00175 to 0.00259 | no difference beyond the noise |
| host CPU-seconds | 172 | 173 | +0.4% | -3.12 to 4.61 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.27 | 1.28 | +0.7% | -0.0214 to 0.0391 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 2.03 to 12 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
