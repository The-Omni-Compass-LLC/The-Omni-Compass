# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 294 | +0.5% | -4.46 to 7.27 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 294 | +0.5% | -4.26 to 7.08 | EVEN, no difference beyond the noise |
| queries a second | 4,677 | 4,699 | +0.5% | -68.2 to 113 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.25 | 3.13 | -3.5% | -0.361 to 0.131 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.94 | 4.74 | -4.1% | -0.532 to 0.126 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.76 | 1.75 | -0.2% | -0.0548 to 0.0492 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 426 | -16.8% | -117 to -54.3 | GAIN |
| pages holding data, mean (MB) | 444 | 381 | -14.1% | -95.9 to -29.4 | GAIN |
| pages read from disk into the pool (misses) | 246,175 | 263,243 | +6.9% | 4,760 to 29,376 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.135 | +1.2% | -0.00226 to 0.00558 | EVEN, no difference beyond the noise |
| host CPU-seconds | 81.1 | 82.1 | +1.3% | -1.41 to 3.45 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.81 | 1.82 | +0.8% | -0.0268 to 0.0549 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 3.52 to 8.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.0% | -4.7 to 4.67 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.0% | -4.65 to 4.66 | EVEN, no difference beyond the noise |
| queries a second | 4,726 | 4,726 | +0.0% | -74.3 to 74.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.03 | 4.05 | +0.6% | -0.0804 to 0.129 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.5 | 5.47 | -0.6% | -0.171 to 0.107 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.16 | 3.17 | +0.4% | -0.0182 to 0.0456 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 398 | -22.2% | -164 to -63.2 | GAIN |
| pages holding data, mean (MB) | 462 | 363 | -21.4% | -158 to -39.2 | GAIN |
| pages read from disk into the pool (misses) | 654,264 | 933,120 | +42.6% | 183,525 to 374,187 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.19 | +2.0% | -0.000345 to 0.00798 | EVEN, no difference beyond the noise |
| host CPU-seconds | 308 | 316 | +2.4% | 0.0641 to 14.6 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.28 | 2.34 | +2.4% | 0.0123 to 0.0957 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 9.67 |  | 6.8 to 12.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 197 | +0.6% | -3.06 to 5.29 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.6% | -2.49 to 4.73 | EVEN, no difference beyond the noise |
| queries a second | 3,942 | 3,964 | +0.6% | -49.7 to 94.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.58 | 4.49 | -1.9% | -0.437 to 0.265 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 9.44 | 9.3 | -1.4% | -2.51 to 2.24 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.64 | 2.66 | +0.7% | -0.165 to 0.2 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 546 | +6.6% | -51.3 to 119 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 490 | +6.0% | -44.5 to 100 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,437 | 542,396 | -11.7% | -270,539 to 126,458 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.114 | -2.4% | -0.0137 to 0.00795 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 203 | -2.4% | -24.1 to 14 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.34 | 2.27 | -3.0% | -0.235 to 0.0956 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.7 |  | 2.92 to 28.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 5.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,962 | +0.0% | -4.01 to 4.97 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,964 | -0.0% | -3.61 to 3.17 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,964 | -0.0% | -3.61 to 3.17 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.183 | 0.146 | -19.9% | -0.0928 to 0.0202 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.338 | 0.305 | -9.8% | -0.0852 to 0.0192 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0924 | 0.0868 | -6.1% | -0.0311 to 0.0199 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 450 | -12.1% | -240 to 116 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 411 | -11.3% | -233 to 128 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,864 | 437,961 | +19.1% | -159,918 to 300,113 | shown, not judged |
| host CPU busy (share of the run) | 0.0713 | 0.0674 | -5.5% | -0.0278 to 0.0199 | EVEN, no difference beyond the noise |
| host CPU-seconds | 128 | 121 | -5.4% | -49.4 to 35.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0948 | 0.0896 | -5.4% | -0.0365 to 0.0262 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | -0.058 to 17.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 90.8 | 89.3 | -1.7% | -38.1 to 35 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 984 | +0.0% | -2.61 to 2.79 | EVEN, no difference beyond the noise |
| queries a second | 984 | 984 | +0.0% | -2.61 to 2.79 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.31 | 1.28 | -1.9% | -0.185 to 0.135 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.27 | 2.24 | -1.6% | -0.605 to 0.533 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.878 | 0.868 | -1.1% | -0.0935 to 0.0738 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 454 | 451 | -0.6% | -15.8 to 10.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,829 | 187,329 | -1.3% | -12,566 to 7,566 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.193 | -2.1% | -0.0319 to 0.0238 | EVEN, no difference beyond the noise |
| host CPU-seconds | 341 | 334 | -2.0% | -54.6 to 40.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 8.66 | 8.25 | -4.7% | -4.86 to 4.04 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
