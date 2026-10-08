# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 288 | 288 | +0.1% | -2.58 to 3.39 | no difference beyond the noise |
| throughput (transactions a second) | 291 | 291 | +0.2% | -2.37 to 3.28 | no difference beyond the noise |
| queries a second | 4,651 | 4,658 | +0.2% | -37.9 to 52.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 6.02 | 6.1 | +1.2% | -0.339 to 0.484 | no difference beyond the noise |
| latency, 99th percentile (ms) | 8.28 | 8.33 | +0.6% | -0.375 to 0.477 | no difference beyond the noise |
| latency, mean (ms) | 3.51 | 3.53 | +0.7% | -0.0748 to 0.121 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 149 | -70.8% | -364 to -362 | better |
| pages holding data, mean (MB) | 438 | 133 | -69.5% | -328 to -281 | better |
| pages read from disk into the pool (misses) | 166,472 | 338,779 | +103.5% | 158,898 to 185,716 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.207 | +2.0% | -0.000126 to 0.00829 | no difference beyond the noise |
| host CPU-seconds | 75.3 | 77.1 | +2.4% | -0.128 to 3.81 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.54 | 2.59 | +2.3% | -0.0277 to 0.147 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 291 | -0.2% | -5.38 to 4.01 | no difference beyond the noise |
| throughput (transactions a second) | 293 | 292 | -0.2% | -5.09 to 3.94 | no difference beyond the noise |
| queries a second | 4,681 | 4,672 | -0.2% | -81.4 to 63 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.36 | 4.49 | +3.0% | -0.0907 to 0.354 | no difference beyond the noise |
| latency, 99th percentile (ms) | 6.02 | 6.28 | +4.3% | -0.0529 to 0.567 | no difference beyond the noise |
| latency, mean (ms) | 3.25 | 3.31 | +1.7% | 0.0397 to 0.0729 | **WORSE** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 326 | -36.3% | -541 to 170 | no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 290 | -37.4% | -458 to 111 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 456,009 | 879,257 | +92.8% | 97,100 to 749,396 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.206 | +3.0% | 0.00325 to 0.00892 | **WORSE** |
| host CPU-seconds | 223 | 231 | +3.5% | 4.21 to 11.4 | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 2.48 | 2.57 | +3.7% | 0.0205 to 0.165 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 13.7 |  | 3.32 to 24 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 187 | 190 | +1.4% | -0.557 to 5.92 | no difference beyond the noise |
| throughput (transactions a second) | 195 | 194 | -0.6% | -3.41 to 1.17 | no difference beyond the noise |
| queries a second | 3,900 | 3,877 | -0.6% | -68.2 to 23.3 | no difference beyond the noise |
| latency, 95th percentile (ms) | 10 | 8.58 | -14.4% | -1.92 to -0.982 | better |
| latency, 99th percentile (ms) | 15.2 | 12.8 | -15.5% | -5.82 to 1.11 | no difference beyond the noise |
| latency, mean (ms) | 5.95 | 5.56 | -6.5% | -1.16 to 0.386 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 942 | +84.1% | 81 to 780 | **WORSE** |
| pages holding data, mean (MB) | 461 | 797 | +73.0% | 121 to 552 | **WORSE** |
| pages read from disk into the pool (misses) | 434,006 | 193,175 | -55.5% | -363,149 to -118,513 | shown, not judged |
| host CPU busy (share of the run) | 0.231 | 0.215 | -6.9% | -0.0319 to -0.000215 | better |
| host CPU-seconds | 250 | 233 | -7.0% | -33.9 to -0.926 | better |
| host CPU-seconds per 1,000 transactions inside the line | 4.34 | 3.98 | -8.3% | -0.58 to -0.136 | better |
| buffer pool size changes written (the knob's moves) | 0 | 26.3 |  | 24.9 to 27.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,912 | 2,913 | +0.0% | -9.91 to 11.9 | no difference beyond the noise |
| throughput (transactions a second) | 2,926 | 2,929 | +0.1% | -8.19 to 14.3 | no difference beyond the noise |
| queries a second | 2,926 | 2,929 | +0.1% | -8.19 to 14.3 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.404 | 0.407 | +0.6% | -0.0177 to 0.0224 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.53 | 0.536 | +1.1% | -0.00691 to 0.0189 | no difference beyond the noise |
| latency, mean (ms) | 0.227 | 0.237 | +4.1% | -0.00116 to 0.0199 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 641 | +25.2% | -98.6 to 357 | no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 565 | +22.1% | -29.7 to 234 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 262,667 | 206,442 | -21.4% | -274,790 to 162,339 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.126 | +0.3% | -0.00841 to 0.00925 | no difference beyond the noise |
| host CPU-seconds | 140 | 141 | +0.4% | -8.91 to 10 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.157 | 0.157 | +0.4% | -0.0102 to 0.0114 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.7 |  | 11.9 to 19.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 42.8 | 42.7 | -0.1% | -32 to 31.9 | no difference beyond the noise |
| throughput (transactions a second) | 973 | 975 | +0.2% | -16.4 to 21.1 | no difference beyond the noise |
| queries a second | 973 | 975 | +0.2% | -16.4 to 21.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 468 | 362 | -22.7% | -1,304 to 1,091 | no difference beyond the noise |
| latency, 99th percentile (ms) | 958 | 814 | -15.0% | -2,854 to 2,567 | no difference beyond the noise |
| latency, mean (ms) | 94.3 | 79.6 | -15.6% | -221 to 191 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 660 | +28.8% | 21.7 to 273 | **WORSE** |
| pages holding data, mean (MB) | 452 | 505 | +11.8% | -11.1 to 118 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 140,255 | 135,328 | -3.5% | -23,650 to 13,795 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.134 | +1.7% | -0.0101 to 0.0147 | no difference beyond the noise |
| host CPU-seconds | 158 | 161 | +1.7% | -13.3 to 18.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 13.3 | 12.3 | -7.5% | -14.4 to 12.4 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 22.3 |  | 18.5 to 26.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
