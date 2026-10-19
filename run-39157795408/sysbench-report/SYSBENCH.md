# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.4% | -1.1 to 3.31 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.3% | -1.36 to 2.83 | EVEN, no difference beyond the noise |
| queries a second | 4,703 | 4,715 | +0.3% | -21.7 to 45.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.41 | 5.18 | -4.1% | -0.361 to -0.0832 | GAIN |
| latency, 99th percentile (ms) | 7.52 | 7.17 | -4.7% | -0.547 to -0.159 | GAIN |
| latency, mean (ms) | 3.42 | 3.35 | -1.9% | -0.19 to 0.0624 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 479 | -6.5% | -123 to 56.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 445 | 400 | -10.1% | -119 to 29.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,823 | 256,619 | +5.2% | -41,694 to 67,286 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.197 | -0.7% | -0.0151 to 0.0122 | EVEN, no difference beyond the noise |
| host CPU-seconds | 110 | 109 | -0.7% | -8.24 to 6.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.45 | 2.43 | -1.0% | -0.174 to 0.123 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 5.52 to 10.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.1% | -2.21 to 1.76 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.1% | -2.07 to 1.64 | EVEN, no difference beyond the noise |
| queries a second | 4,720 | 4,717 | -0.1% | -33.2 to 26.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.96 | 3.86 | -2.4% | -0.193 to 0.00497 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.09 | -3.0% | -0.29 to -0.0208 | GAIN |
| latency, mean (ms) | 3.12 | 3.07 | -1.4% | -0.0861 to -0.00132 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 510 | -0.3% | -94.9 to 91.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 454 | -1.7% | -115 to 99.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,863 | 641,138 | -2.1% | -348,370 to 320,920 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.183 | -1.6% | -0.0062 to 0.000324 | EVEN, no difference beyond the noise |
| host CPU-seconds | 308 | 303 | -1.6% | -10.6 to 1.05 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.28 | 2.25 | -1.5% | -0.0855 to 0.0175 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 |  | 11.1 to 26.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 187 | 186 | -0.4% | -13.7 to 12.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 195 | -0.9% | -4.34 to 0.982 | EVEN, no difference beyond the noise |
| queries a second | 3,940 | 3,907 | -0.9% | -86.8 to 19.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 10.8 | 10.4 | -3.6% | -6.22 to 5.45 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 19.1 | 20.4 | +6.5% | -26.1 to 28.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.11 | 6.14 | +0.4% | -2.31 to 2.35 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 581 | +13.5% | -68 to 206 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 513 | +11.3% | -56 to 160 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 618,102 | 501,006 | -18.9% | -358,663 to 124,471 | shown, not judged |
| host CPU busy (share of the run) | 0.241 | 0.226 | -6.0% | -0.0571 to 0.0285 | EVEN, no difference beyond the noise |
| host CPU-seconds | 388 | 365 | -5.9% | -93.8 to 47.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.53 | 4.28 | -5.4% | -1.37 to 0.879 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 11 to 21 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,938 | 2,940 | +0.1% | -2.23 to 5.81 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,951 | -0.0% | -5.04 to 2.75 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,951 | -0.0% | -5.04 to 2.75 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.354 | 0.338 | -4.6% | -0.0378 to 0.00509 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.549 | 0.527 | -4.1% | -0.0346 to -0.0101 | GAIN |
| latency, mean (ms) | 0.215 | 0.21 | -2.4% | -0.0102 to -1.46e-05 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 492 | -4.0% | -118 to 76.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 441 | -5.0% | -99.4 to 53.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,554 | 390,022 | +6.4% | -113,387 to 160,322 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.107 | -4.2% | -0.0108 to 0.0015 | EVEN, no difference beyond the noise |
| host CPU-seconds | 185 | 178 | -4.2% | -18.5 to 3.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.138 | 0.132 | -4.2% | -0.0137 to 0.00208 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9 |  | 4.03 to 14 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7.29 | 6.1 | -16.3% | -7.05 to 4.68 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 986 | +0.3% | 2.25 to 2.83 | GAIN |
| queries a second | 983 | 986 | +0.3% | 2.25 to 2.83 | GAIN |
| latency, 95th percentile (ms) | 1.88 | 2.01 | +7.3% | -0.615 to 0.889 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.19 | 4.42 | +5.5% | -1.26 to 1.72 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.14 | -2.2% | -0.446 to 0.396 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 499 | -2.4% | -135 to 110 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 413 | -9.0% | -76.5 to -4.74 | GAIN |
| pages read from disk into the pool (misses) | 189,159 | 219,358 | +16.0% | 8,382 to 52,016 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.16 | +32.2% | -0.165 to 0.243 | EVEN, no difference beyond the noise |
| host CPU-seconds | 186 | 247 | +32.7% | -257 to 378 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 67.2 | 90.8 | +35.0% | -129 to 176 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19.7 |  | -0.414 to 39.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
