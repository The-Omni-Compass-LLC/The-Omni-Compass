# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 289 | 288 | -0.6% | -20 to 16.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.4% | -7.14 to 4.83 | EVEN, no difference beyond the noise |
| queries a second | 4,747 | 4,728 | -0.4% | -114 to 77.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.6 | 4.63 | +0.6% | -1.92 to 1.97 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 52 | 48.1 | -7.5% | -101 to 93 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.74 | 3.54 | -5.2% | -2.25 to 1.86 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 501 | -2.1% | -48 to 26.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 451 | +0.5% | -26.7 to 31.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 246,524 | 226,998 | -7.9% | -23,982 to -15,071 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.178 | -0.7% | -0.009 to 0.00635 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 108 | -0.9% | -5.46 to 3.53 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.47 | 2.46 | -0.2% | -0.131 to 0.122 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 |  | 6.9 to 9.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.2% | -1.24 to 2.13 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.2% | -1.39 to 2.45 | EVEN, no difference beyond the noise |
| queries a second | 4,713 | 4,721 | +0.2% | -22.3 to 39.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.2 | 4.13 | -1.8% | -0.0768 to -0.0739 | GAIN |
| latency, 99th percentile (ms) | 5.95 | 5.88 | -1.2% | -0.225 to 0.0821 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.21 | 3.18 | -0.8% | -0.063 to 0.01 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 565 | +10.4% | -49.8 to 156 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 489 | +5.8% | -90.6 to 144 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 652,067 | 561,980 | -13.8% | -380,177 to 200,003 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.19 | -0.6% | -0.00561 to 0.00316 | EVEN, no difference beyond the noise |
| host CPU-seconds | 316 | 314 | -0.6% | -9.45 to 5.72 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.35 | 2.33 | -0.7% | -0.0644 to 0.0301 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 11 to 21 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 195 | +0.2% | -0.837 to 1.53 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.1% | -1.86 to 2.24 | EVEN, no difference beyond the noise |
| queries a second | 3,923 | 3,927 | +0.1% | -37.2 to 44.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.67 | 6.47 | -2.9% | -0.935 to 0.543 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.2 | 9.97 | -2.4% | -1.55 to 1.06 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.42 | 4.39 | -0.7% | -0.119 to 0.0586 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 613 | +19.7% | -61.9 to 264 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 524 | +13.4% | -20.8 to 145 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,071 | 485,713 | -21.0% | -239,001 to -19,716 | shown, not judged |
| host CPU busy (share of the run) | 0.244 | 0.241 | -1.2% | -0.007 to 0.00116 | EVEN, no difference beyond the noise |
| host CPU-seconds | 431 | 426 | -1.2% | -12.6 to 2.47 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.83 | 4.77 | -1.4% | -0.122 to -0.00959 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 20.7 |  | 6.54 to 34.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,932 | 2,940 | +0.3% | -7.25 to 22.5 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,952 | -0.0% | -8.17 to 8.07 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,952 | -0.0% | -8.17 to 8.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.382 | 0.351 | -8.1% | -0.108 to 0.0465 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.544 | 0.489 | -10.2% | -0.195 to 0.0837 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.23 | 0.216 | -6.1% | -0.0644 to 0.0366 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 528 | +3.0% | -80 to 111 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 474 | +2.1% | -74 to 93.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,941 | 338,458 | -7.8% | -99,272 to 42,306 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.111 | -7.9% | -0.0457 to 0.0265 | EVEN, no difference beyond the noise |
| host CPU-seconds | 201 | 185 | -7.9% | -76.3 to 44.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.15 | 0.138 | -8.1% | -0.0576 to 0.0333 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 |  | 2.08 to 14.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0.0145 | 0.0159 | +10.0% | -0.021 to 0.0239 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 975 | 975 | -0.1% | -9.35 to 8.25 | EVEN, no difference beyond the noise |
| queries a second | 975 | 975 | -0.1% | -9.35 to 8.25 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.88 | 1.81 | -3.6% | -0.224 to 0.087 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.55 | 3.33 | -6.1% | -1.34 to 0.907 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.52 | 1.47 | -3.7% | -1.15 to 1.04 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 495 | -3.3% | -168 to 134 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 432 | -4.8% | -161 to 117 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,661 | 204,620 | +7.9% | -46,472 to 76,390 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.159 | -3.0% | -0.018 to 0.00825 | EVEN, no difference beyond the noise |
| host CPU-seconds | 294 | 285 | -3.0% | -32.6 to 15.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 48,677 | 45,413 | -6.7% | -91,296 to 84,768 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 10.2 to 20.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
