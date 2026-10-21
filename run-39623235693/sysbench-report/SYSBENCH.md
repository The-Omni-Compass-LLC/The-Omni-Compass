# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.3% | -8.48 to 6.81 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.2% | -4.38 to 3.28 | EVEN, no difference beyond the noise |
| queries a second | 4,711 | 4,702 | -0.2% | -70.1 to 52.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.25 | 5.31 | +1.1% | -1.32 to 1.43 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.45 | 7.58 | +1.8% | -2.79 to 3.06 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.31 | 3.31 | +0.1% | -0.181 to 0.187 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 520 | +1.6% | -96.9 to 113 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 459 | +2.3% | -101 to 121 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,185 | 232,589 | -5.1% | -64,023 to 38,833 | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.19 | +0.9% | -0.0056 to 0.00907 | EVEN, no difference beyond the noise |
| host CPU-seconds | 104 | 105 | +1.1% | -3.07 to 5.32 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.32 | 2.35 | +1.4% | -0.0157 to 0.0791 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | -1.39 to 16.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.2% | -0.946 to 1.95 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.2% | -0.918 to 2.18 | EVEN, no difference beyond the noise |
| queries a second | 4,712 | 4,722 | +0.2% | -14.7 to 34.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.1 | 3.98 | -3.0% | -0.404 to 0.159 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.06 | 5.99 | -1.2% | -0.228 to 0.0833 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.02 | 2.97 | -1.6% | -0.219 to 0.12 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 580 | +13.4% | -47.8 to 185 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 507 | +9.9% | -25.4 to 117 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,819 | 516,552 | -21.0% | -330,898 to 56,364 | shown, not judged |
| host CPU busy (share of the run) | 0.236 | 0.232 | -1.5% | -0.0154 to 0.00824 | EVEN, no difference beyond the noise |
| host CPU-seconds | 420 | 413 | -1.5% | -27.2 to 14.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.12 | 3.07 | -1.7% | -0.21 to 0.105 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 12.5 to 20.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 193 | +1.0% | 0.854 to 3.13 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.6% | -0.893 to 3.13 | EVEN, no difference beyond the noise |
| queries a second | 3,920 | 3,942 | +0.6% | -17.9 to 62.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.01 | 8.58 | -4.7% | -1.04 to 0.188 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.6 | 12.9 | -5.3% | -2.53 to 1.08 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.44 | 5.33 | -1.9% | -0.626 to 0.421 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 612 | +19.5% | 19.2 to 181 | power given |
| pages holding data, mean (MB) | 461 | 535 | +16.1% | 44.7 to 104 | power given |
| pages read from disk into the pool (misses) | 616,755 | 471,366 | -23.6% | -243,524 to -47,255 | shown, not judged |
| host CPU busy (share of the run) | 0.28 | 0.279 | -0.4% | -0.00371 to 0.0017 | EVEN, no difference beyond the noise |
| host CPU-seconds | 493 | 491 | -0.4% | -6.53 to 3.01 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.65 | 5.57 | -1.4% | -0.116 to -0.0417 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 17.7 |  | 10.5 to 24.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,944 | -0.2% | -18.7 to 8.71 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,955 | 2,953 | -0.1% | -11.8 to 6.81 | EVEN, no difference beyond the noise |
| queries a second | 2,955 | 2,953 | -0.1% | -11.8 to 6.81 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.34 | 0.332 | -2.4% | -0.0653 to 0.0487 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.465 | 0.473 | +1.8% | -0.082 to 0.0987 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.214 | +7.3% | -0.00903 to 0.0383 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 674 | +31.6% | 107 to 217 | power given |
| pages holding data, mean (MB) | 464 | 560 | +20.7% | 39.2 to 153 | power given |
| pages read from disk into the pool (misses) | 368,666 | 246,841 | -33.0% | -147,197 to -96,454 | shown, not judged |
| host CPU busy (share of the run) | 0.162 | 0.164 | +1.3% | -0.017 to 0.0213 | EVEN, no difference beyond the noise |
| host CPU-seconds | 284 | 288 | +1.3% | -29.5 to 37.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.211 | 0.214 | +1.5% | -0.0225 to 0.0288 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18 |  | 4.85 to 31.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 22.2 | 23.5 | +6.0% | -22.9 to 25.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 984 | -0.1% | -5.14 to 4.02 | EVEN, no difference beyond the noise |
| queries a second | 984 | 984 | -0.1% | -5.14 to 4.02 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.57 | 1.61 | +2.3% | -0.611 to 0.683 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.47 | 2.67 | +8.1% | -0.94 to 1.34 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.982 | 1 | +2.3% | -0.155 to 0.199 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 560 | +9.3% | -107 to 203 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 470 | +3.7% | -99 to 133 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,883 | 184,595 | -2.8% | -83,557 to 72,981 | shown, not judged |
| host CPU busy (share of the run) | 0.227 | 0.242 | +6.4% | -0.0933 to 0.122 | EVEN, no difference beyond the noise |
| host CPU-seconds | 399 | 424 | +6.3% | -161 to 212 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 41.9 | 62.2 | +48.3% | -86.4 to 127 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19.7 |  | 13.9 to 25.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
