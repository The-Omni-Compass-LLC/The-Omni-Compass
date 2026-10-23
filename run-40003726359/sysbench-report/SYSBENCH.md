# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 285 | 283 | -0.7% | -9.41 to 5.18 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.2% | -3.35 to 2.08 | EVEN, no difference beyond the noise |
| queries a second | 4,718 | 4,707 | -0.2% | -53.7 to 33.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.91 | 5.92 | +20.6% | -4.36 to 6.38 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 55.6 | 67.8 | +21.9% | -51.9 to 76.2 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.69 | 4.14 | +12.3% | -1.56 to 2.47 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 359 | -29.9% | -366 to 59.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 443 | 317 | -28.5% | -325 to 72.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,466 | 298,167 | +21.5% | -62,141 to 167,543 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.164 | +0.1% | -0.00561 to 0.00597 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98 | 98.1 | +0.1% | -3.3 to 3.48 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.26 | 2.28 | +0.8% | -0.0849 to 0.123 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 0.0313 to 9.97 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.3% | -0.768 to 2.76 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.3% | -0.773 to 2.74 | EVEN, no difference beyond the noise |
| queries a second | 4,703 | 4,719 | +0.3% | -12.4 to 43.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.25 | 4.18 | -1.8% | -0.0785 to -0.0735 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.67 | -2.4% | -0.289 to 0.0127 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.27 | 3.25 | -0.8% | -0.0781 to 0.0281 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 558 | +9.0% | -51 to 143 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 501 | +8.4% | -19.7 to 97.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 652,231 | 529,367 | -18.8% | -343,379 to 97,651 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.197 | -0.2% | -0.00767 to 0.0068 | EVEN, no difference beyond the noise |
| host CPU-seconds | 327 | 326 | -0.2% | -13.8 to 12.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.43 | 2.42 | -0.6% | -0.125 to 0.0966 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 2.17 to 29.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194 | 194 | +0.1% | -2.96 to 3.19 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.2% | -1.98 to 2.91 | EVEN, no difference beyond the noise |
| queries a second | 3,933 | 3,943 | +0.2% | -39.5 to 58.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.17 | 7.43 | +3.7% | -0.599 to 1.13 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 11.6 | 12.1 | +4.3% | -0.607 to 1.61 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.64 | 4.65 | +0.2% | -0.188 to 0.209 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -88.1 to 79 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 455 | -1.6% | -101 to 86.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,792 | 627,293 | +1.9% | -137,434 to 160,436 | shown, not judged |
| host CPU busy (share of the run) | 0.25 | 0.248 | -0.5% | -0.0123 to 0.00957 | EVEN, no difference beyond the noise |
| host CPU-seconds | 441 | 438 | -0.6% | -22.3 to 17.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.96 | 4.93 | -0.6% | -0.273 to 0.211 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14 |  | 5.04 to 23 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,948 | 2,948 | -0.0% | -3.85 to 2.74 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,951 | 2,951 | -0.0% | -4.17 to 3.39 | EVEN, no difference beyond the noise |
| queries a second | 2,951 | 2,951 | -0.0% | -4.17 to 3.39 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.328 | 0.312 | -4.9% | -0.0757 to 0.0437 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.44 | 0.429 | -2.5% | -0.051 to 0.029 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.195 | -3.1% | -0.0285 to 0.0161 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 472 | -7.9% | -124 to 43.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 420 | -9.4% | -118 to 31.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,730 | 423,747 | +15.5% | -86,263 to 200,297 | shown, not judged |
| host CPU busy (share of the run) | 0.1 | 0.0949 | -5.2% | -0.0286 to 0.0182 | EVEN, no difference beyond the noise |
| host CPU-seconds | 166 | 157 | -5.1% | -48 to 31 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.123 | 0.117 | -5.1% | -0.0356 to 0.023 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.67 |  | 5.87 to 13.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1.18 | 0.923 | -21.9% | -2.51 to 2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 984 | +0.0% | -9.4 to 9.79 | EVEN, no difference beyond the noise |
| queries a second | 984 | 984 | +0.0% | -9.4 to 9.79 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.1 | 2.13 | +1.7% | -0.219 to 0.29 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.91 | 5.06 | +3.0% | 0.0231 to 0.276 | LOSS |
| latency, mean (ms) | 1.19 | 1.22 | +1.9% | -0.0193 to 0.0654 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.1% | -11.9 to 12.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 445 | -1.9% | -26.6 to 9.14 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,459 | 190,222 | +0.9% | -2,917 to 6,442 | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.127 | -2.3% | -0.035 to 0.0291 | EVEN, no difference beyond the noise |
| host CPU-seconds | 199 | 195 | -2.1% | -52.2 to 43.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 535 | 463 | -13.4% | -887 to 744 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.3 |  | 10.5 to 18.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
