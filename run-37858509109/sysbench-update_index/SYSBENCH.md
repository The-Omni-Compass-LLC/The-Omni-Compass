# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0.0311 | 0.0331 | +6.4% | -0.0355 to 0.0395 | no difference beyond the noise |
| throughput (transactions a second) | 911 | 899 | -1.2% | -167 to 145 | no difference beyond the noise |
| queries a second | 911 | 899 | -1.2% | -167 to 145 | no difference beyond the noise |
| latency, 95th percentile (ms) | 2,365 | 2,357 | -0.4% | -6,635 to 6,618 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3,665 | 3,867 | +5.5% | -8,601 to 9,005 | no difference beyond the noise |
| latency, mean (ms) | 459 | 391 | -14.8% | -896 to 760 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 452 | -11.7% | -356 to 237 | no difference beyond the noise |
| pages holding data, mean (MB) | 452 | 363 | -19.7% | -271 to 92.6 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 130,203 | 167,578 | +28.7% | -41,004 to 115,754 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.135 | -1.9% | -0.035 to 0.0299 | no difference beyond the noise |
| host CPU-seconds | 168 | 166 | -1.3% | -40 to 35.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 21,973 | 20,701 | -5.8% | -19,416 to 16,873 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | -0.208 to 32.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
