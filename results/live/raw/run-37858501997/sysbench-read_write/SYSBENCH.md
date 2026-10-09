# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 188 | 192 | +1.9% | 0.263 to 6.81 | better |
| throughput (transactions a second) | 194 | 195 | +0.4% | -2.59 to 3.98 | no difference beyond the noise |
| queries a second | 3,877 | 3,891 | +0.4% | -51.9 to 79.5 | no difference beyond the noise |
| latency, 95th percentile (ms) | 9.22 | 8.04 | -12.9% | -2.33 to -0.0416 | better |
| latency, 99th percentile (ms) | 14.4 | 12 | -16.4% | -6.38 to 1.65 | no difference beyond the noise |
| latency, mean (ms) | 5.83 | 5.26 | -9.7% | -1.4 to 0.266 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 814 | +59.0% | 192 to 413 | **WORSE** |
| pages holding data, mean (MB) | 461 | 699 | +51.7% | 158 to 318 | **WORSE** |
| pages read from disk into the pool (misses) | 430,621 | 200,534 | -53.4% | -278,411 to -181,763 | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.202 | -5.6% | -0.0149 to -0.00919 | better |
| host CPU-seconds | 231 | 218 | -5.7% | -16.6 to -9.73 | better |
| host CPU-seconds per 1,000 transactions inside the line | 3.99 | 3.7 | -7.4% | -0.4 to -0.193 | better |
| buffer pool size changes written (the knob's moves) | 0 | 22.3 |  | 17.2 to 27.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
