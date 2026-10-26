# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.3% | -4.23 to 2.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.5% | -4.96 to 1.98 | EVEN, no difference beyond the noise |
| queries a second | 4,740 | 4,716 | -0.5% | -79.4 to 31.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.6 | 5.5 | -1.8% | -0.537 to 0.335 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.18 | 7.84 | -4.1% | -0.747 to 0.075 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.33 | 3.32 | -0.4% | -0.0525 to 0.0271 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 436 | -14.8% | -77.2 to -73.9 | GAIN |
| pages holding data, mean (MB) | 444 | 392 | -11.8% | -56.4 to -48.6 | GAIN |
| pages read from disk into the pool (misses) | 245,210 | 258,690 | +5.5% | 35.2 to 26,925 | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.189 | -0.2% | -0.00872 to 0.00804 | EVEN, no difference beyond the noise |
| host CPU-seconds | 104 | 104 | -0.0% | -4.88 to 4.84 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.32 | 2.33 | +0.3% | -0.115 to 0.128 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 7 to 7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 296 | +0.4% | -2.15 to 4.72 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.4% | -2.02 to 4.4 | EVEN, no difference beyond the noise |
| queries a second | 4,715 | 4,734 | +0.4% | -32.3 to 70.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.23 | 4.15 | -1.8% | -0.263 to 0.112 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.17 | 6.02 | -2.4% | -0.557 to 0.267 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.2 | 3.2 | -0.1% | -0.0443 to 0.0357 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 461 | -10.0% | -141 to 38.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 426 | -7.8% | -120 to 47.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,617 | 774,070 | +18.4% | -143,326 to 384,233 | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.192 | +1.5% | -0.000136 to 0.00564 | EVEN, no difference beyond the noise |
| host CPU-seconds | 313 | 318 | +1.7% | -0.264 to 10.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.32 | 2.35 | +1.2% | -0.0269 to 0.0842 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 9.46 to 15.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 192 | -0.1% | -1.68 to 1.39 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.2% | -2.1 to 1.14 | EVEN, no difference beyond the noise |
| queries a second | 3,934 | 3,924 | -0.2% | -41.9 to 22.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.48 | 8.28 | -2.4% | -0.632 to 0.231 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.3 | 12.2 | -0.6% | -0.389 to 0.242 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.29 | 5.25 | -0.7% | -0.164 to 0.0903 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 546 | +6.7% | -78.8 to 147 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 489 | +5.9% | -47.7 to 102 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,859 | 542,119 | -12.0% | -247,471 to 99,990 | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.212 | -1.1% | -0.0127 to 0.00806 | EVEN, no difference beyond the noise |
| host CPU-seconds | 345 | 341 | -0.9% | -20.4 to 14 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.91 | 3.88 | -0.9% | -0.254 to 0.186 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 20.7 |  | 17.8 to 23.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,923 | 2,924 | +0.0% | -4.89 to 6.37 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,931 | 2,932 | +0.0% | -2.95 to 4.33 | EVEN, no difference beyond the noise |
| queries a second | 2,931 | 2,932 | +0.0% | -2.95 to 4.33 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.228 | 0.222 | -2.5% | -0.0268 to 0.0155 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.482 | 0.476 | -1.2% | -0.0318 to 0.0198 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.185 | 0.175 | -5.5% | -0.234 to 0.213 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 519 | +1.5% | -123 to 138 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 465 | +0.4% | -111 to 114 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,533 | 349,101 | -5.0% | -153,227 to 116,363 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.116 | -0.5% | -0.014 to 0.0129 | EVEN, no difference beyond the noise |
| host CPU-seconds | 211 | 210 | -0.4% | -24.8 to 23.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.157 | 0.156 | -0.4% | -0.0183 to 0.0169 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 |  | -2.35 to 25 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1.09 | 3.24 | +196.6% | -1.88 to 6.18 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 983 | -0.0% | -3.13 to 3.12 | EVEN, no difference beyond the noise |
| queries a second | 983 | 983 | -0.0% | -3.13 to 3.12 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.95 | 1.71 | -42.1% | -3.1 to 0.613 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.33 | 2.92 | -45.2% | -4.82 to 0.000279 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.5 | 1.07 | -28.6% | -0.892 to 0.0314 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 455 | 451 | -0.8% | -14.2 to 6.73 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,970 | 186,964 | -1.1% | -9,200 to 5,187 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.134 | -38.0% | -0.169 to 0.00481 | EVEN, no difference beyond the noise |
| host CPU-seconds | 330 | 205 | -37.9% | -264 to 13.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 9,732 | 285 | -97.1% | -30,028 to 11,135 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
