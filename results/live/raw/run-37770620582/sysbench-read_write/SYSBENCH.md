# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 189 | 190 | +0.9% | -0.695 to 4.11 | no difference beyond the noise |
| throughput (transactions a second) | 195 | 194 | -0.4% | -4.15 to 2.7 | no difference beyond the noise |
| queries a second | 3,904 | 3,889 | -0.4% | -83.1 to 54.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 9.51 | 8.48 | -10.8% | -1.26 to -0.785 | better |
| latency, 99th percentile (ms) | 13.9 | 12.6 | -9.1% | -2.44 to -0.0836 | better |
| latency, mean (ms) | 5.63 | 5.44 | -3.4% | -0.265 to -0.123 | better |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 816 | +59.3% | 74.5 to 533 | **WORSE** |
| pages holding data, mean (MB) | 462 | 707 | +53.0% | 112 to 378 | **WORSE** |
| pages read from disk into the pool (misses) | 435,566 | 260,382 | -40.2% | -366,504 to 16,136 | shown, not judged |
| host CPU busy (share of the run) | 0.229 | 0.217 | -5.2% | -0.0236 to -7.04e-05 | better |
| host CPU-seconds | 248 | 235 | -5.1% | -25.2 to -0.321 | better |
| host CPU-seconds per 1,000 transactions inside the line | 4.26 | 4.01 | -6.0% | -0.459 to -0.0512 | better |
| buffer pool size changes written (the knob's moves) | 0 | 22 |  | 17 to 27 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
