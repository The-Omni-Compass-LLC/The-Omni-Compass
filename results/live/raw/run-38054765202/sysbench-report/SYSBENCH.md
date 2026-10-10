# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.2% | -1.82 to 3.18 | no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.2% | -1.18 to 2.47 | no difference beyond the noise |
| queries a second | 4,697 | 4,707 | +0.2% | -18.9 to 39.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.12 | 5 | -2.4% | -0.597 to 0.353 | no difference beyond the noise |
| latency, 99th percentile (ms) | 7 | 6.91 | -1.2% | -0.558 to 0.392 | no difference beyond the noise |
| latency, mean (ms) | 3.25 | 3.27 | +0.7% | -0.101 to 0.148 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 484 | -5.5% | -67.9 to 12.1 | no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 414 | -7.5% | -107 to 39.3 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,343 | 243,156 | -0.1% | -25,106 to 24,730 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.19 | +2.3% | -0.00762 to 0.0161 | no difference beyond the noise |
| host CPU-seconds | 102 | 105 | +2.4% | -4.3 to 9.22 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.28 | 2.33 | +2.2% | -0.104 to 0.204 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | 0.495 to 14.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.5% | -2.5 to -0.16 | **WORSE** |
| throughput (transactions a second) | 296 | 294 | -0.4% | -2.76 to 0.198 | no difference beyond the noise |
| queries a second | 4,728 | 4,708 | -0.4% | -44.1 to 3.17 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.23 | 4.18 | -1.2% | -0.16 to 0.0583 | no difference beyond the noise |
| latency, 99th percentile (ms) | 6.13 | 6.06 | -1.2% | -0.489 to 0.343 | no difference beyond the noise |
| latency, mean (ms) | 3.2 | 3.19 | -0.5% | -0.0906 to 0.0566 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 517 | +1.0% | -127 to 138 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 463 | +0.4% | -119 to 122 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,923 | 616,884 | -6.0% | -323,993 to 245,915 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.189 | -0.8% | -0.00699 to 0.00414 | no difference beyond the noise |
| host CPU-seconds | 314 | 312 | -0.6% | -10.6 to 6.65 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.32 | -0.2% | -0.0592 to 0.0514 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 |  | 13.2 to 23.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 191 | -0.8% | -2.44 to -0.553 | **WORSE** |
| throughput (transactions a second) | 197 | 196 | -0.5% | -2.61 to 0.813 | no difference beyond the noise |
| queries a second | 3,943 | 3,925 | -0.5% | -52.2 to 16.3 | no difference beyond the noise |
| latency, 95th percentile (ms) | 8.58 | 8.95 | +4.3% | -0.0828 to 0.817 | no difference beyond the noise |
| latency, 99th percentile (ms) | 13.2 | 13.4 | +1.2% | -0.185 to 0.506 | no difference beyond the noise |
| latency, mean (ms) | 5.28 | 5.32 | +0.7% | -0.00208 to 0.0784 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 486 | -5.1% | -50.8 to -1.73 | better |
| pages holding data, mean (MB) | 462 | 430 | -6.8% | -50.1 to -13.1 | better |
| pages read from disk into the pool (misses) | 615,886 | 667,087 | +8.3% | -62,978 to 165,380 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.211 | +0.5% | -0.00464 to 0.00663 | no difference beyond the noise |
| host CPU-seconds | 337 | 339 | +0.6% | -6.67 to 11 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.83 | 3.88 | +1.4% | -0.059 to 0.168 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 23 |  | 16.4 to 29.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,951 | 2,948 | -0.1% | -5.22 to 0.414 | no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,952 | -0.1% | -7.41 to 4.43 | no difference beyond the noise |
| queries a second | 2,953 | 2,952 | -0.1% | -7.41 to 4.43 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.316 | 0.322 | +1.8% | -0.0229 to 0.0342 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.44 | 0.437 | -0.6% | -0.0256 to 0.0203 | no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.198 | +2.5% | -0.00376 to 0.0134 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 416 | -18.7% | -176 to -15.5 | better |
| pages holding data, mean (MB) | 463 | 376 | -18.8% | -162 to -12.2 | better |
| pages read from disk into the pool (misses) | 367,026 | 509,779 | +38.9% | 35,494 to 250,012 | shown, not judged |
| host CPU busy (share of the run) | 0.0937 | 0.0994 | +6.1% | -0.00302 to 0.0145 | no difference beyond the noise |
| host CPU-seconds | 155 | 165 | +6.4% | -4.75 to 24.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.115 | 0.122 | +6.5% | -0.00332 to 0.0182 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | -3.51 to 27.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 93 | 88 | -5.4% | -88.7 to 78.7 | no difference beyond the noise |
| throughput (transactions a second) | 988 | 984 | -0.4% | -14.6 to 6.74 | no difference beyond the noise |
| queries a second | 988 | 984 | -0.4% | -14.6 to 6.74 | no difference beyond the noise |
| latency, 95th percentile (ms) | 187 | 285 | +52.4% | -447 to 643 | no difference beyond the noise |
| latency, 99th percentile (ms) | 534 | 830 | +55.6% | -2,106 to 2,700 | no difference beyond the noise |
| latency, mean (ms) | 38.8 | 57.8 | +48.9% | -109 to 147 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 440 | -14.0% | -126 to -17.1 | better |
| pages holding data, mean (MB) | 453 | 360 | -20.6% | -163 to -24 | better |
| pages read from disk into the pool (misses) | 190,418 | 253,477 | +33.1% | 20,508 to 105,611 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.128 | -3.1% | -0.033 to 0.0249 | no difference beyond the noise |
| host CPU-seconds | 236 | 228 | -3.2% | -62 to 47.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.64 | 5.94 | +5.3% | -5.71 to 6.3 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 23.3 |  | 18.2 to 28.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
