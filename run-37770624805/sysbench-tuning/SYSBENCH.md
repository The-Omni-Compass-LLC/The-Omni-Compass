# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,920 | 2,914 | -0.2% | -19.9 to 7.2 | no difference beyond the noise |
| throughput (transactions a second) | 2,929 | 2,927 | -0.1% | -10.9 to 6.35 | no difference beyond the noise |
| queries a second | 2,929 | 2,927 | -0.1% | -10.9 to 6.35 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.372 | 0.395 | +6.2% | -0.0195 to 0.0655 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.49 | 0.508 | +3.7% | -0.0267 to 0.0627 | no difference beyond the noise |
| latency, mean (ms) | 0.219 | 0.241 | +10.4% | -0.046 to 0.0915 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 628 | +22.6% | -655 to 886 | no difference beyond the noise |
| pages holding data, mean (MB) | 468 | 519 | +10.8% | -436 to 536 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 264,686 | 281,205 | +6.2% | -211,725 to 244,763 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.122 | +2.4% | -0.021 to 0.0268 | no difference beyond the noise |
| host CPU-seconds | 132 | 135 | +2.4% | -23.4 to 29.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.151 | +2.6% | -0.0264 to 0.0342 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | 1.17 to 22.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
