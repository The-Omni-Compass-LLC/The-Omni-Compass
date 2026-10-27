# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 288 | -0.7% | -9.38 to 5.56 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 290 | -0.8% | -9.88 to 5.19 | EVEN, no difference beyond the noise |
| queries a second | 4,675 | 4,637 | -0.8% | -158 to 83 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.92 | 5.77 | -2.4% | -0.762 to 0.475 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.8 | 7.61 | -2.4% | -0.373 to 0.00533 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.56 | 3.6 | +0.9% | -0.242 to 0.304 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 491 | -4.0% | -22.3 to -18.7 | GAIN |
| pages holding data, mean (MB) | 442 | 435 | -1.7% | -15 to 0.208 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 168,383 | 171,480 | +1.8% | -2,032 to 8,224 | shown, not judged |
| host CPU busy (share of the run) | 0.213 | 0.219 | +2.6% | -0.0174 to 0.0286 | EVEN, no difference beyond the noise |
| host CPU-seconds | 79.3 | 81.6 | +3.0% | -6.5 to 11.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.65 | 2.74 | +3.7% | -0.165 to 0.359 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 5 to 5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 291 | -0.3% | -3.25 to 1.72 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 291 | -0.2% | -3.29 to 1.88 | EVEN, no difference beyond the noise |
| queries a second | 4,669 | 4,658 | -0.2% | -52.6 to 30.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.26 | 3.26 | +0.0% | -0.147 to 0.147 | EVEN, the same |
| latency, 99th percentile (ms) | 4.43 | 4.38 | -1.2% | -0.353 to 0.249 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.41 | 2.43 | +0.8% | -0.0139 to 0.0514 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 408 | -20.4% | -239 to 30.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 369 | -20.1% | -225 to 39.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 457,377 | 617,622 | +35.0% | -93,158 to 413,649 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.2 | +0.5% | -0.000245 to 0.00226 | EVEN, no difference beyond the noise |
| host CPU-seconds | 243 | 244 | +0.5% | -0.0719 to 2.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.69 | 2.71 | +0.8% | 0.0147 to 0.027 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 3.9 to 6.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 196 | +0.4% | -2.23 to 3.75 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.3% | -1.51 to 2.88 | EVEN, no difference beyond the noise |
| queries a second | 3,913 | 3,927 | +0.3% | -30.3 to 57.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.18 | 5.28 | +1.8% | -0.716 to 0.905 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.29 | 8.19 | -1.2% | -2.36 to 2.17 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.89 | 2.87 | -0.9% | -0.692 to 0.64 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 506 | -1.1% | -59.4 to 48 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 463 | +0.4% | -40.2 to 43.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 432,968 | 427,644 | -1.2% | -109,058 to 98,410 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.142 | +2.7% | -0.016 to 0.0235 | EVEN, no difference beyond the noise |
| host CPU-seconds | 165 | 169 | +2.7% | -19 to 27.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.77 | 2.83 | +2.3% | -0.351 to 0.478 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,935 | 2,940 | +0.2% | -4.98 to 14.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,943 | 2,947 | +0.1% | -1.75 to 10.4 | EVEN, no difference beyond the noise |
| queries a second | 2,943 | 2,947 | +0.1% | -1.75 to 10.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.283 | 0.277 | -2.4% | -0.0138 to 0.000505 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.365 | 0.354 | -2.9% | -0.0348 to 0.0135 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.217 | -3.1% | -0.112 to 0.0977 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 569 | +11.1% | -63.3 to 176 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 513 | +10.9% | -16.9 to 118 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 264,047 | 213,339 | -19.2% | -122,748 to 21,333 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.114 | -2.5% | -0.00588 to 7.43e-05 | EVEN, no difference beyond the noise |
| host CPU-seconds | 140 | 137 | -2.5% | -7.23 to 0.206 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.156 | 0.152 | -2.6% | -0.00872 to 0.000454 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 3.43 to 16.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 2.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 34.6 | 25.7 | -25.9% | -58 to 40 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 978 | 966 | -1.2% | -61.8 to 37.3 | EVEN, no difference beyond the noise |
| queries a second | 978 | 966 | -1.2% | -61.8 to 37.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 534 | 1,155 | +116.4% | -3,309 to 4,551 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,172 | 2,432 | +107.4% | -6,964 to 9,483 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 99.1 | 213 | +115.4% | -515 to 743 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 452 | 449 | -0.6% | -16.9 to 11 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 140,097 | 136,571 | -2.5% | -13,975 to 6,923 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.132 | -7.6% | -0.0269 to 0.00516 | EVEN, no difference beyond the noise |
| host CPU-seconds | 170 | 158 | -7.0% | -31.1 to 7.43 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 23.1 | 23.6 | +2.1% | -55.7 to 56.7 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
