# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 288 | 289 | +0.3% | -2.55 to 4.39 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 292 | +0.0% | -1.62 to 1.75 | EVEN, no difference beyond the noise |
| queries a second | 4,674 | 4,675 | +0.0% | -25.9 to 28 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.43 | 4.38 | -1.2% | -0.46 to 0.358 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 93.7 | 10.9 | -88.4% | -387 to 221 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.69 | 2.89 | -38.2% | -6.93 to 3.35 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 474 | -7.4% | -230 to 154 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 442 | 424 | -4.0% | -212 to 177 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,372 | 252,893 | +3.9% | -78,384 to 97,425 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.176 | +0.5% | -0.00462 to 0.00643 | EVEN, no difference beyond the noise |
| host CPU-seconds | 106 | 107 | +0.5% | -3.05 to 4.17 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.39 | 2.4 | +0.2% | -0.101 to 0.109 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.33 |  | 2.54 to 10.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.5% | -5.25 to 2.29 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 294 | -0.5% | -4.96 to 2.22 | EVEN, no difference beyond the noise |
| queries a second | 4,728 | 4,706 | -0.5% | -79.4 to 35.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.41 | 4.2 | -4.7% | -0.315 to -0.0967 | GAIN |
| latency, 99th percentile (ms) | 5.88 | 5.67 | -3.5% | -0.461 to 0.0461 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.38 | 3.28 | -2.8% | -0.144 to -0.0432 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 484 | -5.4% | -178 to 122 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 436 | -5.6% | -177 to 126 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,351 | 705,979 | +7.7% | -344,807 to 446,063 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.201 | -3.7% | -0.0104 to -0.0048 | GAIN |
| host CPU-seconds | 346 | 333 | -3.5% | -16.7 to -7.8 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.56 | 2.48 | -3.0% | -0.121 to -0.0352 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 12.5 to 18.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 152 | 152 | -0.1% | -18.6 to 18.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.1% | -2.7 to 2.28 | EVEN, no difference beyond the noise |
| queries a second | 3,915 | 3,911 | -0.1% | -54 to 45.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 180 | 180 | +0.2% | -137 to 138 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 382 | 358 | -6.3% | -137 to 88.4 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 31.6 | 30 | -4.9% | -16.4 to 13.4 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 573 | +11.9% | -33.5 to 156 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 514 | +11.3% | -40.9 to 145 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,729 | 499,555 | -18.7% | -262,749 to 32,401 | shown, not judged |
| host CPU busy (share of the run) | 0.268 | 0.26 | -3.1% | -0.0365 to 0.0196 | EVEN, no difference beyond the noise |
| host CPU-seconds | 440 | 426 | -3.1% | -63.7 to 36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 6.34 | 6.13 | -3.3% | -1.63 to 1.21 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 4.35 to 20.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,963 | 2,963 | -0.0% | -8.91 to 7.91 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,966 | 2,965 | -0.0% | -5.26 to 3.32 | EVEN, no difference beyond the noise |
| queries a second | 2,966 | 2,965 | -0.0% | -5.26 to 3.32 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.2 | 0.198 | -1.2% | -0.0075 to 0.00284 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.344 | 0.338 | -1.7% | -0.006 to -0.006 | GAIN |
| latency, mean (ms) | 0.138 | 0.138 | -0.2% | -0.00741 to 0.00686 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 451 | -12.0% | -99.3 to -23.4 | GAIN |
| pages holding data, mean (MB) | 463 | 413 | -10.9% | -93.1 to -8.24 | GAIN |
| pages read from disk into the pool (misses) | 367,136 | 432,512 | +17.8% | -22,411 to 153,165 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.108 | +0.5% | -0.000376 to 0.00142 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 193 | +0.5% | -0.784 to 2.74 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.142 | 0.143 | +0.5% | -0.000956 to 0.00245 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.33 |  | 4.16 to 14.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 21.2 | 21.6 | +1.9% | -5.84 to 6.65 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 986 | 983 | -0.4% | -6.33 to -0.599 | LOSS |
| queries a second | 986 | 983 | -0.4% | -6.33 to -0.599 | LOSS |
| latency, 95th percentile (ms) | 1.41 | 1.4 | -0.7% | -0.16 to 0.14 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2 | 2.02 | +1.2% | -0.48 to 0.527 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.95 | 0.939 | -1.2% | -0.0487 to 0.0264 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 476 | -7.1% | -114 to 42 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 408 | -10.0% | -114 to 23.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,240 | 214,359 | +13.3% | -38,722 to 88,961 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.111 | -1.9% | -0.0257 to 0.0214 | EVEN, no difference beyond the noise |
| host CPU-seconds | 174 | 171 | -1.7% | -38.7 to 32.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 18.5 | 18.5 | -0.1% | -2.92 to 2.89 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18 |  | 8.06 to 27.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
