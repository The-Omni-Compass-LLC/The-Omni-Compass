# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 181 | 185 | +2.0% | -4.69 to 11.8 | no difference beyond the noise |
| throughput (transactions a second) | 192 | 192 | +0.0% | -3.95 to 3.95 | no difference beyond the noise |
| queries a second | 3,850 | 3,850 | +0.0% | -78.9 to 79.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 11.6 | 9.5 | -18.0% | -6.51 to 2.34 | no difference beyond the noise |
| latency, 99th percentile (ms) | 158 | 193 | +22.1% | -91.9 to 162 | no difference beyond the noise |
| latency, mean (ms) | 8.77 | 9.17 | +4.5% | -2.15 to 2.94 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 895 | +74.8% | -7.01 to 773 | no difference beyond the noise |
| pages holding data, mean (MB) | 459 | 773 | +68.3% | 36.6 to 591 | **WORSE** |
| pages read from disk into the pool (misses) | 434,039 | 230,443 | -46.9% | -493,723 to 86,530 | shown, not judged |
| host CPU busy (share of the run) | 0.235 | 0.225 | -4.1% | -0.036 to 0.0166 | no difference beyond the noise |
| host CPU-seconds | 285 | 274 | -4.1% | -42.6 to 19.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.07 | 4.77 | -5.9% | -0.902 to 0.301 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 23.3 |  | 13.9 to 32.7 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
