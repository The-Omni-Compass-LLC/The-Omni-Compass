# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 290 | -0.0% | -2.78 to 2.72 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.0% | -2.76 to 2.77 | EVEN, no difference beyond the noise |
| queries a second | 4,694 | 4,694 | +0.0% | -44.2 to 44.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.99 | 5.99 | +0.0% | -0.268 to 0.269 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.53 | 8.53 | +0.0% | 0 to 0 | EVEN, the same |
| latency, mean (ms) | 3.5 | 3.49 | -0.5% | -0.0364 to 0.00362 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.8% | 1.81 to 18.2 | power given |
| pages holding data, mean (MB) | 120 | 136 | +13.0% | 9.7 to 21.6 | power given |
| pages read from disk into the pool (misses) | 571,910 | 547,028 | -4.4% | -61,727 to 11,963 | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.2 | -0.7% | -0.00484 to 0.00208 | EVEN, no difference beyond the noise |
| host CPU-seconds | 112 | 111 | -0.7% | -2.83 to 1.21 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.52 | 2.5 | -0.7% | -0.0728 to 0.0373 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.1% | -4.63 to 5.01 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -4.64 to 4.95 | EVEN, no difference beyond the noise |
| queries a second | 4,722 | 4,724 | +0.1% | -74.3 to 79.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.25 | 4.25 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 5.91 | 5.91 | +0.0% | 0 to 0 | EVEN, the same |
| latency, mean (ms) | 3.32 | 3.3 | -0.6% | -0.0256 to -0.0127 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.7% | 7.94 to 14.4 | power given |
| pages holding data, mean (MB) | 120 | 137 | +14.1% | 12.8 to 21.2 | power given |
| pages read from disk into the pool (misses) | 1,993,614 | 1,896,842 | -4.9% | -182,474 to -11,070 | shown, not judged |
| host CPU busy (share of the run) | 0.205 | 0.205 | +0.0% | -0.00636 to 0.0065 | EVEN, no difference beyond the noise |
| host CPU-seconds | 342 | 342 | +0.1% | -10.9 to 11.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.54 | 2.54 | -0.0% | -0.0413 to 0.0411 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 |  | 6.9 to 9.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 189 | 190 | +0.4% | -3.8 to 5.19 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.0% | -3.56 to 3.75 | EVEN, no difference beyond the noise |
| queries a second | 3,916 | 3,917 | +0.0% | -71.2 to 75 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.39 | 9.22 | -1.8% | -0.579 to 0.246 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 125 | 55.8 | -55.5% | -252 to 113 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7.65 | 6.46 | -15.5% | -3.54 to 1.16 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 137 | +7.2% | 5.59 to 12.8 | power given |
| pages holding data, mean (MB) | 121 | 130 | +6.9% | 5.95 to 10.9 | power given |
| pages read from disk into the pool (misses) | 1,662,650 | 1,623,984 | -2.3% | -106,343 to 29,010 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.194 | +1.6% | -0.0117 to 0.0177 | EVEN, no difference beyond the noise |
| host CPU-seconds | 344 | 350 | +1.6% | -21.7 to 32.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.96 | 4.01 | +1.2% | -0.203 to 0.297 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,946 | 2,946 | -0.0% | -9.49 to 9.42 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,953 | +0.0% | -9.82 to 10.6 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,953 | +0.0% | -9.82 to 10.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.342 | 0.342 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 0.453 | 0.456 | +0.6% | -0.00881 to 0.0141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.208 | -0.4% | -0.00245 to 0.00086 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +8.1% | 4.15 to 16.7 | power given |
| pages holding data, mean (MB) | 121 | 134 | +10.6% | 7.24 to 18.4 | power given |
| pages read from disk into the pool (misses) | 1,028,978 | 994,835 | -3.3% | -66,610 to -1,677 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.11 | -0.7% | -0.00205 to 0.000483 | EVEN, no difference beyond the noise |
| host CPU-seconds | 184 | 183 | -0.8% | -3.69 to 0.788 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.137 | 0.136 | -0.8% | -0.0023 to 0.000161 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 81.5 | 72.7 | -10.9% | -42.8 to 25.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 981 | 980 | -0.1% | -7.95 to 6.26 | EVEN, no difference beyond the noise |
| queries a second | 981 | 980 | -0.1% | -7.95 to 6.26 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.49 | 1.55 | +4.2% | -0.319 to 0.443 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.52 | 2.8 | +11.1% | -1.24 to 1.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.919 | 0.95 | +3.4% | -0.0707 to 0.134 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 140 | +9.0% | 5.14 to 17.9 | power given |
| pages holding data, mean (MB) | 119 | 128 | +7.7% | 1.87 to 16.4 | power given |
| pages read from disk into the pool (misses) | 415,233 | 407,814 | -1.8% | -13,232 to -1,607 | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.211 | +5.3% | -0.0632 to 0.0845 | EVEN, no difference beyond the noise |
| host CPU-seconds | 356 | 375 | +5.3% | -112 to 150 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 10.1 | 11.3 | +12.1% | -6.88 to 9.33 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 8 to 8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
