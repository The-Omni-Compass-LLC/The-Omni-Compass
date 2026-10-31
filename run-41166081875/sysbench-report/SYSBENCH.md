# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.3% | -7.92 to 6.18 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.0% | -5.39 to 5.42 | EVEN, no difference beyond the noise |
| queries a second | 4,692 | 4,693 | +0.0% | -86.2 to 86.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.09 | 5.19 | +2.0% | -0.506 to 0.705 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.91 | 7.45 | +7.7% | -0.67 to 1.74 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.25 | 3.16 | -2.8% | -0.206 to 0.0267 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 977 | +663.2% | 616 to 1,081 | power given |
| pages holding data, mean (MB) | 121 | 862 | +610.5% | 607 to 874 | power given |
| pages read from disk into the pool (misses) | 603,096 | 106,694 | -82.3% | -581,695 to -411,109 | shown, not judged |
| host CPU busy (share of the run) | 0.249 | 0.242 | -3.0% | -0.00931 to -0.0055 | GAIN |
| host CPU-seconds | 148 | 144 | -3.0% | -5.54 to -3.36 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.31 | 3.22 | -2.7% | -0.156 to -0.0222 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.0% | -4.5 to 4.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.0% | -4.41 to 4.49 | EVEN, no difference beyond the noise |
| queries a second | 4,716 | 4,717 | +0.0% | -70.5 to 71.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.98 | 3.93 | -1.2% | -0.247 to 0.154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.41 | 5.47 | +1.2% | -0.0757 to 0.207 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.09 | 3 | -3.0% | -0.231 to 0.0424 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 729 | +469.4% | 476 to 726 | power given |
| pages holding data, mean (MB) | 120 | 658 | +447.0% | 437 to 638 | power given |
| pages read from disk into the pool (misses) | 1,994,149 | 319,312 | -84.0% | -1,893,443 to -1,456,231 | shown, not judged |
| host CPU busy (share of the run) | 0.244 | 0.238 | -2.6% | -0.0203 to 0.00753 | EVEN, no difference beyond the noise |
| host CPU-seconds | 434 | 423 | -2.6% | -35.5 to 12.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.22 | 3.14 | -2.6% | -0.216 to 0.0476 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | 1.87 to 9.46 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 196 | 197 | +0.8% | -1.53 to 4.75 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.5% | -1.78 to 3.74 | EVEN, no difference beyond the noise |
| queries a second | 3,937 | 3,957 | +0.5% | -35.6 to 74.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.38 | 4.2 | -22.0% | -3.76 to 1.39 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 9.29 | 6.59 | -29.0% | -11.5 to 6.08 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.52 | 2.29 | -9.2% | -0.746 to 0.282 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 483 | +277.1% | -344 to 1,053 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 122 | 421 | +246.3% | -295 to 893 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,660,441 | 839,151 | -49.5% | -2,268,262 to 625,682 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.113 | -8.9% | -0.0337 to 0.0118 | EVEN, no difference beyond the noise |
| host CPU-seconds | 220 | 200 | -8.9% | -59.7 to 20.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.46 | 2.23 | -9.6% | -0.674 to 0.2 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | -2.4 to 9.07 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,952 | 2,956 | +0.1% | -2.8 to 11.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,964 | 2,963 | -0.0% | -5.57 to 3.7 | EVEN, no difference beyond the noise |
| queries a second | 2,964 | 2,963 | -0.0% | -5.57 to 3.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.253 | 0.23 | -9.2% | -0.0464 to -0.00025 | GAIN |
| latency, 99th percentile (ms) | 0.372 | 0.361 | -3.0% | -0.0462 to 0.0242 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.27 | 0.185 | -31.5% | -0.275 to 0.105 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,181 | +823.0% | 950 to 1,156 | power given |
| pages holding data, mean (MB) | 121 | 905 | +646.4% | 750 to 817 | power given |
| pages read from disk into the pool (misses) | 1,030,291 | 88,760 | -91.4% | -975,432 to -907,630 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.112 | -6.7% | -0.0172 to 0.00107 | EVEN, no difference beyond the noise |
| host CPU-seconds | 213 | 199 | -6.7% | -30.3 to 1.91 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.159 | 0.148 | -6.8% | -0.0224 to 0.000818 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.67 |  | -0.374 to 19.7 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 3.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 282 | 344 | +22.0% | 30 to 94.1 | GAIN |
| throughput (transactions a second) | 988 | 989 | +0.1% | -8.4 to 9.58 | EVEN, no difference beyond the noise |
| queries a second | 988 | 989 | +0.1% | -8.4 to 9.58 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.01 | 3.45 | +14.7% | 0.287 to 0.595 | LOSS |
| latency, 99th percentile (ms) | 7.83 | 6.73 | -14.1% | -5.34 to 3.14 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 1.04 | -11.6% | -0.397 to 0.124 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,281 | +900.7% | 1,069 to 1,236 | power given |
| pages holding data, mean (MB) | 118 | 882 | +646.6% | 756 to 771 | power given |
| pages read from disk into the pool (misses) | 418,369 | 71,129 | -83.0% | -362,873 to -331,607 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.137 | -13.9% | -0.0353 to -0.00893 | GAIN |
| host CPU-seconds | 279 | 241 | -13.8% | -61.1 to -15.9 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.2 | 1.54 | -29.7% | -1.17 to -0.136 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
