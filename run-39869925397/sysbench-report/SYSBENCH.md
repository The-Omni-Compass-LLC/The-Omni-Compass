# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 292 | +0.6% | -2.77 to 6.41 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 290 | 292 | +0.5% | -0.758 to 3.8 | EVEN, no difference beyond the noise |
| queries a second | 4,645 | 4,669 | +0.5% | -12.1 to 60.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.91 | 3.73 | -4.8% | -0.568 to 0.194 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.14 | 5.85 | -4.8% | -1.26 to 0.675 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.29 | 2.15 | -6.0% | -0.956 to 0.681 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 460 | -10.1% | -126 to 22.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 446 | 405 | -9.2% | -104 to 22.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 247,365 | 254,599 | +2.9% | -27,964 to 42,432 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.16 | +0.7% | -0.00999 to 0.0123 | EVEN, no difference beyond the noise |
| host CPU-seconds | 97.6 | 98.3 | +0.6% | -6.07 to 7.29 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.18 | 2.18 | +0.0% | -0.145 to 0.146 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.1% | -2.49 to 2.82 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.1% | -2.69 to 3.16 | EVEN, no difference beyond the noise |
| queries a second | 4,698 | 4,702 | +0.1% | -43 to 50.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.86 | 2.74 | -4.1% | -0.38 to 0.144 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.57 | 4.38 | -4.1% | -0.414 to 0.0393 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.08 | 2.04 | -1.9% | -0.236 to 0.158 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 580 | +13.2% | -125 to 261 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 503 | +8.9% | -73.2 to 155 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 651,470 | 544,234 | -16.5% | -443,498 to 229,027 | shown, not judged |
| host CPU busy (share of the run) | 0.392 | 0.39 | -0.4% | -0.017 to 0.014 | EVEN, no difference beyond the noise |
| host CPU-seconds | 700 | 697 | -0.4% | -31.2 to 26 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.19 | 5.16 | -0.4% | -0.283 to 0.237 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 11.5 to 19.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 136 | 149 | +9.3% | -22.8 to 48.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | -0.1% | -2.26 to 1.95 | EVEN, no difference beyond the noise |
| queries a second | 3,953 | 3,950 | -0.1% | -45.1 to 39 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 169 | 126 | -25.8% | -169 to 81.7 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 411 | 279 | -32.2% | -631 to 366 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 34.4 | 23.5 | -31.6% | -44.5 to 22.8 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 572 | +11.8% | -90.8 to 211 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 504 | +9.3% | -80.9 to 167 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 617,735 | 528,326 | -14.5% | -371,555 to 192,737 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.18 | -1.2% | -0.0134 to 0.00895 | EVEN, no difference beyond the noise |
| host CPU-seconds | 324 | 319 | -1.3% | -23.6 to 15.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.26 | 4.7 | -10.7% | -2.21 to 1.08 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 11.2 to 21.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,946 | 2,945 | -0.0% | -4.18 to 2.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,950 | -0.1% | -8.45 to 3.48 | EVEN, no difference beyond the noise |
| queries a second | 2,953 | 2,950 | -0.1% | -8.45 to 3.48 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.361 | 0.334 | -7.4% | -0.0751 to 0.0218 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.476 | 0.448 | -5.7% | -0.074 to 0.0193 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.213 | 0.205 | -4.0% | -0.0325 to 0.0154 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 513 | +0.2% | -48 to 50.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 456 | -1.6% | -34.7 to 20.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,773 | 374,530 | +2.1% | -60,142 to 75,656 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.104 | -8.1% | -0.0319 to 0.0135 | EVEN, no difference beyond the noise |
| host CPU-seconds | 188 | 173 | -8.2% | -53.7 to 22.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.14 | 0.128 | -8.2% | -0.0396 to 0.0168 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | 4.43 to 17.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 37.2 | 51.7 | +38.9% | -25.8 to 54.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 986 | 985 | -0.1% | -4.83 to 3.35 | EVEN, no difference beyond the noise |
| queries a second | 986 | 985 | -0.1% | -4.83 to 3.35 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 135 | 117 | -13.4% | -178 to 142 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 374 | 285 | -23.7% | -483 to 305 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 24.6 | 19.5 | -20.9% | -35.8 to 25.5 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 494 | -3.5% | -79.5 to 43.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 428 | -5.6% | -102 to 50.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,829 | 202,349 | +6.6% | -29,316 to 54,356 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.149 | -3.3% | -0.0128 to 0.00271 | EVEN, no difference beyond the noise |
| host CPU-seconds | 271 | 263 | -3.3% | -23.2 to 5.38 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 16.8 | 11.4 | -32.3% | -18.8 to 7.92 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 5.94 to 23.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
