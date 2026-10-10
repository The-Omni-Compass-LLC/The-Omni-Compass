# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,945 | -0.0% | -5.76 to 4.47 | no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,952 | -0.1% | -3.15 to -0.502 | **WORSE** |
| queries a second | 2,954 | 2,952 | -0.1% | -3.15 to -0.502 | **WORSE** |
| latency, 95th percentile (ms) | 0.334 | 0.35 | +4.9% | -0.000208 to 0.0329 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.473 | 0.473 | +0.0% | -0.0199 to 0.0199 | same |
| latency, mean (ms) | 0.23 | 0.216 | -6.1% | -0.0841 to 0.0561 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 440 | -14.1% | -128 to -16.9 | better |
| pages holding data, mean (MB) | 463 | 399 | -14.0% | -93.6 to -36.3 | better |
| pages read from disk into the pool (misses) | 367,507 | 454,443 | +23.7% | 6,769 to 167,103 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.116 | +13.0% | 0.00804 to 0.0185 | **WORSE** |
| host CPU-seconds | 170 | 192 | +13.4% | 13.5 to 31.9 | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.126 | 0.143 | +13.4% | 0.00991 to 0.0238 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 2.16 to 12.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
