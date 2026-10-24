# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.0% | -3.66 to 3.72 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | -0.1% | -4.02 to 3.35 | EVEN, no difference beyond the noise |
| queries a second | 4,693 | 4,687 | -0.1% | -64.3 to 53.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.65 | 4.57 | -1.8% | -0.442 to 0.275 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.63 | 6.32 | -4.7% | -1.04 to 0.421 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.07 | 3.04 | -0.9% | -0.15 to 0.092 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 528 | +3.2% | -71.5 to 104 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 478 | +6.4% | -34 to 91.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,251 | 227,519 | -6.9% | -68,579 to 35,115 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.17 | -0.9% | -0.0034 to 0.000146 | EVEN, no difference beyond the noise |
| host CPU-seconds | 95.1 | 94.1 | -1.1% | -2.47 to 0.427 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.12 | 2.1 | -1.0% | -0.0703 to 0.0296 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 2.7 to 11.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | +0.2% | -2 to 3.13 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | +0.2% | -2.32 to 3.31 | EVEN, no difference beyond the noise |
| queries a second | 4,733 | 4,741 | +0.2% | -37.2 to 52.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2 | 1.96 | -1.8% | -0.21 to 0.14 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.82 | 3.82 | +0.1% | -0.299 to 0.305 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.31 | -2.9% | -0.111 to 0.0335 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 437 | -14.7% | -164 to 13.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 396 | -14.3% | -134 to 1.96 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 652,955 | 802,847 | +23.0% | -109,883 to 409,668 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.104 | -2.2% | -0.00952 to 0.00492 | EVEN, no difference beyond the noise |
| host CPU-seconds | 191 | 187 | -2.2% | -17.1 to 8.86 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.42 | 1.38 | -2.3% | -0.126 to 0.0595 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | -3.35 to 24 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 192 | +0.1% | -1.77 to 2.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.2% | -1.8 to 1.16 | EVEN, no difference beyond the noise |
| queries a second | 3,933 | 3,927 | -0.2% | -36 to 23.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.11 | 8.84 | -3.0% | -0.733 to 0.195 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.5 | 13.1 | -2.4% | -1.21 to 0.578 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.44 | 5.4 | -0.8% | -0.467 to 0.374 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 611 | +19.4% | -24.1 to 223 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 534 | +15.5% | 9.98 to 133 | power given |
| pages read from disk into the pool (misses) | 615,998 | 468,136 | -24.0% | -353,490 to 57,766 | shown, not judged |
| host CPU busy (share of the run) | 0.213 | 0.206 | -3.0% | -0.0154 to 0.00241 | EVEN, no difference beyond the noise |
| host CPU-seconds | 342 | 332 | -3.0% | -25.6 to 5.26 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.9 | 3.78 | -3.1% | -0.272 to 0.0322 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17.3 |  | 9.74 to 24.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,666 | 2,770 | +3.9% | -113 to 323 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,937 | 2,932 | -0.2% | -12.3 to 2.85 | EVEN, no difference beyond the noise |
| queries a second | 2,937 | 2,932 | -0.2% | -12.3 to 2.85 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 795 | 2.61 | -99.7% | -3,231 to 1,646 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4,136 | 648 | -84.3% | -7,978 to 1,000 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 149 | 19.7 | -86.7% | -365 to 107 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 542 | +5.9% | -148 to 208 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 472 | +2.1% | -125 to 145 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,832 | 346,051 | -5.9% | -215,709 to 172,146 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.135 | -0.4% | -0.0255 to 0.0244 | EVEN, no difference beyond the noise |
| host CPU-seconds | 244 | 243 | -0.4% | -45.1 to 42.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.199 | 0.191 | -4.2% | -0.0561 to 0.0392 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.3 |  | 6.35 to 22.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2.23 | 2.69 | +20.5% | -0.426 to 1.34 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 985 | 985 | -0.1% | -4.79 to 3.53 | EVEN, no difference beyond the noise |
| queries a second | 985 | 985 | -0.1% | -4.79 to 3.53 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.06 | 2 | -3.0% | -0.121 to -0.00206 | GAIN |
| latency, 99th percentile (ms) | 5.59 | 5.22 | -6.6% | -1.97 to 1.23 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.28 | 1.22 | -4.9% | -0.191 to 0.0634 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 519 | +1.5% | 2.85 to 12.1 | power given |
| pages holding data, mean (MB) | 453 | 447 | -1.4% | -15.4 to 3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,035 | 189,067 | +0.0% | -10,041 to 10,106 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.103 | -4.1% | -0.0303 to 0.0216 | EVEN, no difference beyond the noise |
| host CPU-seconds | 168 | 161 | -4.1% | -45.9 to 32.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 190 | 134 | -29.4% | -256 to 145 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 8.35 to 24.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
