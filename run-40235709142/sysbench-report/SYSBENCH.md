# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.3% | -5.41 to 7.46 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 296 | +0.4% | -5.23 to 7.47 | EVEN, no difference beyond the noise |
| queries a second | 4,712 | 4,730 | +0.4% | -83.6 to 120 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.77 | 2.73 | -1.3% | -0.356 to 0.284 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.36 | 4.33 | -0.6% | -0.133 to 0.0826 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.33 | 1.33 | -0.4% | -0.166 to 0.156 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 421 | -17.8% | -111 to -70.5 | GAIN |
| pages holding data, mean (MB) | 445 | 375 | -15.7% | -106 to -33.9 | GAIN |
| pages read from disk into the pool (misses) | 243,276 | 264,734 | +8.8% | 13,766 to 29,149 | shown, not judged |
| host CPU busy (share of the run) | 0.0992 | 0.0983 | -1.0% | -0.0122 to 0.0103 | EVEN, no difference beyond the noise |
| host CPU-seconds | 59.6 | 58.9 | -1.0% | -7.38 to 6.13 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.33 | 1.31 | -1.4% | -0.196 to 0.16 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | 4.23 to 7.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.2% | -1.99 to 0.777 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.1% | -2.12 to 1.79 | EVEN, no difference beyond the noise |
| queries a second | 4,741 | 4,738 | -0.1% | -34 to 28.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.81 | 2.73 | -2.9% | -0.27 to 0.105 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.05 | 9.72 | +60.7% | -12.2 to 19.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.4 | 2.49 | +3.9% | -0.627 to 0.817 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 457 | -10.7% | -147 to 37.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 426 | -7.7% | -145 to 73.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 652,102 | 779,000 | +19.5% | -153,781 to 407,577 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.163 | +0.1% | -0.0103 to 0.0106 | EVEN, no difference beyond the noise |
| host CPU-seconds | 291 | 292 | +0.1% | -18 to 18.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.17 | 2.18 | +0.3% | -0.136 to 0.15 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 4.74 to 19.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 191 | -0.3% | -2.88 to 1.63 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.2% | -1.42 to 0.546 | EVEN, no difference beyond the noise |
| queries a second | 3,928 | 3,920 | -0.2% | -28.5 to 10.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.79 | 8.69 | -1.2% | -0.566 to 0.352 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.8 | 13 | +1.2% | -0.723 to 1.03 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.46 | 5.44 | -0.4% | -0.131 to 0.0909 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -20.1 to 15.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 457 | -0.9% | -32.5 to 24.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 613,765 | 601,506 | -2.0% | -47,578 to 23,059 | shown, not judged |
| host CPU busy (share of the run) | 0.224 | 0.22 | -1.7% | -0.0174 to 0.00977 | EVEN, no difference beyond the noise |
| host CPU-seconds | 361 | 355 | -1.7% | -28.5 to 16.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.12 | 4.06 | -1.3% | -0.283 to 0.172 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 14.9 to 17.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,942 | 2,945 | +0.1% | -5.84 to 12.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,950 | 2,954 | +0.1% | -3.42 to 10.4 | EVEN, no difference beyond the noise |
| queries a second | 2,950 | 2,954 | +0.1% | -3.42 to 10.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.351 | 0.344 | -1.8% | -0.0399 to 0.0272 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.481 | 0.473 | -1.7% | -0.049 to 0.033 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.214 | 0.213 | -0.4% | -0.0199 to 0.0182 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 486 | -5.0% | -31.2 to -20.4 | GAIN |
| pages holding data, mean (MB) | 464 | 441 | -4.8% | -40.1 to -4.85 | GAIN |
| pages read from disk into the pool (misses) | 366,843 | 378,049 | +3.1% | 5,340 to 17,072 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.112 | +0.0% | -0.0153 to 0.0154 | EVEN, no difference beyond the noise |
| host CPU-seconds | 186 | 187 | +0.1% | -25.4 to 25.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.139 | 0.139 | +0.0% | -0.0193 to 0.0194 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 1.03 to 11 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 392 | 395 | +0.9% | -44.4 to 51.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 989 | 990 | +0.1% | -2.05 to 3.85 | EVEN, no difference beyond the noise |
| queries a second | 989 | 990 | +0.1% | -2.05 to 3.85 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.79 | 3.01 | +7.8% | -0.784 to 1.22 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 8.22 | +46.7% | -4.2 to 9.44 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.943 | 1.06 | +11.9% | -0.227 to 0.452 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 454 | 450 | -0.7% | -21.3 to 14.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,380 | 187,151 | -1.2% | -9,838 to 5,380 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.104 | -1.4% | -0.0127 to 0.0097 | EVEN, no difference beyond the noise |
| host CPU-seconds | 186 | 183 | -1.4% | -22.1 to 16.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.05 | 1.04 | -1.7% | -0.263 to 0.226 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
