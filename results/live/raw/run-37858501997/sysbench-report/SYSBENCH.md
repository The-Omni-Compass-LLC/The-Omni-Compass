# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.5% | -5.52 to 8.4 | no difference beyond the noise |
| throughput (transactions a second) | 292 | 294 | +0.4% | -4.06 to 6.45 | no difference beyond the noise |
| queries a second | 4,679 | 4,698 | +0.4% | -65 to 103 | no difference beyond the noise |
| latency, 95th percentile (ms) | 3.32 | 3.12 | -6.3% | -0.638 to 0.219 | no difference beyond the noise |
| latency, 99th percentile (ms) | 4.57 | 4.44 | -2.9% | -0.743 to 0.478 | no difference beyond the noise |
| latency, mean (ms) | 1.42 | 1.36 | -4.6% | -0.154 to 0.0244 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 224 | -56.3% | -292 to -285 | better |
| pages holding data, mean (MB) | 439 | 188 | -57.1% | -254 to -247 | better |
| pages read from disk into the pool (misses) | 169,531 | 301,649 | +77.9% | 128,370 to 135,867 | shown, not judged |
| host CPU busy (share of the run) | 0.1 | 0.0992 | -1.1% | -0.0117 to 0.00955 | no difference beyond the noise |
| host CPU-seconds | 40.4 | 40 | -1.0% | -4.83 to 4.04 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.36 | 1.33 | -1.6% | -0.139 to 0.0966 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 292 | -0.6% | -6.75 to 3.09 | no difference beyond the noise |
| throughput (transactions a second) | 294 | 292 | -0.6% | -6.75 to 3.33 | no difference beyond the noise |
| queries a second | 4,701 | 4,674 | -0.6% | -108 to 53.3 | no difference beyond the noise |
| latency, 95th percentile (ms) | 3.66 | 3.59 | -1.8% | -0.0682 to -0.0625 | better |
| latency, 99th percentile (ms) | 4.85 | 4.82 | -0.6% | -0.363 to 0.303 | no difference beyond the noise |
| latency, mean (ms) | 2.75 | 2.73 | -0.7% | -0.0646 to 0.0276 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 517 | +1.0% | -395 to 406 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 464 | +0.5% | -337 to 342 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 456,915 | 531,776 | +16.4% | -515,573 to 665,294 | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.219 | -1.2% | -0.00308 to -0.0022 | better |
| host CPU-seconds | 266 | 263 | -1.2% | -3.69 to -2.61 | better |
| host CPU-seconds per 1,000 transactions inside the line | 2.94 | 2.93 | -0.6% | -0.0711 to 0.0378 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.7 |  | -0.89 to 28.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 188 | 192 | +1.9% | 0.263 to 6.81 | better |
| throughput (transactions a second) | 194 | 195 | +0.4% | -2.59 to 3.98 | no difference beyond the noise |
| queries a second | 3,877 | 3,891 | +0.4% | -51.9 to 79.5 | no difference beyond the noise |
| latency, 95th percentile (ms) | 9.22 | 8.04 | -12.9% | -2.33 to -0.0416 | better |
| latency, 99th percentile (ms) | 14.4 | 12 | -16.4% | -6.38 to 1.65 | no difference beyond the noise |
| latency, mean (ms) | 5.83 | 5.26 | -9.7% | -1.4 to 0.266 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 814 | +59.0% | 192 to 413 | **WORSE** |
| pages holding data, mean (MB) | 461 | 699 | +51.7% | 158 to 318 | **WORSE** |
| pages read from disk into the pool (misses) | 430,621 | 200,534 | -53.4% | -278,411 to -181,763 | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.202 | -5.6% | -0.0149 to -0.00919 | better |
| host CPU-seconds | 231 | 218 | -5.7% | -16.6 to -9.73 | better |
| host CPU-seconds per 1,000 transactions inside the line | 3.99 | 3.7 | -7.4% | -0.4 to -0.193 | better |
| buffer pool size changes written (the knob's moves) | 0 | 22.3 |  | 17.2 to 27.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,923 | 2,921 | -0.1% | -11.5 to 8.23 | no difference beyond the noise |
| throughput (transactions a second) | 2,930 | 2,929 | -0.0% | -17 to 15.2 | no difference beyond the noise |
| queries a second | 2,930 | 2,929 | -0.0% | -17 to 15.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.365 | 0.363 | -0.5% | -0.0106 to 0.00661 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.467 | 0.464 | -0.6% | -0.0347 to 0.0287 | no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.203 | +0.8% | -0.00124 to 0.00461 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 626 | +22.2% | -430 to 658 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 528 | +14.3% | -350 to 482 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 262,586 | 219,665 | -16.3% | -365,074 to 279,232 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.103 | -0.1% | -0.00689 to 0.00669 | no difference beyond the noise |
| host CPU-seconds | 115 | 115 | -0.1% | -8.45 to 8.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.128 | 0.128 | -0.0% | -0.00974 to 0.00969 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 |  | 0.744 to 15.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1.73 | 1.53 | -11.6% | -1.68 to 1.28 | no difference beyond the noise |
| throughput (transactions a second) | 975 | 975 | +0.0% | -5.46 to 6.01 | no difference beyond the noise |
| queries a second | 975 | 975 | +0.0% | -5.46 to 6.01 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.89 | 1.92 | +1.6% | -0.198 to 0.259 | no difference beyond the noise |
| latency, 99th percentile (ms) | 4.55 | 5.29 | +16.1% | 0.0293 to 1.44 | **WORSE** |
| latency, mean (ms) | 1.18 | 1.2 | +2.0% | -0.0409 to 0.0868 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 577 | +12.7% | 13.7 to 116 | **WORSE** |
| pages holding data, mean (MB) | 450 | 476 | +5.9% | -41.8 to 94.5 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 138,999 | 142,763 | +2.7% | -12,264 to 19,792 | shown, not judged |
| host CPU busy (share of the run) | 0.148 | 0.147 | -1.0% | -0.0326 to 0.0298 | no difference beyond the noise |
| host CPU-seconds | 153 | 152 | -0.9% | -33.1 to 30.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 325 | 349 | +7.5% | -231 to 280 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 22.7 |  | 19.8 to 25.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
