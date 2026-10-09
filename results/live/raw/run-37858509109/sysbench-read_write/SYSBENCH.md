# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 125 | 127 | +1.8% | -77 to 81.3 | no difference beyond the noise |
| throughput (transactions a second) | 195 | 196 | +0.6% | -1.74 to 4.23 | no difference beyond the noise |
| queries a second | 3,893 | 3,918 | +0.6% | -34.9 to 84.7 | no difference beyond the noise |
| latency, 95th percentile (ms) | 189 | 192 | +1.7% | -271 to 278 | no difference beyond the noise |
| latency, 99th percentile (ms) | 440 | 542 | +23.1% | -447 to 651 | no difference beyond the noise |
| latency, mean (ms) | 40.2 | 44.6 | +11.0% | -64.2 to 73.1 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 833 | +62.6% | -11.1 to 652 | no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 662 | +43.7% | 85.6 to 317 | **WORSE** |
| pages read from disk into the pool (misses) | 430,616 | 259,436 | -39.8% | -295,264 to -47,097 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.185 | -4.1% | -0.0149 to -0.000826 | better |
| host CPU-seconds | 232 | 222 | -4.2% | -16.3 to -3.02 | better |
| host CPU-seconds per 1,000 transactions inside the line | 6.07 | 5.83 | -3.9% | -3.52 to 3.04 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19.7 |  | 15.9 to 23.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
