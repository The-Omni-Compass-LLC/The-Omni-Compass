# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 294 | +0.7% | 1.16 to 3.14 | better |
| throughput (transactions a second) | 293 | 295 | +0.8% | 0.15 to 4.34 | better |
| queries a second | 4,687 | 4,723 | +0.8% | 2.4 to 69.5 | better |
| latency, 95th percentile (ms) | 5.25 | 5.25 | -0.0% | -0.408 to 0.407 | no difference beyond the noise |
| latency, 99th percentile (ms) | 7.34 | 7.34 | +0.0% | -0.989 to 0.989 | same |
| latency, mean (ms) | 3.36 | 3.4 | +1.1% | -0.0331 to 0.107 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 502 | -1.9% | -24.8 to 5.36 | no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 418 | -6.5% | -54.9 to -3.4 | better |
| pages read from disk into the pool (misses) | 244,343 | 245,843 | +0.6% | -5,970 to 8,969 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.201 | +3.6% | -0.00201 to 0.016 | no difference beyond the noise |
| host CPU-seconds | 107 | 111 | +3.8% | -1.09 to 9.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.4 | 2.48 | +3.1% | -0.041 to 0.189 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.1% | -0.701 to 1.28 | no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -0.856 to 1.38 | no difference beyond the noise |
| queries a second | 4,720 | 4,725 | +0.1% | -13.7 to 22.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.13 | 4.05 | -1.8% | -0.258 to 0.11 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.54 | -1.2% | -0.444 to 0.312 | no difference beyond the noise |
| latency, mean (ms) | 3.19 | 3.19 | -0.0% | -0.0803 to 0.0773 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 447 | -12.7% | -210 to 79.9 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 402 | -13.0% | -165 to 44.8 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,269 | 843,557 | +29.1% | -245,039 to 625,613 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.192 | +1.2% | -0.00486 to 0.00928 | no difference beyond the noise |
| host CPU-seconds | 314 | 318 | +1.4% | -7.75 to 16.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.36 | +1.3% | -0.0536 to 0.113 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 1.5 to 11.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 185 | 185 | -0.1% | -2.14 to 1.78 | no difference beyond the noise |
| throughput (transactions a second) | 195 | 196 | +0.3% | -2.85 to 3.99 | no difference beyond the noise |
| queries a second | 3,900 | 3,911 | +0.3% | -56.9 to 79.7 | no difference beyond the noise |
| latency, 95th percentile (ms) | 11 | 11.2 | +2.3% | -2.06 to 2.57 | no difference beyond the noise |
| latency, 99th percentile (ms) | 198 | 159 | -19.5% | -326 to 249 | no difference beyond the noise |
| latency, mean (ms) | 9.15 | 8.3 | -9.3% | -6.31 to 4.61 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 463 | -9.6% | -96.2 to -1.69 | better |
| pages holding data, mean (MB) | 461 | 412 | -10.6% | -85.9 to -11.4 | better |
| pages read from disk into the pool (misses) | 612,824 | 728,901 | +18.9% | -98,652 to 330,806 | shown, not judged |
| host CPU busy (share of the run) | 0.218 | 0.223 | +2.0% | -0.00365 to 0.0124 | no difference beyond the noise |
| host CPU-seconds | 393 | 401 | +2.0% | -6.47 to 22.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.62 | 4.72 | +2.1% | -0.114 to 0.309 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | 9.52 to 14.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,913 | 2,910 | -0.1% | -10.7 to 5.25 | no difference beyond the noise |
| throughput (transactions a second) | 2,941 | 2,941 | +0.0% | -17.2 to 17.4 | no difference beyond the noise |
| queries a second | 2,941 | 2,941 | +0.0% | -17.2 to 17.4 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.43 | 0.461 | +7.2% | -0.122 to 0.184 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.591 | 0.608 | +2.9% | -0.0573 to 0.0919 | no difference beyond the noise |
| latency, mean (ms) | 0.179 | 0.183 | +2.3% | -0.00853 to 0.0168 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 440 | -14.0% | -140 to -4 | better |
| pages holding data, mean (MB) | 464 | 403 | -13.1% | -118 to -3.74 | better |
| pages read from disk into the pool (misses) | 367,414 | 454,487 | +23.7% | -15,903 to 190,049 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.142 | +2.5% | -0.00938 to 0.0162 | no difference beyond the noise |
| host CPU-seconds | 248 | 254 | +2.4% | -16.1 to 28.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.186 | 0.19 | +2.5% | -0.0114 to 0.0208 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 0.0313 to 9.97 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 14.7 | 13.5 | -7.9% | -11.8 to 9.44 | no difference beyond the noise |
| throughput (transactions a second) | 984 | 984 | -0.0% | -6.57 to 6.35 | no difference beyond the noise |
| queries a second | 984 | 984 | -0.0% | -6.57 to 6.35 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.57 | 1.65 | +4.8% | -0.123 to 0.274 | no difference beyond the noise |
| latency, 99th percentile (ms) | 2.87 | 2.88 | +0.5% | -0.47 to 0.498 | no difference beyond the noise |
| latency, mean (ms) | 1.01 | 1.02 | +0.9% | -0.0561 to 0.0736 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 419 | -18.2% | -104 to -81.7 | better |
| pages holding data, mean (MB) | 453 | 355 | -21.5% | -118 to -76.8 | better |
| pages read from disk into the pool (misses) | 189,017 | 256,485 | +35.7% | 61,158 to 73,777 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.17 | +44.9% | -0.0486 to 0.154 | no difference beyond the noise |
| host CPU-seconds | 181 | 263 | +45.4% | -76.7 to 241 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 32.3 | 45.6 | +41.3% | -18 to 44.7 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 7.61 to 25.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
