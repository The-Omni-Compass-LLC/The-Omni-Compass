# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 284 | -2.0% | -22.8 to 11.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.1% | -5.91 to 5.29 | EVEN, no difference beyond the noise |
| queries a second | 4,726 | 4,721 | -0.1% | -94.6 to 84.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.06 | 5.1 | +25.5% | -3.28 to 5.36 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 28.7 | 128 | +345.3% | -30 to 228 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.98 | 6.55 | +119.9% | -0.909 to 8.05 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 478 | -6.6% | -86.9 to 19.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 432 | -3.4% | -70.1 to 39.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 246,297 | 247,730 | +0.6% | -20,566 to 23,433 | shown, not judged |
| host CPU busy (share of the run) | 0.162 | 0.164 | +1.2% | -0.00458 to 0.0086 | EVEN, no difference beyond the noise |
| host CPU-seconds | 96.9 | 98.1 | +1.3% | -2.54 to 5.06 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.19 | 2.27 | +3.4% | -0.0429 to 0.19 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 5.23 to 8.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | -0.1% | -1.59 to 1.27 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.0% | -1.54 to 1.37 | EVEN, no difference beyond the noise |
| queries a second | 4,701 | 4,700 | -0.0% | -24.7 to 21.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.13 | 3.13 | -0.0% | -0.14 to 0.138 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.33 | 4.3 | -0.6% | -0.475 to 0.421 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.4 | 2.43 | +1.0% | -0.0824 to 0.133 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 440 | -14.2% | -216 to 70.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 394 | -14.8% | -138 to 1.07 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 651,863 | 850,963 | +30.5% | -68,603 to 466,802 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.195 | +1.3% | -0.00673 to 0.0117 | EVEN, no difference beyond the noise |
| host CPU-seconds | 349 | 353 | +1.3% | -12.6 to 21.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.58 | 2.62 | +1.3% | -0.079 to 0.147 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17 |  | 12 to 22 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 144 | 157 | +8.9% | -26.4 to 52 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.4% | -3.97 to 2.52 | EVEN, no difference beyond the noise |
| queries a second | 3,955 | 3,941 | -0.4% | -79.5 to 50.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 148 | 109 | -26.1% | -168 to 91.4 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 355 | 295 | -16.7% | -466 to 347 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 29.3 | 21.7 | -25.8% | -35.8 to 20.7 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 480 | -6.2% | -82.5 to 18.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 429 | -7.0% | -59.7 to -5.17 | GAIN |
| pages read from disk into the pool (misses) | 617,284 | 692,914 | +12.3% | -70,398 to 221,657 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.182 | +0.3% | -0.00542 to 0.00637 | EVEN, no difference beyond the noise |
| host CPU-seconds | 324 | 324 | +0.2% | -8.15 to 9.33 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.94 | 4.56 | -7.8% | -1.47 to 0.696 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17.7 |  | 11.4 to 23.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 3.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,957 | 2,958 | +0.0% | -15.5 to 17.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,961 | 2,963 | +0.1% | -14.5 to 18.8 | EVEN, no difference beyond the noise |
| queries a second | 2,961 | 2,963 | +0.1% | -14.5 to 18.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.195 | 0.206 | +6.0% | -0.0222 to 0.0456 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.334 | 0.336 | +0.6% | -0.00661 to 0.0106 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.108 | 0.106 | -2.2% | -0.00644 to 0.00177 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 423 | -17.4% | -175 to -3.01 | GAIN |
| pages holding data, mean (MB) | 464 | 380 | -18.1% | -191 to 23.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,662 | 483,832 | +31.6% | -69,233 to 301,572 | shown, not judged |
| host CPU busy (share of the run) | 0.0832 | 0.0803 | -3.5% | -0.0209 to 0.015 | EVEN, no difference beyond the noise |
| host CPU-seconds | 149 | 144 | -3.5% | -37.2 to 26.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.111 | 0.107 | -3.5% | -0.0277 to 0.02 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | 6.03 to 16 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 9.46 | 10.7 | +13.5% | -3.82 to 6.38 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 985 | 984 | -0.0% | -8.7 to 8.04 | EVEN, no difference beyond the noise |
| queries a second | 985 | 984 | -0.0% | -8.7 to 8.04 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.65 | 1.62 | -2.0% | -0.239 to 0.173 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.37 | 3.45 | +2.4% | -0.144 to 0.308 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1.04 | -1.3% | -0.0948 to 0.068 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 475 | -7.2% | -67.6 to -6.26 | GAIN |
| pages holding data, mean (MB) | 453 | 407 | -10.2% | -64 to -28.3 | GAIN |
| pages read from disk into the pool (misses) | 189,518 | 213,686 | +12.8% | -2,948 to 51,284 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.116 | -5.6% | -0.0408 to 0.027 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 179 | -5.4% | -61.3 to 40.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 48.5 | 36.8 | -24.2% | -62.4 to 39 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17.3 |  | 12.2 to 22.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
