# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.2% | -4.52 to 5.77 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.1% | -4.34 to 5.05 | EVEN, no difference beyond the noise |
| queries a second | 4,700 | 4,705 | +0.1% | -69.4 to 80.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.12 | 5 | -2.4% | -0.593 to 0.349 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.04 | 6.83 | -2.9% | -0.987 to 0.573 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.3 | 3.28 | -0.4% | -0.105 to 0.0761 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 500 | -2.3% | -99.2 to 76 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 417 | -6.6% | -140 to 80.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,765 | 245,551 | -0.1% | -81,933 to 81,505 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.194 | +2.1% | -0.00142 to 0.00954 | EVEN, no difference beyond the noise |
| host CPU-seconds | 104 | 107 | +2.4% | -0.56 to 5.61 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.38 | +2.2% | 0.0238 to 0.0801 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.2% | -1.06 to 2.41 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.2% | -0.965 to 2.42 | EVEN, no difference beyond the noise |
| queries a second | 4,715 | 4,727 | +0.2% | -15.4 to 38.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.1 | 4.08 | -0.6% | -0.129 to 0.0804 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.67 | -0.6% | -0.328 to 0.258 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.2 | 3.18 | -0.8% | -0.0427 to -0.00767 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 597 | +16.6% | -82.9 to 253 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 503 | +8.8% | -69 to 151 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,275 | 538,931 | -17.6% | -310,294 to 79,607 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.189 | -0.5% | -0.00443 to 0.00261 | EVEN, no difference beyond the noise |
| host CPU-seconds | 315 | 313 | -0.4% | -7.07 to 4.27 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.34 | 2.32 | -0.7% | -0.052 to 0.0207 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 |  | 8.32 to 29 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 189 | 189 | +0.4% | -3.05 to 4.68 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.2% | -2 to 1.07 | EVEN, no difference beyond the noise |
| queries a second | 3,931 | 3,922 | -0.2% | -40 to 21.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 10.2 | 9.5 | -6.4% | -1.67 to 0.368 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 15.2 | 15.9 | +4.4% | -9.08 to 10.4 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.78 | 5.79 | +0.3% | -0.819 to 0.856 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 672 | +31.3% | -98.7 to 419 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 566 | +22.7% | -25.3 to 234 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 617,087 | 410,181 | -33.5% | -469,269 to 55,458 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.214 | -3.1% | -0.0114 to -0.00216 | GAIN |
| host CPU-seconds | 355 | 344 | -3.0% | -17 to -4.51 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.1 | 3.96 | -3.4% | -0.153 to -0.129 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 |  | 5.83 to 30.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,959 | 2,958 | -0.0% | -7.09 to 4.91 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,965 | +0.0% | -1.79 to 2.45 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,965 | +0.0% | -1.79 to 2.45 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.197 | 0.2 | +1.9% | -0.0308 to 0.0381 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.338 | 0.336 | -0.6% | -0.0622 to 0.0582 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0941 | 0.0936 | -0.5% | -0.026 to 0.0252 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 534 | +4.3% | -81.9 to 126 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 486 | +4.9% | -76.1 to 122 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,601 | 331,555 | -9.8% | -157,801 to 85,709 | shown, not judged |
| host CPU busy (share of the run) | 0.0736 | 0.0691 | -6.1% | -0.0221 to 0.0132 | EVEN, no difference beyond the noise |
| host CPU-seconds | 132 | 124 | -6.1% | -39.6 to 23.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0979 | 0.092 | -6.0% | -0.0295 to 0.0177 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 0.0626 to 19.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 148 | 144 | -2.5% | -106 to 98.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 986 | 987 | +0.0% | -10 to 10.7 | EVEN, no difference beyond the noise |
| queries a second | 986 | 987 | +0.0% | -10 to 10.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 88.6 | 96.7 | +9.2% | -42.4 to 58.6 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 203 | 213 | +4.7% | -78.3 to 97.5 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 15.7 | 17.1 | +8.4% | -12.5 to 15.1 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 469 | -8.5% | -170 to 83.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 405 | -10.6% | -157 to 61.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,990 | 222,233 | +17.0% | -33,350 to 97,837 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.134 | -0.1% | -0.0278 to 0.0276 | EVEN, no difference beyond the noise |
| host CPU-seconds | 238 | 238 | +0.0% | -48.1 to 48.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.84 | 3.61 | -6.0% | -4.11 to 3.66 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 4.62 to 27.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
