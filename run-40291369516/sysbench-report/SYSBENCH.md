# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.6% | -3.01 to 6.82 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 296 | +0.7% | -2.85 to 6.89 | EVEN, no difference beyond the noise |
| queries a second | 4,699 | 4,732 | +0.7% | -45.7 to 110 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.08 | 2.97 | -3.5% | -0.247 to 0.0289 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.6 | 4.62 | +0.6% | -0.211 to 0.267 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.42 | 1.43 | +0.9% | -0.063 to 0.0896 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 501 | -2.1% | -25.3 to 3.52 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 439 | -1.8% | -15.1 to -1.33 | GAIN |
| pages read from disk into the pool (misses) | 244,500 | 232,826 | -4.8% | -20,353 to -2,996 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.107 | +1.7% | -0.00319 to 0.00672 | EVEN, no difference beyond the noise |
| host CPU-seconds | 63 | 64.1 | +1.7% | -1.81 to 3.95 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.41 | 1.42 | +1.0% | -0.0653 to 0.0936 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.2% | -4.56 to 3.54 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.2% | -4.58 to 3.52 | EVEN, no difference beyond the noise |
| queries a second | 4,727 | 4,718 | -0.2% | -73.2 to 56.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.2 | 4.15 | -1.2% | -0.158 to 0.0576 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.09 | 5.95 | -2.4% | -0.298 to 0.00881 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.18 | 3.17 | -0.3% | -0.0272 to 0.00542 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 568 | +11.0% | 3.09 to 110 | power given |
| pages holding data, mean (MB) | 462 | 518 | +12.3% | 19 to 94.4 | power given |
| pages read from disk into the pool (misses) | 657,161 | 482,971 | -26.5% | -248,602 to -99,778 | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.188 | -0.4% | -0.00245 to 0.000848 | EVEN, no difference beyond the noise |
| host CPU-seconds | 312 | 311 | -0.4% | -3.46 to 0.904 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.31 | 2.31 | -0.2% | -0.0232 to 0.0124 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 11.8 to 17.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 69.9 | 62.8 | -10.1% | -29.3 to 15.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 195 | -1.1% | -12.3 to 8.08 | EVEN, no difference beyond the noise |
| queries a second | 3,942 | 3,899 | -1.1% | -246 to 162 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 600 | 1,540 | +156.5% | -2,837 to 4,716 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,454 | 2,591 | +78.2% | -3,533 to 5,808 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 139 | 255 | +82.5% | -306 to 536 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 462 | 459 | -0.6% | -16.2 to 10.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,729 | 601,097 | -2.2% | -65,286 to 38,022 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.193 | -0.9% | -0.0134 to 0.0101 | EVEN, no difference beyond the noise |
| host CPU-seconds | 349 | 346 | -0.6% | -21.3 to 16.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 11.2 | 12.4 | +10.9% | -2.73 to 5.16 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,962 | 2,959 | -0.1% | -10.3 to 3.67 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,964 | 2,964 | -0.0% | -5.51 to 5.25 | EVEN, no difference beyond the noise |
| queries a second | 2,964 | 2,964 | -0.0% | -5.51 to 5.25 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.198 | 0.198 | -0.2% | -0.00906 to 0.00839 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.344 | 0.342 | -0.6% | -0.0106 to 0.00661 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.136 | 0.227 | +67.0% | -0.252 to 0.434 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 534 | +4.3% | -319 to 362 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 476 | +2.6% | -259 to 283 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,509 | 351,449 | -4.4% | -389,561 to 357,441 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.108 | +0.4% | -0.00212 to 0.00298 | EVEN, no difference beyond the noise |
| host CPU-seconds | 193 | 193 | +0.4% | -3.84 to 5.43 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.143 | +0.5% | -0.00241 to 0.00389 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 |  | -7.64 to 30.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 73.5 | 76.6 | +4.2% | -11.4 to 17.5 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 987 | -0.1% | -4.33 to 2.74 | EVEN, no difference beyond the noise |
| queries a second | 988 | 987 | -0.1% | -4.33 to 2.74 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 153 | 134 | -12.6% | -72.4 to 34 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 420 | 295 | -29.8% | -324 to 74 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 29.4 | 23.6 | -19.7% | -17.1 to 5.5 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 455 | 451 | -0.9% | -15.1 to 6.67 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 190,085 | 188,631 | -0.8% | -9,848 to 6,940 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.136 | -3.4% | -0.0292 to 0.0197 | EVEN, no difference beyond the noise |
| host CPU-seconds | 249 | 241 | -3.4% | -50 to 33.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 7.6 | 7.15 | -5.9% | -0.855 to -0.0392 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
