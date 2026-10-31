# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.5% | -5.98 to 8.64 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.4% | -6.44 to 8.77 | EVEN, no difference beyond the noise |
| queries a second | 4,714 | 4,733 | +0.4% | -103 to 140 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.06 | 3.04 | -0.6% | -0.303 to 0.269 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.68 | 4.68 | -0.0% | -0.37 to 0.366 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.6 | 1.51 | -5.6% | -0.647 to 0.469 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 447 | 447 | -0.0% | -2.59 to 2.29 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 246,793 | 246,814 | +0.0% | -5,958 to 6,000 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.114 | +3.4% | -0.00314 to 0.0106 | EVEN, no difference beyond the noise |
| host CPU-seconds | 66.5 | 68.7 | +3.3% | -1.82 to 6.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.48 | 1.53 | +2.9% | -0.0268 to 0.112 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 297 | +0.3% | -0.707 to 2.55 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.3% | -0.721 to 2.57 | EVEN, no difference beyond the noise |
| queries a second | 4,735 | 4,749 | +0.3% | -11.5 to 41.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.69 | 1.74 | +3.0% | 0.00543 to 0.0972 | LOSS |
| latency, 99th percentile (ms) | 2.98 | 3.15 | +5.5% | -0.0695 to 0.4 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.21 | +0.2% | -0.0667 to 0.0714 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 587 | +14.6% | -247 to 397 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 521 | +12.4% | -209 to 325 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,794 | 541,461 | -17.2% | -588,001 to 363,337 | shown, not judged |
| host CPU busy (share of the run) | 0.0971 | 0.0976 | +0.5% | -0.00722 to 0.00817 | EVEN, no difference beyond the noise |
| host CPU-seconds | 175 | 175 | +0.5% | -13.1 to 14.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.3 | 1.3 | +0.2% | -0.101 to 0.106 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.667 |  | -2.2 to 3.54 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 194 | +0.4% | -5.91 to 7.54 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.2% | -3.76 to 3.08 | EVEN, no difference beyond the noise |
| queries a second | 3,948 | 3,941 | -0.2% | -75.1 to 61.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.68 | 4.77 | -16.1% | -2.39 to 0.563 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 19.5 | 13.5 | -30.5% | -27.2 to 15.4 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.97 | 2.74 | -7.8% | -0.791 to 0.329 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,075 | +110.0% | 177 to 949 | power given |
| pages holding data, mean (MB) | 461 | 928 | +101.2% | 196 to 738 | power given |
| pages read from disk into the pool (misses) | 616,531 | 150,465 | -75.6% | -621,172 to -310,961 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.117 | -3.4% | -0.0104 to 0.00227 | EVEN, no difference beyond the noise |
| host CPU-seconds | 214 | 207 | -3.4% | -18.2 to 3.78 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.44 | 2.35 | -3.8% | -0.172 to -0.0136 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,946 | 2,950 | +0.1% | -3.29 to 11.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,950 | 2,954 | +0.1% | -4.34 to 12.8 | EVEN, no difference beyond the noise |
| queries a second | 2,950 | 2,954 | +0.1% | -4.34 to 12.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.314 | 0.313 | -0.5% | -0.00884 to 0.00551 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.432 | 0.435 | +0.6% | -0.00881 to 0.0141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.191 | -0.9% | -0.00588 to 0.00245 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 464 | 461 | -0.7% | -17.9 to 11.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,578 | 364,818 | -0.8% | -18,850 to 13,330 | shown, not judged |
| host CPU busy (share of the run) | 0.157 | 0.157 | -0.3% | -0.00342 to 0.0025 | EVEN, no difference beyond the noise |
| host CPU-seconds | 277 | 276 | -0.2% | -5.85 to 4.49 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.205 | 0.205 | -0.4% | -0.00432 to 0.0028 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 11.9 | 17.9 | +50.8% | -3.32 to 15.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 985 | +0.0% | -1.48 to 1.87 | EVEN, no difference beyond the noise |
| queries a second | 984 | 985 | +0.0% | -1.48 to 1.87 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.8 | 1.76 | -2.1% | -0.467 to 0.391 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.57 | 3.55 | -0.7% | -0.539 to 0.492 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 1.04 | -1.9% | -0.153 to 0.113 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.3% | 703 to 745 | power given |
| pages holding data, mean (MB) | 458 | 888 | +94.0% | 408 to 453 | power given |
| pages read from disk into the pool (misses) | 193,005 | 71,691 | -62.9% | -129,293 to -113,335 | shown, not judged |
| host CPU busy (share of the run) | 0.234 | 0.224 | -3.9% | -0.0348 to 0.0164 | EVEN, no difference beyond the noise |
| host CPU-seconds | 410 | 394 | -3.9% | -60.6 to 28.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 78.5 | 49.5 | -36.9% | -82.7 to 24.7 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
