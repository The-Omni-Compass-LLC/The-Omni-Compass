# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 291 | -1.1% | -17.1 to 10.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.2% | -5.88 to 4.49 | EVEN, no difference beyond the noise |
| queries a second | 4,745 | 4,733 | -0.2% | -94.1 to 71.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.54 | 3.67 | +3.6% | -1.19 to 1.44 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.14 | 41.9 | +414.2% | -73.4 to 141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.31 | 3.22 | +38.9% | -1.41 to 3.21 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,199 | +134.2% | 634 to 740 | power given |
| pages holding data, mean (MB) | 458 | 973 | +112.2% | 493 to 536 | power given |
| pages read from disk into the pool (misses) | 248,951 | 83,074 | -66.6% | -175,629 to -156,126 | shown, not judged |
| host CPU busy (share of the run) | 0.162 | 0.16 | -1.5% | -0.0038 to -0.00119 | GAIN |
| host CPU-seconds | 97.1 | 95.6 | -1.5% | -2.41 to -0.574 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.17 | 2.16 | -0.4% | -0.128 to 0.108 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.3% | -2.21 to 0.564 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.2% | -1.92 to 0.624 | EVEN, no difference beyond the noise |
| queries a second | 4,722 | 4,712 | -0.2% | -30.7 to 9.99 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.15 | 4.23 | +1.8% | -0.112 to 0.263 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.13 | 6.28 | +2.4% | -0.273 to 0.567 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.11 | 3.07 | -1.1% | -0.128 to 0.057 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 930 | +81.6% | 144 to 692 | power given |
| pages holding data, mean (MB) | 464 | 823 | +77.1% | 126 to 591 | power given |
| pages read from disk into the pool (misses) | 657,382 | 167,519 | -74.5% | -644,140 to -335,586 | shown, not judged |
| host CPU busy (share of the run) | 0.243 | 0.24 | -1.2% | -0.00995 to 0.00401 | EVEN, no difference beyond the noise |
| host CPU-seconds | 432 | 427 | -1.2% | -17.8 to 7.24 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.21 | 3.18 | -1.0% | -0.115 to 0.054 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 196 | +0.4% | -3.1 to 4.63 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.0% | -4.02 to 4.08 | EVEN, no difference beyond the noise |
| queries a second | 3,919 | 3,919 | +0.0% | -80.5 to 81.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.83 | 5.54 | -18.9% | -1.56 to -1.02 | GAIN |
| latency, 99th percentile (ms) | 9.79 | 7.3 | -25.5% | -2.66 to -2.33 | GAIN |
| latency, mean (ms) | 4.36 | 4.09 | -6.1% | -0.386 to -0.144 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,076 | +110.3% | 376 to 753 | power given |
| pages holding data, mean (MB) | 463 | 931 | +101.0% | 302 to 634 | power given |
| pages read from disk into the pool (misses) | 622,118 | 134,276 | -78.4% | -520,654 to -455,029 | shown, not judged |
| host CPU busy (share of the run) | 0.244 | 0.227 | -7.0% | -0.0208 to -0.0134 | GAIN |
| host CPU-seconds | 444 | 412 | -7.0% | -38.7 to -23.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.95 | 4.59 | -7.4% | -0.484 to -0.247 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | 0.538 to 8.13 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,948 | 2,947 | -0.1% | -13.7 to 10.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,951 | 2,951 | -0.0% | -11.1 to 9.88 | EVEN, no difference beyond the noise |
| queries a second | 2,951 | 2,951 | -0.0% | -11.1 to 9.88 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.303 | 0.304 | +0.2% | -0.0493 to 0.0506 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.409 | 0.427 | +4.4% | -0.0309 to 0.0669 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.183 | 0.189 | +2.8% | -0.00877 to 0.0192 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 706 | +37.9% | -333 to 721 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 628 | +35.4% | -255 to 584 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,554 | 256,486 | -30.0% | -393,404 to 173,269 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.154 | +2.6% | -0.0055 to 0.0133 | EVEN, no difference beyond the noise |
| host CPU-seconds | 265 | 272 | +2.6% | -9.61 to 23.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.197 | 0.202 | +2.6% | -0.00715 to 0.0175 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.667 |  | -0.768 to 2.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 145 | 141 | -2.9% | -49.7 to 41.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 987 | 988 | +0.1% | -4.79 to 7.13 | EVEN, no difference beyond the noise |
| queries a second | 987 | 988 | +0.1% | -4.79 to 7.13 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 147 | 187 | +27.2% | -170 to 250 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 341 | 424 | +24.4% | -406 to 573 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 26.6 | 34.6 | +29.8% | -41.6 to 57.5 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,238 | +141.9% | 705 to 748 | power given |
| pages holding data, mean (MB) | 457 | 893 | +95.5% | 409 to 464 | power given |
| pages read from disk into the pool (misses) | 191,677 | 71,827 | -62.5% | -130,253 to -109,446 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.128 | -4.4% | -0.0225 to 0.0107 | EVEN, no difference beyond the noise |
| host CPU-seconds | 237 | 227 | -4.2% | -38.1 to 18.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.72 | 3.56 | -4.3% | -1.56 to 1.24 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
