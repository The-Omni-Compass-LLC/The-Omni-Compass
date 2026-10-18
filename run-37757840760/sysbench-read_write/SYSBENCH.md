# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 194 | +1.2% | -3.16 to 7.8 | no difference beyond the noise |
| throughput (transactions a second) | 194 | 196 | +0.8% | -0.445 to 3.68 | no difference beyond the noise |
| queries a second | 3,886 | 3,918 | +0.8% | -8.89 to 73.5 | no difference beyond the noise |
| latency, 95th percentile (ms) | 7.94 | 7.56 | -4.8% | -2.28 to 1.52 | no difference beyond the noise |
| latency, 99th percentile (ms) | 11.7 | 10.7 | -9.0% | -4.82 to 2.71 | no difference beyond the noise |
| latency, mean (ms) | 5.08 | 4.99 | -1.9% | -0.508 to 0.319 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 708 | +38.3% | -430 to 822 | no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 611 | +32.5% | -314 to 614 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 431,242 | 318,781 | -26.1% | -593,652 to 368,730 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.204 | -2.5% | -0.0346 to 0.0241 | no difference beyond the noise |
| host CPU-seconds | 226 | 221 | -2.5% | -37.5 to 26.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.85 | 3.71 | -3.6% | -0.769 to 0.489 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19.7 |  | 7.41 to 31.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
