# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | -0.0% | -4.2 to 4.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.0% | -4.33 to 4.14 | EVEN, no difference beyond the noise |
| queries a second | 4,700 | 4,699 | -0.0% | -69.3 to 66.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.09 | 5.12 | +0.6% | -0.102 to 0.164 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.79 | 6.83 | +0.6% | -0.308 to 0.392 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.38 | 3.37 | -0.3% | -0.0616 to 0.0399 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.5% | -0.0902 to 19.2 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 135 | +12.2% | 10.4 to 19 | power given |
| pages read from disk into the pool (misses) | 572,588 | 543,189 | -5.1% | -94,336 to 35,538 | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.201 | -0.2% | -0.00513 to 0.00431 | EVEN, no difference beyond the noise |
| host CPU-seconds | 112 | 112 | -0.3% | -2.79 to 2.18 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.5 | 2.49 | -0.2% | -0.0304 to 0.0182 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.1% | -3.14 to 2.42 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.1% | -3.17 to 2.47 | EVEN, no difference beyond the noise |
| queries a second | 4,720 | 4,715 | -0.1% | -50.7 to 39.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.1 | 4.13 | +0.6% | -0.0826 to 0.133 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.54 | 5.5 | -0.6% | -0.171 to 0.107 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.24 | 3.24 | +0.0% | -0.071 to 0.0716 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.3% | 1.92 to 19.4 | power given |
| pages holding data, mean (MB) | 120 | 137 | +14.1% | 11.4 to 22.5 | power given |
| pages read from disk into the pool (misses) | 1,975,999 | 1,905,467 | -3.6% | -154,606 to 13,542 | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.202 | +0.0% | -0.00824 to 0.00824 | EVEN, no difference beyond the noise |
| host CPU-seconds | 336 | 336 | +0.0% | -14 to 14.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.49 | 2.49 | +0.1% | -0.0962 to 0.102 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 196 | +0.2% | -4 to 4.65 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | +0.1% | -4.03 to 4.43 | EVEN, no difference beyond the noise |
| queries a second | 3,955 | 3,959 | +0.1% | -80.7 to 88.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.89 | 7.84 | -0.6% | -0.253 to 0.157 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 11.2 | 11.1 | -0.6% | -0.355 to 0.221 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.97 | 4.01 | +1.1% | -0.102 to 0.187 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.5% | 2.66 to 11.4 | power given |
| pages holding data, mean (MB) | 122 | 127 | +4.2% | 3.15 to 7.19 | power given |
| pages read from disk into the pool (misses) | 1,670,787 | 1,639,449 | -1.9% | -139,779 to 77,102 | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.201 | +0.1% | -0.00556 to 0.00577 | EVEN, no difference beyond the noise |
| host CPU-seconds | 356 | 356 | +0.1% | -9.33 to 9.79 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4 | 3.99 | -0.1% | -0.0637 to 0.0556 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,964 | 2,960 | -0.1% | -5.34 to -3.11 | LOSS |
| throughput (transactions a second) | 2,968 | 2,965 | -0.1% | -10.9 to 4.13 | EVEN, no difference beyond the noise |
| queries a second | 2,968 | 2,965 | -0.1% | -10.9 to 4.13 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.192 | 0.194 | +1.4% | -0.106 to 0.111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.312 | 0.311 | -0.5% | -0.0231 to 0.0198 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0904 | 0.0879 | -2.7% | -0.0213 to 0.0164 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.8% | -2.66 to 17.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 133 | +9.3% | -2.93 to 25.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,029,216 | 1,011,793 | -1.7% | -43,324 to 8,478 | shown, not judged |
| host CPU busy (share of the run) | 0.0695 | 0.0679 | -2.2% | -0.0179 to 0.0148 | EVEN, no difference beyond the noise |
| host CPU-seconds | 124 | 122 | -2.2% | -32.1 to 26.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0923 | 0.0903 | -2.1% | -0.0236 to 0.0198 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.08 | 2.2 | -28.5% | -2.32 to 0.573 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 982 | -0.2% | -5.61 to 1.3 | EVEN, no difference beyond the noise |
| queries a second | 984 | 982 | -0.2% | -5.61 to 1.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.32 | 2.66 | +14.5% | -1.57 to 2.25 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.03 | 4.8 | +19.1% | -4.47 to 6.01 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.22 | 1.3 | +6.4% | -0.461 to 0.617 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 159 | +24.1% | -38.3 to 100 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 118 | 141 | +19.0% | -42.3 to 87.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 416,099 | 393,476 | -5.4% | -72,705 to 27,459 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.266 | +30.8% | -0.234 to 0.359 | EVEN, no difference beyond the noise |
| host CPU-seconds | 314 | 413 | +31.5% | -367 to 564 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 251 | 432 | +71.9% | -428 to 790 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 7.8 to 13.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
