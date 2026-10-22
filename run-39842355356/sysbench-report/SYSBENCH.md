# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.3% | -3.48 to 1.96 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.2% | -3.6 to 2.24 | EVEN, no difference beyond the noise |
| queries a second | 4,705 | 4,694 | -0.2% | -57.7 to 35.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.82 | 4.77 | -1.2% | -0.306 to 0.19 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.59 | 6.71 | +1.8% | -0.183 to 0.424 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.18 | 3.17 | -0.0% | -0.0559 to 0.0542 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 505 | -1.4% | -45.7 to 31.2 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 439 | -1.8% | -124 to 108 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,409 | 244,801 | +0.2% | -35,875 to 36,659 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.18 | +0.8% | -0.0116 to 0.0144 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98.2 | 99.1 | +0.9% | -6.68 to 8.39 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.19 | 2.21 | +1.1% | -0.126 to 0.176 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.6% | 0.426 to 3.02 | GAIN |
| throughput (transactions a second) | 294 | 296 | +0.6% | 0.42 to 3.16 | GAIN |
| queries a second | 4,703 | 4,731 | +0.6% | 6.72 to 50.6 | GAIN |
| latency, 95th percentile (ms) | 4.13 | 4.1 | -0.6% | -0.133 to 0.0826 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.57 | 5.54 | -0.6% | -0.321 to 0.254 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.19 | 3.19 | +0.1% | -0.0382 to 0.0449 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 498 | -2.8% | -73.8 to 45.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 444 | -3.8% | -79.9 to 44.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 651,496 | 679,661 | +4.3% | -132,176 to 188,507 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.192 | +1.5% | -0.00168 to 0.00733 | EVEN, no difference beyond the noise |
| host CPU-seconds | 314 | 319 | +1.6% | -3.22 to 13 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.36 | +1.0% | -0.0477 to 0.0924 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 8.41 to 20.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 192 | +0.0% | -2.39 to 2.55 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.0% | -0.493 to 0.563 | EVEN, no difference beyond the noise |
| queries a second | 3,928 | 3,929 | +0.0% | -9.85 to 11.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.84 | 8.79 | -0.6% | -0.508 to 0.407 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.1 | 13 | -0.5% | -1.77 to 1.63 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.37 | 5.36 | -0.1% | -0.218 to 0.204 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 541 | +5.7% | -43.2 to 102 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 481 | +4.0% | -45.4 to 82.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,715 | 573,488 | -6.7% | -229,995 to 147,540 | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.21 | -0.5% | -0.0135 to 0.0112 | EVEN, no difference beyond the noise |
| host CPU-seconds | 340 | 338 | -0.5% | -21.1 to 17.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.87 | 3.85 | -0.5% | -0.283 to 0.242 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 |  | 6.63 to 26.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,938 | 2,939 | +0.0% | -8.4 to 10.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,953 | +0.0% | -10.7 to 11.4 | EVEN, no difference beyond the noise |
| queries a second | 2,953 | 2,953 | +0.0% | -10.7 to 11.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.355 | 0.353 | -0.6% | -0.0272 to 0.0232 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.546 | 0.54 | -1.2% | -0.0687 to 0.056 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.22 | +2.1% | -0.00516 to 0.0142 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -19.5 to 15 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 457 | -1.4% | -17.4 to 4.07 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,692 | 361,519 | -1.4% | -34,716 to 24,370 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.114 | +3.7% | -0.00419 to 0.0123 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 189 | +3.8% | -6.37 to 20.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.135 | 0.141 | +3.8% | -0.00488 to 0.0152 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13 |  | 6.43 to 19.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 32 | 35.7 | +11.5% | -15.1 to 22.5 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 983 | -0.1% | -4.55 to 2.93 | EVEN, no difference beyond the noise |
| queries a second | 984 | 983 | -0.1% | -4.55 to 2.93 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.56 | 1.5 | -4.1% | -0.524 to 0.395 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.71 | 2.57 | -4.9% | -0.976 to 0.709 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.968 | 0.947 | -2.2% | -0.165 to 0.122 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 501 | -2.2% | -65.5 to 43.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 433 | -4.5% | -76.9 to 36.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,926 | 196,995 | +3.7% | -15,427 to 29,564 | shown, not judged |
| host CPU busy (share of the run) | 0.225 | 0.219 | -2.7% | -0.0463 to 0.0343 | EVEN, no difference beyond the noise |
| host CPU-seconds | 394 | 384 | -2.6% | -81.2 to 60.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 28.7 | 23.8 | -17.2% | -30 to 20.1 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 9.16 to 23.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
