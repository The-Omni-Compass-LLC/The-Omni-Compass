# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.3% | -6.1 to 4.21 | no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.4% | -5.72 to 3.25 | no difference beyond the noise |
| queries a second | 4,724 | 4,704 | -0.4% | -91.5 to 52.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.37 | 5.31 | -1.2% | -0.746 to 0.621 | no difference beyond the noise |
| latency, 99th percentile (ms) | 7.48 | 7.3 | -2.3% | -1.54 to 1.19 | no difference beyond the noise |
| latency, mean (ms) | 3.44 | 3.46 | +0.8% | -0.0942 to 0.15 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 495 | -3.3% | -52.2 to 18.4 | no difference beyond the noise |
| pages holding data, mean (MB) | 445 | 411 | -7.5% | -70.1 to 3.23 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,617 | 250,676 | +2.9% | -13,304 to 27,420 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.208 | +1.9% | 0.000758 to 0.00719 | **WORSE** |
| host CPU-seconds | 113 | 115 | +2.3% | 1 to 4.08 | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 2.51 | 2.57 | +2.5% | 0.00909 to 0.117 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.1% | -0.653 to 0.272 | no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.1% | -0.631 to 0.304 | no difference beyond the noise |
| queries a second | 4,719 | 4,716 | -0.1% | -10.1 to 4.86 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.15 | 4.08 | -1.8% | -0.262 to 0.113 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.54 | 5.47 | -1.2% | -0.45 to 0.316 | no difference beyond the noise |
| latency, mean (ms) | 3.24 | 3.22 | -0.6% | -0.125 to 0.0883 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 443 | -13.4% | -208 to 70.6 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 401 | -13.2% | -153 to 31.4 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,814 | 826,435 | +26.4% | -213,355 to 558,597 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.197 | -0.2% | -0.0129 to 0.012 | no difference beyond the noise |
| host CPU-seconds | 327 | 327 | -0.1% | -22.7 to 22.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.42 | 2.42 | -0.0% | -0.162 to 0.161 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 1.04 to 19 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 192 | +0.2% | -1.9 to 2.66 | no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.5% | -3.77 to 1.95 | no difference beyond the noise |
| queries a second | 3,948 | 3,930 | -0.5% | -75.5 to 39.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 8.58 | 7.63 | -11.1% | -6.86 to 4.95 | no difference beyond the noise |
| latency, 99th percentile (ms) | 38 | 30.3 | -20.2% | -34.5 to 19.2 | no difference beyond the noise |
| latency, mean (ms) | 4.79 | 4.71 | -1.6% | -1.72 to 1.56 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 410 | -19.9% | -189 to -14.6 | better |
| pages holding data, mean (MB) | 462 | 369 | -20.0% | -160 to -24.8 | better |
| pages read from disk into the pool (misses) | 614,990 | 881,367 | +43.3% | -66,106 to 598,860 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.19 | +2.4% | -0.00123 to 0.0103 | no difference beyond the noise |
| host CPU-seconds | 329 | 337 | +2.4% | -2.26 to 18.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.76 | 3.85 | +2.2% | -0.0514 to 0.215 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | 7.6 to 19.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,945 | -0.0% | -5.76 to 4.47 | no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,952 | -0.1% | -3.15 to -0.502 | **WORSE** |
| queries a second | 2,954 | 2,952 | -0.1% | -3.15 to -0.502 | **WORSE** |
| latency, 95th percentile (ms) | 0.334 | 0.35 | +4.9% | -0.000208 to 0.0329 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.473 | 0.473 | +0.0% | -0.0199 to 0.0199 | same |
| latency, mean (ms) | 0.23 | 0.216 | -6.1% | -0.0841 to 0.0561 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 440 | -14.1% | -128 to -16.9 | better |
| pages holding data, mean (MB) | 463 | 399 | -14.0% | -93.6 to -36.3 | better |
| pages read from disk into the pool (misses) | 367,507 | 454,443 | +23.7% | 6,769 to 167,103 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.116 | +13.0% | 0.00804 to 0.0185 | **WORSE** |
| host CPU-seconds | 170 | 192 | +13.4% | 13.5 to 31.9 | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.126 | 0.143 | +13.4% | 0.00991 to 0.0238 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 2.16 to 12.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.58 | 4.14 | +15.6% | -9.41 to 10.5 | no difference beyond the noise |
| throughput (transactions a second) | 983 | 982 | -0.1% | -3.66 to 2.19 | no difference beyond the noise |
| queries a second | 983 | 982 | -0.1% | -3.66 to 2.19 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.87 | 1.88 | +0.5% | -0.314 to 0.333 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.54 | 3.53 | -0.3% | -1.36 to 1.34 | no difference beyond the noise |
| latency, mean (ms) | 1.23 | 1.19 | -3.2% | -0.796 to 0.718 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 485 | -5.2% | -121 to 67.9 | no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 415 | -8.5% | -156 to 78.3 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,157 | 212,034 | +12.1% | -72,511 to 118,264 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.158 | +24.2% | -0.153 to 0.214 | no difference beyond the noise |
| host CPU-seconds | 196 | 244 | +24.7% | -235 to 332 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 198 | 185 | -6.8% | -758 to 731 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | -10.5 to 32.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
