# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 291 | +0.5% | -0.0916 to 2.75 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.2% | -2.6 to 3.79 | EVEN, no difference beyond the noise |
| queries a second | 4,682 | 4,691 | +0.2% | -41.6 to 60.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.68 | 5.47 | -3.6% | -0.885 to 0.475 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.28 | 7.89 | -4.8% | -1.18 to 0.396 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.4 | 3.33 | -2.1% | -0.377 to 0.231 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 522 | +2.0% | -52.9 to 72.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 446 | 424 | -5.0% | -86.1 to 41.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 241,863 | 241,499 | -0.2% | -42,845 to 42,118 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.188 | +1.6% | -0.00236 to 0.00817 | EVEN, no difference beyond the noise |
| host CPU-seconds | 102 | 104 | +1.7% | -1.25 to 4.63 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.3 | 2.33 | +1.2% | -0.0294 to 0.0851 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.33 |  | 4.9 to 7.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.1% | -2.45 to 1.87 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.0% | -2.58 to 2.29 | EVEN, no difference beyond the noise |
| queries a second | 4,717 | 4,715 | -0.0% | -41.3 to 36.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.24 | 4.18 | -1.3% | -1.17 to 1.06 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.55 | 5.61 | +1.2% | -1.32 to 1.46 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.22 | 3.19 | -0.9% | -0.443 to 0.387 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 567 | +10.8% | -120 to 231 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 491 | +6.3% | -127 to 186 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,899 | 556,781 | -14.9% | -502,734 to 308,498 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.192 | -1.3% | -0.037 to 0.0321 | EVEN, no difference beyond the noise |
| host CPU-seconds | 323 | 319 | -1.3% | -61.9 to 53.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.39 | 2.37 | -1.2% | -0.447 to 0.39 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 6.39 to 23.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 193 | +0.9% | -0.473 to 3.88 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 197 | +0.2% | -0.893 to 1.75 | EVEN, no difference beyond the noise |
| queries a second | 3,929 | 3,937 | +0.2% | -17.9 to 35 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.79 | 8.13 | -7.5% | -1.45 to 0.129 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.9 | 12.1 | -6.4% | -1.63 to -0.00812 | GAIN |
| latency, mean (ms) | 5.48 | 5.4 | -1.4% | -0.291 to 0.143 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 692 | +35.1% | 16.5 to 343 | power given |
| pages holding data, mean (MB) | 462 | 576 | +24.6% | 16 to 211 | power given |
| pages read from disk into the pool (misses) | 616,615 | 413,218 | -33.0% | -420,404 to 13,610 | shown, not judged |
| host CPU busy (share of the run) | 0.224 | 0.22 | -1.7% | -0.0155 to 0.00799 | EVEN, no difference beyond the noise |
| host CPU-seconds | 361 | 355 | -1.6% | -24.7 to 13 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.11 | 4.01 | -2.5% | -0.36 to 0.157 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 20.7 |  | 15.5 to 25.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,918 | 2,915 | -0.1% | -16.4 to 10.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,953 | +0.0% | -3.47 to 3.77 | EVEN, no difference beyond the noise |
| queries a second | 2,953 | 2,953 | +0.0% | -3.47 to 3.77 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.413 | 0.428 | +3.7% | -0.0506 to 0.0813 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.638 | 0.657 | +3.0% | 0.00436 to 0.0343 | LOSS |
| latency, mean (ms) | 0.228 | 0.235 | +3.3% | -0.00577 to 0.0209 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 524 | +2.4% | 5.53 to 19.4 | power given |
| pages holding data, mean (MB) | 464 | 461 | -0.6% | -25.5 to 20 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,968 | 365,381 | -0.4% | -34,484 to 31,310 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.121 | +4.5% | -0.00443 to 0.0148 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 201 | +4.6% | -7.22 to 24.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.144 | 0.15 | +4.7% | -0.00583 to 0.0192 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 6.06 to 25.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4.21 | 3.87 | -8.1% | -10.6 to 9.94 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 984 | -0.0% | -1.48 to 0.669 | EVEN, no difference beyond the noise |
| queries a second | 984 | 984 | -0.0% | -1.48 to 0.669 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.6 | 1.73 | +8.5% | -0.152 to 0.423 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.49 | 3.08 | +23.5% | -0.241 to 1.41 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.03 | 1.1 | +7.5% | -0.0175 to 0.171 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 553 | +7.9% | -31.8 to 113 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 461 | +1.6% | -106 to 121 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,900 | 187,171 | -0.9% | -44,081 to 40,622 | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.161 | +25.6% | -0.112 to 0.177 | EVEN, no difference beyond the noise |
| host CPU-seconds | 197 | 249 | +26.2% | -174 to 278 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 135 | 183 | +35.8% | -316 to 412 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 |  | 4.65 to 32 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
