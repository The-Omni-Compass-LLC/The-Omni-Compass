# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 289 | 288 | -0.0% | -4.49 to 4.38 | no difference beyond the noise |
| throughput (transactions a second) | 292 | 291 | -0.2% | -7.14 to 6.14 | no difference beyond the noise |
| queries a second | 4,672 | 4,664 | -0.2% | -114 to 98.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.23 | 4.1 | -2.9% | -0.659 to 0.411 | no difference beyond the noise |
| latency, 99th percentile (ms) | 31.5 | 14 | -55.5% | -132 to 96.8 | no difference beyond the noise |
| latency, mean (ms) | 3.79 | 2.71 | -28.4% | -5.39 to 3.24 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 283 | -44.8% | -368 to -91.1 | better |
| pages holding data, mean (MB) | 441 | 244 | -44.7% | -329 to -65.4 | better |
| pages read from disk into the pool (misses) | 243,999 | 363,652 | +49.0% | -33,972 to 273,279 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.164 | -0.6% | -0.00403 to 0.00202 | no difference beyond the noise |
| host CPU-seconds | 101 | 100 | -0.6% | -2.45 to 1.31 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.27 | 2.26 | -0.5% | -0.0566 to 0.032 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | 0.872 to 8.46 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 297 | 296 | -0.3% | -5.39 to 3.76 | no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.3% | -5.35 to 3.78 | no difference beyond the noise |
| queries a second | 4,751 | 4,738 | -0.3% | -85.5 to 60.5 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.95 | 1.89 | -3.0% | -0.328 to 0.21 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.62 | 3.66 | +1.1% | -0.206 to 0.288 | no difference beyond the noise |
| latency, mean (ms) | 1.29 | 1.28 | -0.8% | -0.0765 to 0.0565 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 385 | -24.8% | -159 to -94.6 | better |
| pages holding data, mean (MB) | 462 | 359 | -22.2% | -124 to -80.7 | better |
| pages read from disk into the pool (misses) | 657,571 | 1,058,917 | +61.0% | 192,402 to 610,289 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.101 | -0.2% | -0.00434 to 0.00385 | no difference beyond the noise |
| host CPU-seconds | 183 | 182 | -0.2% | -7.82 to 6.97 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.35 | 1.35 | +0.0% | -0.0694 to 0.0707 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 4.87 to 12.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 191 | -0.9% | -5.03 to 1.7 | no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.3% | -3.49 to 2.38 | no difference beyond the noise |
| queries a second | 3,945 | 3,933 | -0.3% | -69.8 to 47.5 | no difference beyond the noise |
| latency, 95th percentile (ms) | 8.79 | 9.33 | +6.2% | 0.0758 to 1.01 | **WORSE** |
| latency, 99th percentile (ms) | 13.1 | 13.7 | +4.3% | 0.201 to 0.929 | **WORSE** |
| latency, mean (ms) | 5.41 | 5.51 | +1.9% | -0.0985 to 0.3 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 487 | -4.8% | -135 to 85.9 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 427 | -7.4% | -90.7 to 22 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,576 | 695,914 | +13.1% | -144,768 to 305,444 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.224 | +2.0% | -0.00351 to 0.0122 | no difference beyond the noise |
| host CPU-seconds | 354 | 361 | +2.2% | -6.07 to 21.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.02 | 4.14 | +3.1% | -0.0962 to 0.342 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 23.3 |  | 19.5 to 27.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,950 | 2,948 | -0.1% | -14.1 to 10.9 | no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,951 | -0.0% | -14 to 11.8 | no difference beyond the noise |
| queries a second | 2,952 | 2,951 | -0.0% | -14 to 11.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.332 | 0.324 | -2.4% | -0.0308 to 0.0148 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.432 | 0.424 | -1.9% | -0.0468 to 0.0302 | no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.201 | -0.1% | -0.00985 to 0.00949 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 450 | -12.0% | -110 to -13.3 | better |
| pages holding data, mean (MB) | 464 | 406 | -12.4% | -101 to -14.5 | better |
| pages read from disk into the pool (misses) | 365,499 | 452,894 | +23.9% | -25,925 to 200,714 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.103 | +0.8% | -0.0083 to 0.00993 | no difference beyond the noise |
| host CPU-seconds | 169 | 171 | +1.0% | -13.5 to 16.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.125 | 0.126 | +1.0% | -0.00943 to 0.012 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.7 |  | 5.41 to 17.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0.00217 | 0.00217 | +0.0% | -0.0054 to 0.0054 | no difference beyond the noise |
| throughput (transactions a second) | 976 | 976 | +0.0% | -3.92 to 4.3 | no difference beyond the noise |
| queries a second | 976 | 976 | +0.0% | -3.92 to 4.3 | no difference beyond the noise |
| latency, 95th percentile (ms) | 2.66 | 2.58 | -2.9% | -0.258 to 0.101 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.31 | 5.21 | -1.8% | -0.505 to 0.311 | no difference beyond the noise |
| latency, mean (ms) | 1.5 | 1.55 | +3.3% | -0.303 to 0.403 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 377 | -26.4% | -238 to -32.6 | better |
| pages holding data, mean (MB) | 453 | 314 | -30.5% | -233 to -43.3 | better |
| pages read from disk into the pool (misses) | 189,848 | 286,680 | +51.0% | 57,074 to 136,589 | shown, not judged |
| host CPU busy (share of the run) | 0.166 | 0.164 | -1.1% | -0.0163 to 0.0127 | no difference beyond the noise |
| host CPU-seconds | 297 | 294 | -1.1% | -29.4 to 23 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 297,183 | 244,952 | -17.6% | -249,523 to 145,060 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19.3 |  | 6.58 to 32.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
