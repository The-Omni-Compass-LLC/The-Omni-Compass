# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.3% | -7.62 to 5.94 | no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.4% | -7.34 to 5.26 | no difference beyond the noise |
| queries a second | 4,724 | 4,707 | -0.4% | -117 to 84.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 3 | 3.02 | +0.6% | -0.395 to 0.43 | no difference beyond the noise |
| latency, 99th percentile (ms) | 4.1 | 4.13 | +0.6% | -0.258 to 0.306 | no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.32 | -1.2% | -0.192 to 0.161 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 169 | -66.9% | -346 to -339 | better |
| pages holding data, mean (MB) | 439 | 145 | -67.0% | -315 to -274 | better |
| pages read from disk into the pool (misses) | 168,519 | 338,855 | +101.1% | 163,731 to 176,941 | shown, not judged |
| host CPU busy (share of the run) | 0.0979 | 0.0977 | -0.2% | -0.00296 to 0.0026 | no difference beyond the noise |
| host CPU-seconds | 39.5 | 39.4 | -0.2% | -1.24 to 1.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.31 | 1.31 | +0.1% | -0.0555 to 0.0576 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.1% | -2.75 to 2 | no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.1% | -3.36 to 2.75 | no difference beyond the noise |
| queries a second | 4,715 | 4,710 | -0.1% | -53.8 to 43.9 | no difference beyond the noise |
| latency, 95th percentile (ms) | 2.15 | 2.14 | -0.5% | -0.31 to 0.288 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.73 | 3.86 | +3.5% | -0.775 to 1.03 | no difference beyond the noise |
| latency, mean (ms) | 1.38 | 1.33 | -3.6% | -0.233 to 0.132 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 225 | -56.1% | -491 to -83.1 | better |
| pages holding data, mean (MB) | 462 | 212 | -54.2% | -430 to -70.4 | better |
| pages read from disk into the pool (misses) | 457,974 | 1,108,461 | +142.0% | 95,329 to 1,205,644 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.108 | -4.4% | -0.0224 to 0.0125 | no difference beyond the noise |
| host CPU-seconds | 136 | 130 | -4.4% | -27.2 to 15.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.51 | 1.45 | -4.3% | -0.308 to 0.179 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | -1.45 to 13.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 189 | 190 | +0.9% | -0.695 to 4.11 | no difference beyond the noise |
| throughput (transactions a second) | 195 | 194 | -0.4% | -4.15 to 2.7 | no difference beyond the noise |
| queries a second | 3,904 | 3,889 | -0.4% | -83.1 to 54.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 9.51 | 8.48 | -10.8% | -1.26 to -0.785 | better |
| latency, 99th percentile (ms) | 13.9 | 12.6 | -9.1% | -2.44 to -0.0836 | better |
| latency, mean (ms) | 5.63 | 5.44 | -3.4% | -0.265 to -0.123 | better |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 816 | +59.3% | 74.5 to 533 | **WORSE** |
| pages holding data, mean (MB) | 462 | 707 | +53.0% | 112 to 378 | **WORSE** |
| pages read from disk into the pool (misses) | 435,566 | 260,382 | -40.2% | -366,504 to 16,136 | shown, not judged |
| host CPU busy (share of the run) | 0.229 | 0.217 | -5.2% | -0.0236 to -7.04e-05 | better |
| host CPU-seconds | 248 | 235 | -5.1% | -25.2 to -0.321 | better |
| host CPU-seconds per 1,000 transactions inside the line | 4.26 | 4.01 | -6.0% | -0.459 to -0.0512 | better |
| buffer pool size changes written (the knob's moves) | 0 | 22 |  | 17 to 27 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,920 | 2,915 | -0.2% | -19 to 7.64 | no difference beyond the noise |
| throughput (transactions a second) | 2,931 | 2,928 | -0.1% | -10.2 to 3.96 | no difference beyond the noise |
| queries a second | 2,931 | 2,928 | -0.1% | -10.2 to 3.96 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.369 | 0.376 | +1.9% | -0.0104 to 0.0244 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.487 | 0.499 | +2.5% | -0.0222 to 0.0462 | no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.212 | +3.0% | -0.00686 to 0.0191 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 548 | +7.1% | -550 to 623 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 470 | +1.7% | -401 to 417 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 262,474 | 294,252 | +12.1% | -271,652 to 335,209 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.106 | +1.5% | -0.00384 to 0.00697 | no difference beyond the noise |
| host CPU-seconds | 116 | 118 | +1.6% | -4.58 to 8.32 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.13 | 0.132 | +1.8% | -0.00427 to 0.00898 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.33 |  | 0.609 to 18.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 48.3 | 48.7 | +0.7% | -22.3 to 23 | no difference beyond the noise |
| throughput (transactions a second) | 978 | 975 | -0.3% | -7.03 to 1.36 | no difference beyond the noise |
| queries a second | 978 | 975 | -0.3% | -7.03 to 1.36 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.52 | 1.56 | +2.7% | -0.663 to 0.746 | no difference beyond the noise |
| latency, 99th percentile (ms) | 11.1 | 9.24 | -17.0% | -54.8 to 51 | no difference beyond the noise |
| latency, mean (ms) | 1.21 | 1.15 | -5.4% | -1.45 to 1.32 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 542 | +5.8% | -304 to 364 | no difference beyond the noise |
| pages holding data, mean (MB) | 451 | 447 | -1.1% | -247 to 238 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 139,216 | 145,801 | +4.7% | -62,311 to 75,481 | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.212 | -1.1% | -0.0357 to 0.031 | no difference beyond the noise |
| host CPU-seconds | 249 | 247 | -1.0% | -40.6 to 35.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 17.2 | 16.6 | -3.3% | -11.3 to 10.2 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 21.7 |  | 6.49 to 36.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
