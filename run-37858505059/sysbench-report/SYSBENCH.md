# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 290 | -0.5% | -5.99 to 2.83 | no difference beyond the noise |
| throughput (transactions a second) | 291 | 290 | -0.5% | -5.86 to 2.85 | no difference beyond the noise |
| queries a second | 4,661 | 4,637 | -0.5% | -93.8 to 45.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.54 | 4.54 | +0.0% | -0.408 to 0.412 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.84 | 5.77 | -1.2% | -0.368 to 0.229 | no difference beyond the noise |
| latency, mean (ms) | 2.82 | 2.87 | +1.7% | -0.0096 to 0.105 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 231 | -54.9% | -306 to -256 | better |
| pages holding data, mean (MB) | 438 | 194 | -55.7% | -269 to -219 | better |
| pages read from disk into the pool (misses) | 167,008 | 294,013 | +76.0% | 89,110 to 164,900 | shown, not judged |
| host CPU busy (share of the run) | 0.222 | 0.226 | +1.5% | 0.000403 to 0.00638 | **WORSE** |
| host CPU-seconds | 89.3 | 90.7 | +1.6% | 0.231 to 2.56 | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 2.98 | 3.04 | +2.1% | 0.0448 to 0.081 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 0.798 to 6.54 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 291 | -0.2% | -1.64 to 0.196 | no difference beyond the noise |
| throughput (transactions a second) | 291 | 291 | -0.2% | -1.63 to 0.277 | no difference beyond the noise |
| queries a second | 4,663 | 4,652 | -0.2% | -26.1 to 4.43 | no difference beyond the noise |
| latency, 95th percentile (ms) | 2.7 | 2.68 | -0.6% | -0.0884 to 0.0551 | no difference beyond the noise |
| latency, 99th percentile (ms) | 4.15 | 4.1 | -1.2% | -0.159 to 0.058 | no difference beyond the noise |
| latency, mean (ms) | 1.88 | 1.86 | -0.6% | -0.067 to 0.044 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 385 | -24.7% | -493 to 240 | no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 337 | -26.9% | -413 to 165 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 458,240 | 800,796 | +74.8% | -150,858 to 835,969 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.155 | -0.6% | -0.00599 to 0.00402 | no difference beyond the noise |
| host CPU-seconds | 192 | 190 | -0.6% | -7.4 to 4.98 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.13 | 2.12 | -0.4% | -0.0708 to 0.0552 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | -4.42 to 20.4 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 100 | 95.7 | -4.3% | -20.6 to 12 | no difference beyond the noise |
| throughput (transactions a second) | 195 | 196 | +0.6% | -2.64 to 5.15 | no difference beyond the noise |
| queries a second | 3,904 | 3,929 | +0.6% | -52.7 to 103 | no difference beyond the noise |
| latency, 95th percentile (ms) | 321 | 245 | -23.8% | -248 to 95.5 | no difference beyond the noise |
| latency, 99th percentile (ms) | 755 | 454 | -39.8% | -727 to 125 | no difference beyond the noise |
| latency, mean (ms) | 68.5 | 55.5 | -19.0% | -36.9 to 10.8 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 831 | +62.3% | 220 to 418 | **WORSE** |
| pages holding data, mean (MB) | 460 | 675 | +46.8% | 58.7 to 372 | **WORSE** |
| pages read from disk into the pool (misses) | 431,327 | 241,571 | -44.0% | -386,312 to 6,801 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.185 | -4.6% | -0.0153 to -0.00242 | better |
| host CPU-seconds | 233 | 222 | -4.5% | -17.2 to -3.88 | better |
| host CPU-seconds per 1,000 transactions inside the line | 7.6 | 7.6 | -0.0% | -1.05 to 1.04 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 21.7 |  | 16.5 to 26.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 2.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,920 | 2,922 | +0.1% | -5.06 to 8.03 | no difference beyond the noise |
| throughput (transactions a second) | 2,929 | 2,933 | +0.1% | -8.8 to 15.4 | no difference beyond the noise |
| queries a second | 2,929 | 2,933 | +0.1% | -8.8 to 15.4 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.379 | 0.381 | +0.5% | -0.0475 to 0.0515 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.482 | 0.49 | +1.8% | -0.0572 to 0.0745 | no difference beyond the noise |
| latency, mean (ms) | 0.211 | 0.214 | +1.1% | -0.0253 to 0.0299 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 452 | -11.6% | -244 to 125 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 414 | -10.4% | -219 to 123 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 262,457 | 308,609 | +17.6% | -114,919 to 207,222 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.114 | +2.6% | -0.0227 to 0.0284 | no difference beyond the noise |
| host CPU-seconds | 124 | 127 | +2.8% | -25.3 to 32.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.138 | 0.141 | +2.7% | -0.0279 to 0.0355 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | 2.8 to 8.54 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0.00108 | 0 | -100.0% | -0.0057 to 0.00355 | no difference beyond the noise |
| throughput (transactions a second) | 968 | 967 | -0.1% | -7.49 to 5.99 | no difference beyond the noise |
| queries a second | 968 | 967 | -0.1% | -7.49 to 5.99 | no difference beyond the noise |
| latency, 95th percentile (ms) | 2.05 | 2.06 | +0.4% | -0.375 to 0.39 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.57 | 3.75 | +5.2% | -1.38 to 1.75 | no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.4 | +3.3% | -0.354 to 0.443 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 490 | -4.3% | -31.5 to -12.9 | better |
| pages holding data, mean (MB) | 449 | 408 | -9.1% | -70.5 to -11.1 | better |
| pages read from disk into the pool (misses) | 139,387 | 164,549 | +18.1% | 10,195 to 40,129 | shown, not judged |
| host CPU busy (share of the run) | 0.217 | 0.215 | -1.2% | -0.0347 to 0.0295 | no difference beyond the noise |
| host CPU-seconds | 262 | 259 | -1.2% | -42 to 35.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 262,043 | 258,903 | -1.2% | -42,033 to 35,753 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17.7 |  | 16.2 to 19.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
