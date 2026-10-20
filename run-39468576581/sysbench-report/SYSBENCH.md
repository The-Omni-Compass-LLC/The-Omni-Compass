# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `80843e7684b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.4% | -3.26 to 1.15 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.4% | -3.15 to 0.83 | EVEN, no difference beyond the noise |
| queries a second | 4,718 | 4,699 | -0.4% | -50.5 to 13.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.25 | 5.28 | +0.6% | -0.327 to 0.388 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.39 | 7.34 | -0.6% | -0.239 to 0.149 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.36 | 3.36 | +0.1% | -0.0816 to 0.0882 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 520 | +1.6% | -62.4 to 79.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 448 | 434 | -3.1% | -102 to 73.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,612 | 235,727 | -4.0% | -66,842 to 47,072 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.196 | +0.6% | -0.00624 to 0.00841 | EVEN, no difference beyond the noise |
| host CPU-seconds | 107 | 108 | +0.7% | -3.51 to 5.08 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.39 | 2.42 | +1.1% | -0.0686 to 0.122 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `80843e7684b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 295 | +0.7% | -2.42 to 6.26 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.3% | -3.18 to 4.77 | EVEN, no difference beyond the noise |
| queries a second | 4,727 | 4,740 | +0.3% | -50.9 to 76.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.09 | 3.07 | -0.6% | -0.0972 to 0.0606 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 11.3 | 5.74 | -49.3% | -26.1 to 15 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.81 | 2.57 | -8.7% | -0.567 to 0.0795 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 555 | +8.4% | -64 to 150 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 491 | +6.1% | -80.8 to 138 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,415 | 557,458 | -14.9% | -352,030 to 156,115 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.188 | +0.8% | -0.00186 to 0.00471 | EVEN, no difference beyond the noise |
| host CPU-seconds | 334 | 336 | +0.7% | -3.27 to 8.14 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.5 | 2.5 | +0.1% | -0.0183 to 0.0217 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.3 |  | 9.16 to 19.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `80843e7684b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 192 | +0.1% | -2.98 to 3.44 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.2% | -1.93 to 1.03 | EVEN, no difference beyond the noise |
| queries a second | 3,925 | 3,916 | -0.2% | -38.6 to 20.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.64 | 8.28 | -4.1% | -1.45 to 0.737 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.8 | 12.4 | -3.6% | -1.6 to 0.684 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.28 | 5.18 | -1.9% | -0.384 to 0.182 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 609 | +19.0% | 32 to 162 | power given |
| pages holding data, mean (MB) | 462 | 514 | +11.2% | 14.1 to 89.2 | power given |
| pages read from disk into the pool (misses) | 612,637 | 505,974 | -17.4% | -152,265 to -61,060 | shown, not judged |
| host CPU busy (share of the run) | 0.283 | 0.276 | -2.6% | -0.0157 to 0.0011 | EVEN, no difference beyond the noise |
| host CPU-seconds | 498 | 485 | -2.6% | -27.5 to 1.97 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.67 | 5.52 | -2.7% | -0.404 to 0.101 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18 |  | 9.04 to 27 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `80843e7684b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,955 | 2,949 | -0.2% | -20.8 to 10 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,964 | -0.0% | -4.38 to 3.15 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,964 | -0.0% | -4.38 to 3.15 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.213 | 0.221 | +3.6% | -0.0182 to 0.0335 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.35 | 0.365 | +4.4% | -0.0306 to 0.0613 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.254 | 0.273 | +7.9% | -0.0826 to 0.122 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 511 | -0.2% | -72.6 to 70.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 464 | +0.2% | -59.3 to 61.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,299 | 353,785 | -3.7% | -89,895 to 62,866 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.114 | +3.7% | 0.000992 to 0.0072 | power given |
| host CPU-seconds | 195 | 202 | +3.9% | 1.97 to 13.1 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.145 | 0.151 | +3.9% | 0.000887 to 0.0105 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 0.427 to 13.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `80843e7684b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 158 | 192 | +21.9% | -42.9 to 112 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 987 | 989 | +0.2% | -2.53 to 6.31 | EVEN, no difference beyond the noise |
| queries a second | 987 | 989 | +0.2% | -2.53 to 6.31 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.53 | 2.48 | -1.8% | -0.242 to 0.149 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.88 | 4.89 | +0.1% | -0.969 to 0.98 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.02 | 1.05 | +2.3% | -0.141 to 0.187 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 450 | -12.0% | -201 to 78.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 452 | 381 | -15.8% | -176 to 33.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,589 | 234,966 | +23.9% | -50,883 to 141,637 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.123 | -3.2% | -0.0175 to 0.00932 | EVEN, no difference beyond the noise |
| host CPU-seconds | 224 | 217 | -3.2% | -30.8 to 16.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.11 | 2.51 | -19.3% | -1.69 to 0.493 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 9.43 to 22.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
