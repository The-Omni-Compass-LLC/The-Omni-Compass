# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 292 | +0.7% | -7.73 to 11.9 | no difference beyond the noise |
| throughput (transactions a second) | 292 | 294 | +0.6% | -8.5 to 12.2 | no difference beyond the noise |
| queries a second | 4,668 | 4,698 | +0.6% | -136 to 195 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.99 | 5.95 | -0.6% | -0.445 to 0.372 | no difference beyond the noise |
| latency, 99th percentile (ms) | 7.94 | 7.89 | -0.6% | -0.247 to 0.154 | no difference beyond the noise |
| latency, mean (ms) | 3.49 | 3.52 | +1.0% | -0.0294 to 0.0975 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 236 | -53.9% | -649 to 97.8 | no difference beyond the noise |
| pages holding data, mean (MB) | 438 | 200 | -54.4% | -517 to 40.8 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 167,371 | 291,275 | +74.0% | -100,582 to 348,391 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.211 | +3.8% | -0.00358 to 0.0192 | no difference beyond the noise |
| host CPU-seconds | 75.4 | 78.6 | +4.3% | -1.05 to 7.51 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.53 | 2.61 | +3.5% | 0.0343 to 0.144 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | -3.61 to 13.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.4% | -5.1 to 7.27 | no difference beyond the noise |
| throughput (transactions a second) | 292 | 293 | +0.4% | -4.99 to 7.32 | no difference beyond the noise |
| queries a second | 4,672 | 4,691 | +0.4% | -79.9 to 117 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.25 | 4.3 | +1.2% | -0.0591 to 0.162 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.64 | +0.6% | -0.256 to 0.323 | no difference beyond the noise |
| latency, mean (ms) | 3.22 | 3.25 | +1.1% | -0.0612 to 0.131 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 372 | -27.3% | -508 to 229 | no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 339 | -26.6% | -447 to 202 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 455,556 | 831,679 | +82.6% | -139,844 to 892,090 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.206 | +2.9% | -0.014 to 0.0255 | no difference beyond the noise |
| host CPU-seconds | 223 | 230 | +3.2% | -15.8 to 30.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.48 | 2.55 | +2.8% | -0.132 to 0.273 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.7 |  | -0.497 to 31.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 192 | +1.3% | -2.1 to 7.14 | no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.1% | -3.93 to 3.6 | no difference beyond the noise |
| queries a second | 3,915 | 3,912 | -0.1% | -78.5 to 72 | no difference beyond the noise |
| latency, 95th percentile (ms) | 9.33 | 8.26 | -11.5% | -3.16 to 1.01 | no difference beyond the noise |
| latency, 99th percentile (ms) | 13.6 | 11.9 | -12.9% | -5.22 to 1.71 | no difference beyond the noise |
| latency, mean (ms) | 5.56 | 5.31 | -4.6% | -0.595 to 0.0814 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 803 | +56.8% | -99.8 to 682 | no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 709 | +53.8% | -103 to 599 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 435,904 | 252,039 | -42.2% | -479,681 to 111,951 | shown, not judged |
| host CPU busy (share of the run) | 0.226 | 0.212 | -6.3% | -0.0393 to 0.0108 | no difference beyond the noise |
| host CPU-seconds | 245 | 229 | -6.4% | -43.1 to 12 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.19 | 3.87 | -7.5% | -0.871 to 0.241 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 24.7 |  | 18.9 to 30.4 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,922 | 2,921 | -0.0% | -11.8 to 8.98 | no difference beyond the noise |
| throughput (transactions a second) | 2,931 | 2,930 | -0.0% | -12.5 to 10.3 | no difference beyond the noise |
| queries a second | 2,931 | 2,930 | -0.0% | -12.5 to 10.3 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.374 | 0.374 | +0.0% | -0.0348 to 0.0348 | same |
| latency, 99th percentile (ms) | 0.482 | 0.479 | -0.6% | -0.0568 to 0.0508 | no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.212 | +0.8% | -0.0146 to 0.0179 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 437 | -14.6% | -398 to 249 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 398 | -13.8% | -358 to 230 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 262,148 | 336,355 | +28.3% | -217,662 to 366,075 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.112 | +1.9% | -0.0141 to 0.0184 | no difference beyond the noise |
| host CPU-seconds | 122 | 125 | +2.2% | -15.8 to 21.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.136 | 0.139 | +2.2% | -0.0175 to 0.0235 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 1.08 to 13.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.09 | 2.39 | -22.7% | -4.05 to 2.65 | no difference beyond the noise |
| throughput (transactions a second) | 976 | 976 | +0.0% | -2.64 to 2.69 | no difference beyond the noise |
| queries a second | 976 | 976 | +0.0% | -2.64 to 2.69 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.99 | 2.15 | +7.8% | -0.348 to 0.66 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.71 | 4 | +8.1% | -0.0843 to 0.682 | no difference beyond the noise |
| latency, mean (ms) | 1.15 | 1.17 | +2.5% | -0.118 to 0.176 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 547 | +6.9% | -79.9 to 151 | no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 440 | -1.9% | -74.4 to 56.9 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 139,278 | 147,884 | +6.2% | -34,472 to 51,685 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.175 | +25.5% | -0.0525 to 0.123 | no difference beyond the noise |
| host CPU-seconds | 144 | 181 | +25.7% | -54.5 to 129 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 226 | 273 | +20.8% | -253 to 347 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 24.3 |  | 14.9 to 33.7 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
