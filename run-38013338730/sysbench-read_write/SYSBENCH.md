# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 192 | -0.0% | -1.83 to 1.64 | no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.0% | -1.86 to 1.94 | no difference beyond the noise |
| queries a second | 3,914 | 3,915 | +0.0% | -37.2 to 38.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 7 | 7.43 | +6.2% | 0.068 to 0.797 | **WORSE** |
| latency, 99th percentile (ms) | 69.8 | 57.8 | -17.1% | -28.4 to 4.47 | no difference beyond the noise |
| latency, mean (ms) | 6.47 | 6.39 | -1.3% | -1.03 to 0.855 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 431 | -15.8% | -138 to -24.1 | better |
| pages holding data, mean (MB) | 460 | 388 | -15.8% | -120 to -24.8 | better |
| pages read from disk into the pool (misses) | 616,393 | 829,272 | +34.5% | 14,709 to 411,049 | shown, not judged |
| host CPU busy (share of the run) | 0.183 | 0.183 | -0.2% | -0.0036 to 0.00297 | no difference beyond the noise |
| host CPU-seconds | 331 | 330 | -0.2% | -6.57 to 5.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.74 | 3.74 | -0.1% | -0.0922 to 0.0824 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 6.08 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
