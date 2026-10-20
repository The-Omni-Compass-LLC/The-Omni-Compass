# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 289 | 288 | -0.4% | -9.28 to 6.84 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 291 | 291 | -0.3% | -4.34 to 2.64 | EVEN, no difference beyond the noise |
| queries a second | 4,662 | 4,648 | -0.3% | -69.4 to 42.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.71 | 3.66 | -1.3% | -0.551 to 0.455 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 21.5 | 8.79 | -59.1% | -87 to 61.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.8 | 2.56 | -8.4% | -3.97 to 3.5 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 383 | -25.2% | -320 to 61.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 441 | 341 | -22.5% | -296 to 97.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,917 | 284,517 | +16.6% | -58,415 to 139,615 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.167 | +1.7% | -0.00918 to 0.0146 | EVEN, no difference beyond the noise |
| host CPU-seconds | 101 | 102 | +1.7% | -5.83 to 9.19 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.26 | 2.31 | +2.1% | -0.15 to 0.244 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 0.162 to 10.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.1% | -2.33 to 2.69 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.1% | -2.3 to 2.78 | EVEN, no difference beyond the noise |
| queries a second | 4,694 | 4,698 | +0.1% | -36.9 to 44.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.25 | 3.19 | -1.8% | -0.203 to 0.0873 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.54 | 4.51 | -0.6% | -0.145 to 0.0903 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.42 | 2.4 | -0.7% | -0.0662 to 0.0347 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 472 | -7.9% | -61.8 to -18.6 | GAIN |
| pages holding data, mean (MB) | 462 | 423 | -8.4% | -55.1 to -22.6 | GAIN |
| pages read from disk into the pool (misses) | 653,189 | 745,761 | +14.2% | 29,572 to 155,572 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.192 | -0.4% | -0.00334 to 0.00176 | EVEN, no difference beyond the noise |
| host CPU-seconds | 348 | 347 | -0.4% | -6.07 to 3.07 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.59 | 2.57 | -0.5% | -0.0511 to 0.0258 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 12.5 to 20.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 194 | -0.6% | -4.97 to 2.77 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.0% | -3.97 to 3.84 | EVEN, no difference beyond the noise |
| queries a second | 3,940 | 3,938 | -0.0% | -79.4 to 76.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.04 | 7.31 | +3.8% | -1.05 to 1.58 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.8 | 79.2 | +634.4% | -224 to 361 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.53 | 8.04 | +77.7% | -11.2 to 18.2 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 540 | +5.5% | -101 to 158 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 485 | +5.0% | -79 to 125 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 617,090 | 560,880 | -9.1% | -272,247 to 159,827 | shown, not judged |
| host CPU busy (share of the run) | 0.259 | 0.262 | +1.0% | 0.000314 to 0.00471 | power given |
| host CPU-seconds | 460 | 465 | +1.0% | -0.203 to 9.11 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.16 | 5.24 | +1.5% | -0.0731 to 0.232 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | -3.59 to 36.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,962 | +0.0% | -7.79 to 9.34 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,966 | +0.0% | -5.54 to 7.78 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,966 | +0.0% | -5.54 to 7.78 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.169 | 0.163 | -3.6% | -0.0711 to 0.0591 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.334 | 0.326 | -2.3% | -0.0542 to 0.0388 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0968 | 0.0981 | +1.4% | -0.0263 to 0.029 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 460 | -10.1% | -100 to -3.08 | GAIN |
| pages holding data, mean (MB) | 463 | 419 | -9.5% | -87.8 to -0.0139 | GAIN |
| pages read from disk into the pool (misses) | 367,548 | 428,544 | +16.6% | 12,108 to 109,884 | shown, not judged |
| host CPU busy (share of the run) | 0.0735 | 0.0741 | +0.8% | -0.022 to 0.0232 | EVEN, no difference beyond the noise |
| host CPU-seconds | 132 | 133 | +0.8% | -39.3 to 41.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0976 | 0.0984 | +0.8% | -0.0289 to 0.0304 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 7.46 to 13.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 22.1 | 22.5 | +2.1% | -4.08 to 5.02 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 986 | +0.2% | -0.651 to 5.16 | EVEN, no difference beyond the noise |
| queries a second | 983 | 986 | +0.2% | -0.651 to 5.16 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.71 | 1.67 | -2.7% | -0.38 to 0.288 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.55 | 3.51 | -1.3% | -0.382 to 0.292 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.03 | 1.02 | -0.6% | -0.0811 to 0.0693 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 497 | -2.9% | -50.5 to 20.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 428 | -5.3% | -59 to 10.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,975 | 202,325 | +6.5% | -25,138 to 49,838 | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.216 | -1.9% | -0.031 to 0.0226 | EVEN, no difference beyond the noise |
| host CPU-seconds | 387 | 380 | -1.9% | -54.1 to 39.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 39.8 | 37.3 | -6.5% | -18.8 to 13.6 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19.7 |  | 13.9 to 25.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
