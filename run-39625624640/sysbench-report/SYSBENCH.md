# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 279 | 281 | +0.6% | -3.88 to 7.47 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.1% | -8 to 8.58 | EVEN, no difference beyond the noise |
| queries a second | 4,709 | 4,713 | +0.1% | -128 to 137 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 10.1 | 8.82 | -12.4% | -8.44 to 5.95 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 154 | 165 | +7.7% | -71.1 to 94.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.64 | 6.97 | +4.9% | -2.46 to 3.12 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 455 | -11.1% | -134 to 20 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 445 | 405 | -9.1% | -122 to 41.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,582 | 258,709 | +5.3% | -29,377 to 55,631 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.167 | +1.1% | -0.00604 to 0.00978 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98.8 | 99.9 | +1.1% | -3.99 to 6.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.32 | 2.33 | +0.5% | -0.134 to 0.157 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 2.87 to 10.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.0% | -1.25 to 1.25 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.0% | -1.03 to 1.21 | EVEN, no difference beyond the noise |
| queries a second | 4,718 | 4,719 | +0.0% | -16.5 to 19.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.03 | 4.03 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 5.54 | 5.54 | +0.0% | -0.249 to 0.25 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.06 | 3.09 | +1.1% | -0.0357 to 0.103 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 505 | -1.3% | -104 to 90.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 444 | -3.8% | -156 to 121 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,179 | 683,968 | +4.4% | -333,659 to 391,238 | shown, not judged |
| host CPU busy (share of the run) | 0.242 | 0.245 | +1.3% | -0.00288 to 0.00915 | EVEN, no difference beyond the noise |
| host CPU-seconds | 430 | 435 | +1.3% | -5 to 16.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.19 | 3.23 | +1.3% | -0.0256 to 0.107 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 12.5 to 18.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 195 | +0.3% | -3.21 to 4.21 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.0% | -2.51 to 2.56 | EVEN, no difference beyond the noise |
| queries a second | 3,948 | 3,949 | +0.0% | -50.2 to 51.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.1 | 6.75 | -4.9% | -1.6 to 0.909 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12 | 11.3 | -6.1% | -2.72 to 1.26 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.26 | 4.14 | -2.7% | -0.829 to 0.596 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 616 | +20.4% | -8.78 to 217 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 543 | +17.6% | 15.9 to 147 | power given |
| pages read from disk into the pool (misses) | 619,414 | 452,268 | -27.0% | -347,109 to 12,817 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.205 | -2.2% | -0.0354 to 0.0262 | EVEN, no difference beyond the noise |
| host CPU-seconds | 371 | 362 | -2.3% | -59.7 to 42.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.17 | 4.07 | -2.6% | -0.747 to 0.534 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18 |  | 8.06 to 27.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,933 | 2,931 | -0.0% | -2.64 to 0.044 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,935 | 2,935 | -0.0% | -1.93 to 0.847 | EVEN, no difference beyond the noise |
| queries a second | 2,935 | 2,935 | -0.0% | -1.93 to 0.847 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.226 | 0.214 | -5.2% | -0.0303 to 0.00698 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.422 | 0.405 | -4.1% | -0.0439 to 0.00923 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.142 | 0.144 | +1.0% | -0.0115 to 0.0143 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 480 | -6.3% | -180 to 115 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 438 | -5.5% | -174 to 123 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,408 | 386,779 | +5.3% | -155,121 to 193,863 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.122 | +0.3% | -0.00196 to 0.00262 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 222 | +0.3% | -3.58 to 4.75 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.164 | 0.165 | +0.3% | -0.00252 to 0.00362 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 |  | 3.16 to 13.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 127 | 133 | +4.7% | -35.4 to 47.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 981 | 980 | -0.1% | -5.72 to 4.51 | EVEN, no difference beyond the noise |
| queries a second | 981 | 980 | -0.1% | -5.72 to 4.51 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.35 | 1.34 | -0.8% | -0.226 to 0.206 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.06 | 1.95 | -5.3% | -0.744 to 0.528 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.846 | -19.8% | -1.13 to 0.71 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 469 | -8.4% | -108 to 22.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 452 | 377 | -16.7% | -164 to 12.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 190,127 | 251,540 | +32.3% | 2,861 to 119,965 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.178 | -1.2% | -0.0236 to 0.0194 | EVEN, no difference beyond the noise |
| host CPU-seconds | 320 | 316 | -1.2% | -41.2 to 33.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.72 | 5.22 | -8.7% | -3.57 to 2.58 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17 |  | 5.62 to 28.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
