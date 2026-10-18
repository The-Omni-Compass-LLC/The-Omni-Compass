# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 291 | -0.6% | -7.22 to 3.79 | no difference beyond the noise |
| throughput (transactions a second) | 293 | 291 | -0.6% | -7.16 to 3.73 | no difference beyond the noise |
| queries a second | 4,683 | 4,655 | -0.6% | -115 to 59.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.79 | 4.91 | +2.4% | -0.133 to 0.363 | no difference beyond the noise |
| latency, 99th percentile (ms) | 6.1 | 6.17 | +1.2% | -0.562 to 0.706 | no difference beyond the noise |
| latency, mean (ms) | 2.85 | 2.93 | +2.9% | 0.0617 to 0.106 | **WORSE** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 171 | -66.7% | -343 to -340 | better |
| pages holding data, mean (MB) | 440 | 149 | -66.2% | -317 to -265 | better |
| pages read from disk into the pool (misses) | 169,349 | 334,300 | +97.4% | 161,067 to 168,835 | shown, not judged |
| host CPU busy (share of the run) | 0.223 | 0.226 | +1.6% | 0.000105 to 0.00716 | **WORSE** |
| host CPU-seconds | 89.4 | 90.8 | +1.6% | 0.0404 to 2.89 | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 2.97 | 3.04 | +2.2% | 0.0135 to 0.12 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.2% | -1.31 to 2.63 | no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.3% | -1.02 to 2.6 | no difference beyond the noise |
| queries a second | 4,685 | 4,698 | +0.3% | -16.3 to 41.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 3.68 | 3.75 | +1.8% | 0.067 to 0.067 | **WORSE** |
| latency, 99th percentile (ms) | 5.09 | 5.06 | -0.6% | -0.379 to 0.317 | no difference beyond the noise |
| latency, mean (ms) | 2.75 | 2.81 | +2.3% | 0.0144 to 0.112 | **WORSE** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 258 | -49.5% | -476 to -31.4 | better |
| pages holding data, mean (MB) | 461 | 220 | -52.4% | -356 to -128 | better |
| pages read from disk into the pool (misses) | 456,881 | 1,035,506 | +126.6% | 377,919 to 779,329 | shown, not judged |
| host CPU busy (share of the run) | 0.222 | 0.226 | +2.0% | -0.00389 to 0.0126 | no difference beyond the noise |
| host CPU-seconds | 266 | 271 | +2.0% | -5.2 to 15.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.96 | 3.01 | +1.7% | -0.058 to 0.159 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 3.43 to 16.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 181 | 185 | +2.0% | -4.69 to 11.8 | no difference beyond the noise |
| throughput (transactions a second) | 192 | 192 | +0.0% | -3.95 to 3.95 | no difference beyond the noise |
| queries a second | 3,850 | 3,850 | +0.0% | -78.9 to 79.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 11.6 | 9.5 | -18.0% | -6.51 to 2.34 | no difference beyond the noise |
| latency, 99th percentile (ms) | 158 | 193 | +22.1% | -91.9 to 162 | no difference beyond the noise |
| latency, mean (ms) | 8.77 | 9.17 | +4.5% | -2.15 to 2.94 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 895 | +74.8% | -7.01 to 773 | no difference beyond the noise |
| pages holding data, mean (MB) | 459 | 773 | +68.3% | 36.6 to 591 | **WORSE** |
| pages read from disk into the pool (misses) | 434,039 | 230,443 | -46.9% | -493,723 to 86,530 | shown, not judged |
| host CPU busy (share of the run) | 0.235 | 0.225 | -4.1% | -0.036 to 0.0166 | no difference beyond the noise |
| host CPU-seconds | 285 | 274 | -4.1% | -42.6 to 19.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.07 | 4.77 | -5.9% | -0.902 to 0.301 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 23.3 |  | 13.9 to 32.7 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,906 | 2,910 | +0.1% | -12 to 18.7 | no difference beyond the noise |
| throughput (transactions a second) | 2,909 | 2,912 | +0.1% | -10.8 to 17.8 | no difference beyond the noise |
| queries a second | 2,909 | 2,912 | +0.1% | -10.8 to 17.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.301 | 0.303 | +0.7% | -0.0183 to 0.0223 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.395 | 0.381 | -3.5% | -0.0314 to 0.00339 | no difference beyond the noise |
| latency, mean (ms) | 0.123 | 0.125 | +1.3% | -0.00843 to 0.0115 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 329 | -35.8% | -536 to 170 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 303 | -34.4% | -491 to 173 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 263,217 | 456,511 | +73.4% | -120,173 to 506,761 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.105 | -1.0% | -0.00725 to 0.0052 | no difference beyond the noise |
| host CPU-seconds | 129 | 128 | -1.0% | -9.01 to 6.33 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.144 | 0.142 | -1.1% | -0.0105 to 0.0074 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | -1.4 to 10.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.29 | 6.75 | +7.2% | -4.57 to 5.48 | no difference beyond the noise |
| throughput (transactions a second) | 979 | 976 | -0.3% | -11.4 to 5.33 | no difference beyond the noise |
| queries a second | 979 | 976 | -0.3% | -11.4 to 5.33 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.73 | 2.06 | +19.2% | 0.0939 to 0.57 | **WORSE** |
| latency, 99th percentile (ms) | 3 | 4.82 | +60.6% | 1.44 to 2.2 | **WORSE** |
| latency, mean (ms) | 1.09 | 1.45 | +33.1% | 0.0612 to 0.658 | **WORSE** |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 701 | +36.9% | -304 to 682 | no difference beyond the noise |
| pages holding data, mean (MB) | 450 | 546 | +21.4% | -171 to 364 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 139,508 | 124,289 | -10.9% | -100,220 to 69,782 | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.229 | +76.6% | -0.0734 to 0.273 | no difference beyond the noise |
| host CPU-seconds | 134 | 239 | +78.0% | -78.9 to 289 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 70 | 135 | +92.9% | -147 to 277 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 25.7 |  | 9.13 to 42.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
