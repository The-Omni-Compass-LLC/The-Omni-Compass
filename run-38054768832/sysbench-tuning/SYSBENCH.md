# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,910 | 2,914 | +0.1% | -10.8 to 17.7 | no difference beyond the noise |
| throughput (transactions a second) | 2,930 | 2,935 | +0.2% | -0.923 to 11.8 | no difference beyond the noise |
| queries a second | 2,930 | 2,935 | +0.2% | -0.923 to 11.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.305 | 0.332 | +8.9% | -0.112 to 0.166 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.521 | 0.531 | +1.9% | -0.118 to 0.137 | no difference beyond the noise |
| latency, mean (ms) | 0.29 | 0.157 | -45.8% | -0.645 to 0.379 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 415 | -19.0% | -306 to 112 | no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 373 | -19.3% | -281 to 102 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,291 | 502,048 | +36.7% | -189,177 to 458,691 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.115 | +1.0% | -0.0175 to 0.0197 | no difference beyond the noise |
| host CPU-seconds | 206 | 208 | +0.9% | -31.4 to 35.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.154 | 0.155 | +0.8% | -0.0239 to 0.0265 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | 10.5 to 16.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
