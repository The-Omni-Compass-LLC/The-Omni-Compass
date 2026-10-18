# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.58 | 4.14 | +15.6% | -9.41 to 10.5 | no difference beyond the noise |
| throughput (transactions a second) | 983 | 982 | -0.1% | -3.66 to 2.19 | no difference beyond the noise |
| queries a second | 983 | 982 | -0.1% | -3.66 to 2.19 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.87 | 1.88 | +0.5% | -0.314 to 0.333 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.54 | 3.53 | -0.3% | -1.36 to 1.34 | no difference beyond the noise |
| latency, mean (ms) | 1.23 | 1.19 | -3.2% | -0.796 to 0.718 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 485 | -5.2% | -121 to 67.9 | no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 415 | -8.5% | -156 to 78.3 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,157 | 212,034 | +12.1% | -72,511 to 118,264 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.158 | +24.2% | -0.153 to 0.214 | no difference beyond the noise |
| host CPU-seconds | 196 | 244 | +24.7% | -235 to 332 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 198 | 185 | -6.8% | -758 to 731 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | -10.5 to 32.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
