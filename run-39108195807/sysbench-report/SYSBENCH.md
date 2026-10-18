# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| throughput (transactions a second) | 82 | 80.4 | -2.0% | -7.64 to 4.35 | EVEN, no difference beyond the noise |
| queries a second | 1,313 | 1,286 | -2.0% | -122 to 69.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 19,427 | 19,661 | +1.2% | -1,099 to 1,566 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 21,131 | 21,515 | +1.8% | 364 to 404 | LOSS |
| latency, mean (ms) | 10,468 | 10,529 | +0.6% | -467 to 589 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 434 | 433 | -0.2% | -6.86 to 5.24 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 83,295 | 81,408 | -2.3% | -3,407 to -367 | shown, not judged |
| host CPU busy (share of the run) | 0.898 | 0.889 | -0.9% | -0.123 to 0.107 | EVEN, no difference beyond the noise |
| host CPU-seconds | 149 | 147 | -1.3% | -8.54 to 4.58 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 148,997 | 147,020 | -1.3% | -8,536 to 4,583 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 297 | 297 | +0.1% | -2.36 to 3.05 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 297 | 297 | +0.1% | -2.55 to 3.17 | EVEN, no difference beyond the noise |
| queries a second | 4,747 | 4,752 | +0.1% | -40.8 to 50.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.93 | 1.94 | +0.9% | -0.549 to 0.585 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.68 | 3.6 | -2.2% | -0.898 to 0.733 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.32 | 1.29 | -1.8% | -0.197 to 0.149 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 417 | -18.5% | -251 to 61.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 381 | -17.5% | -228 to 65.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 656,468 | 895,813 | +36.5% | -213,624 to 692,314 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.102 | -2.1% | -0.0148 to 0.0105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 187 | 183 | -2.1% | -26.5 to 18.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.38 | 1.35 | -2.2% | -0.185 to 0.125 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.7 |  | 6.5 to 16.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 186 | 187 | +0.3% | -3.72 to 4.87 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.1% | -2.52 to 2.27 | EVEN, no difference beyond the noise |
| queries a second | 3,913 | 3,910 | -0.1% | -50.4 to 45.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 10.6 | 10.2 | -3.6% | -2.04 to 1.27 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 199 | 163 | -18.2% | -193 to 121 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 9.46 | 8.25 | -12.8% | -5.15 to 2.73 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 542 | +5.8% | -16.8 to 76 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 485 | +5.2% | -7.25 to 55.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,152 | 554,486 | -9.9% | -204,990 to 83,659 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.213 | -1.4% | -0.00433 to -0.00182 | GAIN |
| host CPU-seconds | 389 | 384 | -1.4% | -8.14 to -2.72 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.54 | 4.46 | -1.7% | -0.212 to 0.0566 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19 |  | 7.62 to 30.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,938 | 2,937 | -0.0% | -8.52 to 6.64 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,952 | -0.0% | -10.9 to 8.06 | EVEN, no difference beyond the noise |
| queries a second | 2,954 | 2,952 | -0.0% | -10.9 to 8.06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.35 | 0.352 | +0.6% | -0.00661 to 0.0106 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.543 | 0.54 | -0.6% | -0.0159 to 0.00991 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.217 | 0.22 | +1.3% | -0.00691 to 0.0126 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 483 | -5.6% | -101 to 43.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 432 | -6.7% | -88.4 to 26.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,376 | 398,934 | +8.6% | -106,656 to 169,773 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.114 | +2.2% | -0.00769 to 0.0126 | EVEN, no difference beyond the noise |
| host CPU-seconds | 185 | 190 | +2.3% | -12.5 to 21.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.138 | 0.141 | +2.4% | -0.00902 to 0.0155 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.7 |  | 8.5 to 18.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| throughput (transactions a second) | 977 | 978 | +0.1% | -1.47 to 3.15 | EVEN, no difference beyond the noise |
| queries a second | 977 | 978 | +0.1% | -1.47 to 3.15 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.3 | 2.17 | -5.8% | -0.875 to 0.608 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 111 | 34 | -69.3% | -498 to 344 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.07 | 3.08 | -39.4% | -12.8 to 8.84 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 533 | +4.1% | -27.6 to 69.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 459 | +1.4% | -21.8 to 34.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,442 | 183,843 | -2.4% | -24,870 to 15,672 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.202 | -2.2% | -0.0244 to 0.0153 | EVEN, no difference beyond the noise |
| host CPU-seconds | 368 | 360 | -2.2% | -43.7 to 27.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 367,983 | 360,007 | -2.2% | -43,662 to 27,709 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 |  | 6.63 to 26.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
