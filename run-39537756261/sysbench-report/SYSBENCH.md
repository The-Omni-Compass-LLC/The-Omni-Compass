# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.6% | -4.85 to 1.52 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.6% | -3.93 to 0.479 | EVEN, no difference beyond the noise |
| queries a second | 4,710 | 4,682 | -0.6% | -62.9 to 7.66 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.31 | 5.18 | -2.4% | -0.484 to 0.232 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.34 | 7.17 | -2.3% | -1.2 to 0.858 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.35 | 3.33 | -0.6% | -0.068 to 0.0255 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 496 | -3.1% | -46.1 to 14.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 416 | -7.0% | -114 to 50.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,031 | 251,269 | +3.0% | -14,194 to 28,669 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.195 | +0.4% | -0.00101 to 0.00253 | EVEN, no difference beyond the noise |
| host CPU-seconds | 107 | 108 | +0.6% | -0.42 to 1.75 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.38 | 2.41 | +1.2% | -0.000432 to 0.0569 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | 6.23 to 9.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.1% | -2.78 to 2.17 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.1% | -2.76 to 2.37 | EVEN, no difference beyond the noise |
| queries a second | 4,720 | 4,717 | -0.1% | -44.1 to 37.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.91 | 3.86 | -1.2% | -0.147 to 0.0538 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.64 | 5.54 | -1.8% | -0.355 to 0.152 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.98 | 2.96 | -0.7% | -0.0549 to 0.0135 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 492 | -3.9% | -135 to 95.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 444 | -3.8% | -103 to 68.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,564 | 678,965 | +3.7% | -249,765 to 298,567 | shown, not judged |
| host CPU busy (share of the run) | 0.235 | 0.234 | -0.7% | -0.00526 to 0.00206 | EVEN, no difference beyond the noise |
| host CPU-seconds | 419 | 416 | -0.7% | -8.88 to 3.07 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.11 | 3.09 | -0.6% | -0.0423 to 0.00562 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17 |  | 6.17 to 27.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 191 | +0.5% | -3.8 to 5.83 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.1% | -2.61 to 2.87 | EVEN, no difference beyond the noise |
| queries a second | 3,921 | 3,924 | +0.1% | -52.1 to 57.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.23 | 8.74 | -5.3% | -1.21 to 0.233 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.9 | 13.2 | -4.8% | -2.22 to 0.894 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.49 | 5.37 | -2.1% | -0.22 to -0.0118 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 569 | +11.1% | -54.9 to 169 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 505 | +9.2% | -40.9 to 126 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,181 | 510,519 | -17.1% | -289,498 to 78,174 | shown, not judged |
| host CPU busy (share of the run) | 0.217 | 0.211 | -2.8% | -0.0126 to 0.000389 | EVEN, no difference beyond the noise |
| host CPU-seconds | 349 | 339 | -2.8% | -19.6 to 0.149 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.01 | 3.87 | -3.3% | -0.252 to -0.0123 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 7.35 to 23.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,947 | 2,947 | -0.0% | -5.58 to 5.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,953 | +0.0% | -5.57 to 5.67 | EVEN, no difference beyond the noise |
| queries a second | 2,953 | 2,953 | +0.0% | -5.57 to 5.67 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.322 | 0.316 | -1.9% | -0.0209 to 0.00891 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.448 | -1.8% | -0.0279 to 0.0119 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.2 | +0.3% | -0.00469 to 0.0057 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 468 | -8.6% | -81.6 to -5.99 | GAIN |
| pages holding data, mean (MB) | 464 | 421 | -9.2% | -79.4 to -6.33 | GAIN |
| pages read from disk into the pool (misses) | 366,457 | 424,698 | +15.9% | 3,688 to 112,794 | shown, not judged |
| host CPU busy (share of the run) | 0.0977 | 0.0984 | +0.7% | -0.00461 to 0.006 | EVEN, no difference beyond the noise |
| host CPU-seconds | 162 | 163 | +0.8% | -7.65 to 10.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.12 | 0.121 | +0.8% | -0.00557 to 0.00753 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.7 |  | 4.68 to 20.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 8.36 | 9.62 | +15.2% | -8.34 to 10.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 982 | -0.1% | -2.31 to 1.15 | EVEN, no difference beyond the noise |
| queries a second | 983 | 982 | -0.1% | -2.31 to 1.15 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.78 | 1.77 | -0.7% | -0.136 to 0.112 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.25 | 3.3 | +1.8% | 0.0565 to 0.0615 | LOSS |
| latency, mean (ms) | 1.07 | 1.07 | -0.3% | -0.015 to 0.00883 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 509 | -0.5% | -19.1 to 13.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 438 | -3.4% | -17.9 to -13 | GAIN |
| pages read from disk into the pool (misses) | 189,897 | 194,918 | +2.6% | -11,524 to 21,566 | shown, not judged |
| host CPU busy (share of the run) | 0.236 | 0.229 | -2.8% | -0.0205 to 0.00711 | EVEN, no difference beyond the noise |
| host CPU-seconds | 414 | 402 | -2.9% | -35 to 11 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 120 | 91.7 | -23.5% | -137 to 80.7 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 10 to 20 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
