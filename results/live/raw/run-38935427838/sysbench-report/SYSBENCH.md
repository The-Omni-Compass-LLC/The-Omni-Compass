# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.4% | -5.81 to 7.93 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.3% | -4.89 to 6.77 | EVEN, no difference beyond the noise |
| queries a second | 4,697 | 4,713 | +0.3% | -78.2 to 108 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.43 | 2.53 | +3.7% | -0.131 to 0.313 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.89 | 4.06 | +4.4% | -0.0541 to 0.394 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.23 | 1.27 | +2.8% | -0.109 to 0.179 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 329 | -35.7% | -334 to -30.9 | GAIN |
| pages holding data, mean (MB) | 442 | 285 | -35.4% | -300 to -12.8 | GAIN |
| pages read from disk into the pool (misses) | 239,667 | 313,631 | +30.9% | -7,238 to 155,165 | shown, not judged |
| host CPU busy (share of the run) | 0.0917 | 0.093 | +1.5% | -0.00125 to 0.00396 | EVEN, no difference beyond the noise |
| host CPU-seconds | 55.1 | 55.8 | +1.4% | -0.775 to 2.36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.23 | 1.25 | +1.1% | -0.0216 to 0.0483 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 287 | 286 | -0.2% | -5.03 to 3.92 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | +0.0% | -1.41 to 1.52 | EVEN, no difference beyond the noise |
| queries a second | 4,737 | 4,737 | +0.0% | -22.5 to 24.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.48 | 3.59 | +3.3% | -0.882 to 1.11 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 98.4 | 110 | +11.3% | -119 to 141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.81 | 5.31 | +10.5% | -3.66 to 4.67 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 442 | -13.7% | -145 to 4.55 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 401 | -13.0% | -122 to 1.51 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,505 | 855,267 | +30.7% | -169,431 to 570,955 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.167 | +0.8% | -0.00577 to 0.00837 | EVEN, no difference beyond the noise |
| host CPU-seconds | 296 | 299 | +0.8% | -10.3 to 15.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.27 | 2.29 | +1.0% | -0.0938 to 0.14 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 9.5 to 19.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 191 | -0.4% | -4.14 to 2.68 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | +0.0% | -4.06 to 4.11 | EVEN, no difference beyond the noise |
| queries a second | 3,901 | 3,902 | +0.0% | -81.3 to 82.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.3 | 8.03 | +10.1% | 0.528 to 0.944 | LOSS |
| latency, 99th percentile (ms) | 12.6 | 14.6 | +15.3% | -8.07 to 11.9 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.08 | 4.37 | +7.3% | -0.307 to 0.899 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 405 | -20.9% | -122 to -91.5 | GAIN |
| pages holding data, mean (MB) | 461 | 367 | -20.3% | -107 to -79.9 | GAIN |
| pages read from disk into the pool (misses) | 616,349 | 922,398 | +49.7% | 188,714 to 423,384 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.174 | +2.0% | -0.00285 to 0.00967 | EVEN, no difference beyond the noise |
| host CPU-seconds | 309 | 315 | +1.9% | -5.03 to 17 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.49 | 3.57 | +2.4% | -0.0597 to 0.226 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.3 |  | 11.5 to 17.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,935 | 2,934 | -0.1% | -6.99 to 3.96 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,940 | 2,939 | -0.1% | -7.68 to 4.54 | EVEN, no difference beyond the noise |
| queries a second | 2,940 | 2,939 | -0.1% | -7.68 to 4.54 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.284 | 0.279 | -1.6% | -0.0283 to 0.0189 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.445 | -2.3% | -0.041 to 0.0197 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.183 | 0.186 | +1.5% | -0.00512 to 0.0106 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 462 | -9.7% | -121 to 21.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 423 | -8.8% | -102 to 20.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,298 | 413,907 | +12.7% | -48,953 to 142,170 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.146 | +0.0% | -0.0042 to 0.00431 | EVEN, no difference beyond the noise |
| host CPU-seconds | 263 | 263 | -0.0% | -7.46 to 7.34 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.195 | 0.196 | +0.1% | -0.00516 to 0.0054 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 2.74 to 17.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 186 | 192 | +2.8% | -45.2 to 55.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 986 | 987 | +0.1% | -2.35 to 4.76 | EVEN, no difference beyond the noise |
| queries a second | 986 | 987 | +0.1% | -2.35 to 4.76 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 79.5 | 80.7 | +1.5% | -59.7 to 62 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 206 | 184 | -10.6% | -170 to 126 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 12.1 | 11.5 | -5.1% | -9.54 to 8.31 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 369 | -27.9% | -166 to -119 | GAIN |
| pages holding data, mean (MB) | 454 | 312 | -31.2% | -188 to -95.3 | GAIN |
| pages read from disk into the pool (misses) | 190,231 | 292,178 | +53.6% | 82,688 to 121,207 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.142 | +2.6% | -0.016 to 0.0233 | EVEN, no difference beyond the noise |
| host CPU-seconds | 244 | 251 | +2.6% | -29.2 to 42 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.95 | 2.89 | -1.9% | -1.43 to 1.31 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13 |  | 3.06 to 22.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
