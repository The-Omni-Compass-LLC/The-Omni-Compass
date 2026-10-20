# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.5% | -4.43 to 1.78 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 293 | -0.4% | -4.58 to 2 | EVEN, no difference beyond the noise |
| queries a second | 4,714 | 4,694 | -0.4% | -73.3 to 32 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.31 | 5.25 | -1.2% | -0.331 to 0.206 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.66 | 7.61 | -0.6% | -0.242 to 0.151 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.28 | 3.26 | -0.5% | -0.186 to 0.15 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 496 | -3.1% | -31.3 to -0.849 | GAIN |
| pages holding data, mean (MB) | 447 | 388 | -13.2% | -65.3 to -52.9 | GAIN |
| pages read from disk into the pool (misses) | 247,337 | 260,420 | +5.3% | 11,648 to 14,519 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.25 | -0.4% | -0.0129 to 0.0109 | EVEN, no difference beyond the noise |
| host CPU-seconds | 149 | 149 | -0.4% | -7.81 to 6.61 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.33 | 3.33 | +0.1% | -0.163 to 0.168 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 1.03 to 11 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.1% | -3.74 to 3.29 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.0% | -3.62 to 3.32 | EVEN, no difference beyond the noise |
| queries a second | 4,724 | 4,721 | -0.0% | -57.9 to 53.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4 | 3.96 | -1.2% | -0.151 to 0.0553 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.34 | 5.31 | -0.6% | -0.393 to 0.33 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.14 | 3.13 | -0.2% | -0.0245 to 0.00912 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 585 | +14.2% | -54.4 to 200 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 518 | +12.0% | -41 to 152 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,998 | 497,383 | -24.1% | -424,590 to 109,359 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.187 | +0.1% | -0.00306 to 0.00357 | EVEN, no difference beyond the noise |
| host CPU-seconds | 308 | 309 | +0.2% | -4.57 to 5.93 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.28 | 2.29 | +0.3% | -0.00598 to 0.0195 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 |  | 4.11 to 33.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 193 | +0.9% | -3.82 to 7.11 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 197 | +0.7% | -0.251 to 2.95 | EVEN, no difference beyond the noise |
| queries a second | 3,917 | 3,944 | +0.7% | -5.02 to 58.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.74 | 8.53 | -2.4% | -1.57 to 1.15 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.3 | 13.8 | +3.8% | -6.09 to 7.1 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.27 | 5.32 | +1.1% | -1.11 to 1.23 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 597 | +16.7% | 28.1 to 143 | power given |
| pages holding data, mean (MB) | 461 | 525 | +13.7% | 44.8 to 81.6 | power given |
| pages read from disk into the pool (misses) | 615,885 | 475,938 | -22.7% | -179,520 to -100,375 | shown, not judged |
| host CPU busy (share of the run) | 0.272 | 0.27 | -1.0% | -0.00884 to 0.00325 | EVEN, no difference beyond the noise |
| host CPU-seconds | 479 | 474 | -1.0% | -15.2 to 5.18 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.48 | 5.38 | -1.9% | -0.178 to -0.0295 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 9.16 to 23.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,948 | 2,948 | +0.0% | -7.57 to 7.85 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,953 | +0.0% | -7.56 to 9.18 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,953 | +0.0% | -7.56 to 9.18 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.33 | 0.32 | -3.0% | -0.0186 to -0.00139 | GAIN |
| latency, 99th percentile (ms) | 0.443 | 0.432 | -2.4% | -0.0221 to 0.000808 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.198 | 0.2 | +1.4% | -0.00844 to 0.0138 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 597 | +16.6% | -52.7 to 223 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 530 | +14.4% | -7.78 to 141 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,136 | 273,576 | -25.7% | -200,638 to 11,517 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.159 | -1.2% | -0.00722 to 0.00331 | EVEN, no difference beyond the noise |
| host CPU-seconds | 283 | 280 | -1.2% | -12.7 to 5.74 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.21 | 0.208 | -1.2% | -0.00979 to 0.00473 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 5.5 to 15.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 17.3 | 16.5 | -4.7% | -10.4 to 8.83 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 982 | 980 | -0.2% | -7.96 to 4.59 | EVEN, no difference beyond the noise |
| queries a second | 982 | 980 | -0.2% | -7.96 to 4.59 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.01 | 1.93 | -4.3% | -1.05 to 0.877 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.37 | 4.65 | -13.4% | -4.88 to 3.45 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.41 | 1.32 | -6.5% | -0.428 to 0.244 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 444 | -13.3% | -226 to 89.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 452 | 384 | -15.2% | -204 to 66 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 190,115 | 246,505 | +29.7% | -73,421 to 186,199 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.144 | -0.4% | -0.0252 to 0.0239 | EVEN, no difference beyond the noise |
| host CPU-seconds | 259 | 258 | -0.4% | -44.5 to 42.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 34.6 | 34.3 | -1.0% | -29.3 to 28.7 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 7.49 to 21.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
