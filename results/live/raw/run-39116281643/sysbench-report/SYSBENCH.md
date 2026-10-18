# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 291 | -0.7% | -8.58 to 4.55 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 294 | -0.6% | -6.56 to 2.91 | EVEN, no difference beyond the noise |
| queries a second | 4,731 | 4,702 | -0.6% | -105 to 46.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.54 | 5.54 | -0.0% | -0.431 to 0.429 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.18 | 8.33 | +1.8% | -1.19 to 1.5 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.28 | 3.5 | +6.5% | -0.751 to 1.18 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -71.6 to 64.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 435 | -2.6% | -114 to 90.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 246,055 | 235,902 | -4.1% | -51,337 to 31,030 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.183 | +0.5% | -0.0017 to 0.00359 | EVEN, no difference beyond the noise |
| host CPU-seconds | 100 | 101 | +0.7% | -0.632 to 2.01 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.24 | 2.27 | +1.4% | 0.00774 to 0.0544 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | 6.23 to 9.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.2% | -2.43 to 3.53 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.2% | -2.54 to 3.61 | EVEN, no difference beyond the noise |
| queries a second | 4,713 | 4,722 | +0.2% | -40.6 to 57.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.25 | 4.15 | -2.4% | -0.203 to 0.00223 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.06 | 5.95 | -1.8% | -0.37 to 0.156 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.23 | 3.19 | -1.3% | -0.142 to 0.058 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 478 | -6.6% | -126 to 57.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 434 | -6.0% | -95.8 to 40.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,806 | 715,824 | +9.5% | -189,353 to 313,389 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.191 | -0.8% | -0.00714 to 0.00417 | EVEN, no difference beyond the noise |
| host CPU-seconds | 319 | 317 | -0.6% | -11.4 to 7.42 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.37 | 2.35 | -0.8% | -0.104 to 0.067 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17 |  | 12.7 to 21.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 192 | -0.1% | -1.79 to 1.55 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.1% | -2.57 to 2.13 | EVEN, no difference beyond the noise |
| queries a second | 3,938 | 3,934 | -0.1% | -51.3 to 42.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.79 | 8.63 | -1.8% | -0.831 to 0.517 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.9 | 13 | +0.6% | -0.81 to 0.965 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.39 | 5.32 | -1.3% | -0.186 to 0.044 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 532 | +3.8% | 10.7 to 28.6 | power given |
| pages holding data, mean (MB) | 463 | 475 | +2.8% | -0.323 to 25.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 617,338 | 579,139 | -6.2% | -76,612 to 214 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.213 | -1.5% | -0.00883 to 0.00213 | EVEN, no difference beyond the noise |
| host CPU-seconds | 348 | 342 | -1.5% | -13.7 to 3.23 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.96 | 3.9 | -1.4% | -0.187 to 0.0726 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 8.74 to 23.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,954 | 2,950 | -0.1% | -9.01 to 2.47 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,956 | 2,953 | -0.1% | -8.56 to 2.62 | EVEN, no difference beyond the noise |
| queries a second | 2,956 | 2,953 | -0.1% | -8.56 to 2.62 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.334 | 0.328 | -1.8% | -0.0454 to 0.0334 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.445 | 0.435 | -2.4% | -0.052 to 0.0307 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.203 | 0.204 | +0.1% | -0.0194 to 0.0197 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 483 | -5.6% | -71.8 to 14.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 441 | -5.0% | -74.1 to 27.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,132 | 392,687 | +7.0% | -83,489 to 134,599 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.106 | -0.1% | -0.0179 to 0.0177 | EVEN, no difference beyond the noise |
| host CPU-seconds | 175 | 175 | +0.0% | -29.7 to 29.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.13 | 0.13 | +0.1% | -0.0218 to 0.0221 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | 1.17 to 22.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 21.9 | 21.7 | -1.2% | -5.73 to 5.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 986 | 984 | -0.2% | -3.48 to 0.287 | EVEN, no difference beyond the noise |
| queries a second | 986 | 984 | -0.2% | -3.48 to 0.287 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.48 | 1.55 | +4.5% | -0.0546 to 0.187 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.25 | 2.47 | +9.5% | -0.454 to 0.883 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.957 | 0.994 | +3.9% | -0.0633 to 0.137 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 478 | -6.7% | -97.6 to 29.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 398 | -12.2% | -150 to 38.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,771 | 223,612 | +18.5% | -32,318 to 102,000 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.139 | +23.1% | -0.0702 to 0.122 | EVEN, no difference beyond the noise |
| host CPU-seconds | 174 | 214 | +23.4% | -111 to 192 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 18 | 22.3 | +24.0% | -8.61 to 17.2 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 21.3 |  | 2.36 to 40.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
