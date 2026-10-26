# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 279 | 282 | +1.4% | -9.48 to 17 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.3% | -1.67 to 3.46 | EVEN, no difference beyond the noise |
| queries a second | 4,710 | 4,725 | +0.3% | -26.7 to 55.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 14.6 | 7.57 | -48.1% | -46.3 to 32.3 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 114 | 104 | -9.3% | -283 to 262 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.39 | 5.44 | -14.9% | -12.9 to 11 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 489 | -4.5% | -171 to 125 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 445 | 431 | -3.1% | -125 to 97 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,091 | 241,710 | -1.4% | -60,246 to 53,484 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.164 | +0.9% | -0.00435 to 0.00736 | EVEN, no difference beyond the noise |
| host CPU-seconds | 97.4 | 98.4 | +1.0% | -2.94 to 4.88 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.3 | 2.29 | -0.4% | -0.178 to 0.159 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 3.52 to 8.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | -0.1% | -1.32 to 0.73 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.1% | -0.688 to 0.198 | EVEN, no difference beyond the noise |
| queries a second | 4,745 | 4,741 | -0.1% | -11 to 3.17 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.04 | 1.97 | -3.8% | -0.574 to 0.42 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.82 | 3.66 | -4.0% | -0.652 to 0.347 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.32 | -1.7% | -0.176 to 0.131 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 484 | -5.6% | -244 to 187 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 438 | -5.2% | -229 to 181 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,264 | 698,919 | +6.7% | -500,698 to 588,009 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.104 | -2.5% | -0.0154 to 0.01 | EVEN, no difference beyond the noise |
| host CPU-seconds | 191 | 186 | -2.5% | -27.6 to 18 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.41 | 1.38 | -2.4% | -0.2 to 0.132 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.33 |  | -6.83 to 25.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 196 | +0.3% | -1.76 to 3.06 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.1% | -1.1 to 1.49 | EVEN, no difference beyond the noise |
| queries a second | 3,935 | 3,939 | +0.1% | -22.1 to 29.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.78 | 5.71 | -1.2% | -1.14 to 1 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.6 | 9.29 | -12.0% | -7.09 to 4.55 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.74 | 3.63 | -2.8% | -0.913 to 0.704 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 549 | +7.2% | -128 to 201 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 498 | +8.0% | -102 to 175 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,325 | 542,358 | -11.7% | -298,936 to 155,002 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.18 | +0.0% | -0.00323 to 0.00333 | EVEN, no difference beyond the noise |
| host CPU-seconds | 318 | 319 | +0.1% | -6.9 to 7.34 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.58 | 3.57 | -0.3% | -0.0767 to 0.0587 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | 3.04 to 21 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,924 | 2,924 | -0.0% | -13.5 to 13.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,939 | 2,940 | +0.0% | -8.29 to 9.99 | EVEN, no difference beyond the noise |
| queries a second | 2,939 | 2,940 | +0.0% | -8.29 to 9.99 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.32 | 0.312 | -2.5% | -0.0166 to 0.000606 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.473 | 0.467 | -1.2% | -0.0301 to 0.0187 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.185 | 0.185 | +0.2% | -0.007 to 0.0079 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 524 | +2.4% | 5.92 to 18.4 | power given |
| pages holding data, mean (MB) | 464 | 461 | -0.7% | -25.3 to 19.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,700 | 354,019 | -3.5% | -24,692 to -670 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.143 | -1.3% | -0.00545 to 0.00177 | EVEN, no difference beyond the noise |
| host CPU-seconds | 260 | 257 | -1.2% | -9.49 to 3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.194 | 0.191 | -1.2% | -0.00742 to 0.00263 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 9.6 to 21.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.32 | 6.23 | -1.4% | -2.74 to 2.56 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 983 | -0.1% | -7.03 to 5.24 | EVEN, no difference beyond the noise |
| queries a second | 984 | 983 | -0.1% | -7.03 to 5.24 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.84 | 1.87 | +1.6% | -0.268 to 0.326 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.73 | 3.84 | +3.0% | -0.0654 to 0.287 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.22 | 1.1 | -10.0% | -0.557 to 0.311 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 454 | 451 | -0.7% | -15 to 8.35 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 187,953 | 187,323 | -0.3% | -15,638 to 14,379 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.115 | -5.0% | -0.0394 to 0.0275 | EVEN, no difference beyond the noise |
| host CPU-seconds | 186 | 177 | -4.8% | -60.3 to 42.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 70.4 | 67.7 | -3.9% | -33 to 27.5 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
