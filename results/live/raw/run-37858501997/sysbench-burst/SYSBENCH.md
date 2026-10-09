# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.5% | -5.52 to 8.4 | no difference beyond the noise |
| throughput (transactions a second) | 292 | 294 | +0.4% | -4.06 to 6.45 | no difference beyond the noise |
| queries a second | 4,679 | 4,698 | +0.4% | -65 to 103 | no difference beyond the noise |
| latency, 95th percentile (ms) | 3.32 | 3.12 | -6.3% | -0.638 to 0.219 | no difference beyond the noise |
| latency, 99th percentile (ms) | 4.57 | 4.44 | -2.9% | -0.743 to 0.478 | no difference beyond the noise |
| latency, mean (ms) | 1.42 | 1.36 | -4.6% | -0.154 to 0.0244 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 224 | -56.3% | -292 to -285 | better |
| pages holding data, mean (MB) | 439 | 188 | -57.1% | -254 to -247 | better |
| pages read from disk into the pool (misses) | 169,531 | 301,649 | +77.9% | 128,370 to 135,867 | shown, not judged |
| host CPU busy (share of the run) | 0.1 | 0.0992 | -1.1% | -0.0117 to 0.00955 | no difference beyond the noise |
| host CPU-seconds | 40.4 | 40 | -1.0% | -4.83 to 4.04 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.36 | 1.33 | -1.6% | -0.139 to 0.0966 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
