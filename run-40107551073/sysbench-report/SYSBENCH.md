# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.2% | -0.782 to 1.75 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.2% | -0.883 to 1.87 | EVEN, no difference beyond the noise |
| queries a second | 4,713 | 4,721 | +0.2% | -14.1 to 29.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.18 | 4.13 | -1.2% | -0.267 to 0.166 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.64 | 5.64 | +0.0% | -0.251 to 0.251 | EVEN, the same |
| latency, mean (ms) | 2.75 | 2.75 | -0.1% | -0.0234 to 0.0205 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 488 | -4.6% | -55 to 7.56 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 412 | -8.3% | -93.8 to 19.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,981 | 246,245 | +0.1% | -39,077 to 39,606 | shown, not judged |
| host CPU busy (share of the run) | 0.215 | 0.216 | +0.7% | -0.0036 to 0.00655 | EVEN, no difference beyond the noise |
| host CPU-seconds | 128 | 129 | +0.7% | -2.33 to 4.12 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.85 | 2.86 | +0.5% | -0.0642 to 0.0941 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | -0.573 to 12.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.2% | -3.49 to 2.05 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.2% | -3.6 to 2.38 | EVEN, no difference beyond the noise |
| queries a second | 4,725 | 4,715 | -0.2% | -57.7 to 38.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.36 | 4.33 | -0.6% | -0.141 to 0.0881 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.78 | +0.0% | -0.263 to 0.264 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.33 | 3.32 | -0.4% | -0.105 to 0.0751 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 582 | +13.7% | -32.7 to 173 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 505 | +9.4% | -53.3 to 140 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,480 | 521,402 | -20.5% | -327,162 to 59,006 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.202 | -0.8% | -0.0111 to 0.00786 | EVEN, no difference beyond the noise |
| host CPU-seconds | 338 | 336 | -0.7% | -19 to 14 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.51 | 2.49 | -0.5% | -0.151 to 0.126 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 11.7 to 20.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 194 | -0.7% | -7.35 to 4.76 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.1% | -3.33 to 3.88 | EVEN, no difference beyond the noise |
| queries a second | 3,948 | 3,954 | +0.1% | -66.6 to 77.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.06 | 5.83 | +15.1% | -1.36 to 2.9 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.8 | 16.9 | +57.0% | -7.56 to 19.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.93 | 3.24 | +10.7% | -0.791 to 1.42 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 523 | +2.2% | -73.7 to 95.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 472 | +2.3% | -52.8 to 73.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,045 | 604,457 | -1.9% | -209,932 to 186,757 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.127 | +2.4% | -0.00182 to 0.00781 | EVEN, no difference beyond the noise |
| host CPU-seconds | 220 | 225 | +2.5% | -2.78 to 13.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.47 | 2.55 | +3.1% | -0.0694 to 0.224 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14 |  | 5.04 to 23 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,946 | 2,946 | +0.0% | -6.93 to 7.19 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,953 | +0.0% | -6.44 to 6.73 | EVEN, no difference beyond the noise |
| queries a second | 2,953 | 2,953 | +0.0% | -6.44 to 6.73 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.33 | 0.324 | -1.8% | -0.0209 to 0.00891 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.459 | 0.448 | -2.3% | -0.0221 to 0.000808 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.205 | +0.2% | -0.00222 to 0.00297 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 494 | -3.4% | -379 to 344 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 440 | -5.1% | -335 to 288 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,889 | 396,203 | +8.0% | -363,302 to 421,930 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.103 | +0.9% | -0.000741 to 0.0025 | EVEN, no difference beyond the noise |
| host CPU-seconds | 169 | 171 | +1.0% | -1.1 to 4.41 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.126 | 0.127 | +1.0% | -0.000921 to 0.00333 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 |  | 1.29 to 21.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 333 | 256 | -22.9% | -231 to 78.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 987 | 988 | +0.0% | -0.984 to 1.89 | EVEN, no difference beyond the noise |
| queries a second | 987 | 988 | +0.0% | -0.984 to 1.89 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.37 | 2.51 | +6.1% | -1.18 to 1.47 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.97 | 5.72 | +15.0% | -1.9 to 3.4 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.877 | 0.997 | +13.7% | -0.166 to 0.407 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 461 | -9.9% | -195 to 93.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 403 | -11.0% | -179 to 79.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,780 | 217,277 | +15.1% | -33,179 to 90,175 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.121 | +7.0% | -0.0163 to 0.032 | EVEN, no difference beyond the noise |
| host CPU-seconds | 199 | 212 | +6.9% | -28.2 to 55.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.46 | 2.14 | +46.7% | -1.27 to 2.63 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.7 |  | 6.41 to 18.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
