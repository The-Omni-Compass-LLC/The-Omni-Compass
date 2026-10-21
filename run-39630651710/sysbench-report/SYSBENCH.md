# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.4% | -3.95 to 1.83 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.3% | -4.23 to 2.41 | EVEN, no difference beyond the noise |
| queries a second | 4,722 | 4,707 | -0.3% | -67.6 to 38.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.18 | 5.18 | -0.0% | -0.234 to 0.231 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.21 | 7.34 | +1.8% | -0.191 to 0.45 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.4 | 3.38 | -0.6% | -0.124 to 0.0814 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 509 | -0.5% | -30.2 to 24.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 451 | 411 | -8.8% | -132 to 53.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 246,595 | 248,448 | +0.8% | -52,161 to 55,869 | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.2 | -0.6% | -0.00835 to 0.00606 | EVEN, no difference beyond the noise |
| host CPU-seconds | 111 | 111 | -0.5% | -4.59 to 3.53 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.47 | 2.47 | -0.1% | -0.0828 to 0.0795 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | -0.404 to 11.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.0% | -2.86 to 2.93 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.1% | -2.09 to 1.53 | EVEN, no difference beyond the noise |
| queries a second | 4,731 | 4,726 | -0.1% | -33.4 to 24.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.69 | 2.66 | -1.2% | -0.102 to 0.0373 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.89 | 5.19 | -11.9% | -4.17 to 2.78 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.67 | 2.39 | -10.6% | -0.845 to 0.278 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 538 | +5.1% | -33.1 to 85.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 479 | +3.9% | -25.4 to 61.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,291 | 591,456 | -9.6% | -150,066 to 24,395 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.162 | +0.3% | -0.0057 to 0.00678 | EVEN, no difference beyond the noise |
| host CPU-seconds | 289 | 290 | +0.3% | -10.3 to 12.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.16 | 2.17 | +0.3% | -0.0552 to 0.0693 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14 |  | 14 to 14 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | +0.2% | -1.55 to 2.35 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | -0.0% | -2.22 to 2.12 | EVEN, no difference beyond the noise |
| queries a second | 3,905 | 3,904 | -0.0% | -44.4 to 42.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.04 | 7.05 | +0.1% | -0.84 to 0.858 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 11.9 | 10.9 | -7.8% | -4.28 to 2.43 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.93 | 3.95 | +0.5% | -0.315 to 0.354 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 523 | +2.2% | -67.8 to 90.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 473 | +2.5% | -51.2 to 74.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 618,608 | 588,118 | -4.9% | -194,777 to 133,795 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.182 | -0.9% | -0.0129 to 0.00958 | EVEN, no difference beyond the noise |
| host CPU-seconds | 340 | 337 | -1.0% | -24.1 to 17.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.83 | 3.79 | -1.1% | -0.284 to 0.196 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 9.5 to 19.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,953 | 2,948 | -0.2% | -10.9 to 0.112 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,967 | 2,963 | -0.1% | -6.52 to -0.581 | LOSS |
| queries a second | 2,967 | 2,963 | -0.1% | -6.52 to -0.581 | LOSS |
| latency, 95th percentile (ms) | 0.227 | 0.225 | -1.2% | -0.0178 to 0.0125 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.386 | 0.39 | +1.2% | -0.0154 to 0.0247 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.315 | 0.331 | +5.3% | -0.223 to 0.257 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 521 | +1.7% | -52.3 to 69.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 472 | +1.9% | -61.6 to 79.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,934 | 348,116 | -5.6% | -91,504 to 49,870 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.111 | +2.1% | -0.00776 to 0.0123 | EVEN, no difference beyond the noise |
| host CPU-seconds | 193 | 197 | +2.0% | -14.3 to 22 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.146 | +2.2% | -0.0103 to 0.0167 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 5.52 to 10.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 110 | 118 | +7.6% | 2.14 to 14.7 | GAIN |
| throughput (transactions a second) | 986 | 985 | -0.1% | -11.7 to 10.6 | EVEN, no difference beyond the noise |
| queries a second | 986 | 985 | -0.1% | -11.7 to 10.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 155 | 154 | -0.7% | -23.1 to 21.1 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 330 | 328 | -0.8% | -35 to 29.9 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 30.9 | 28 | -9.4% | -13.2 to 7.45 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 525 | +2.6% | -17 to 44 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 425 | -6.3% | -77.7 to 21 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 190,804 | 213,480 | +11.9% | -36,662 to 82,015 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.136 | +1.1% | -0.0226 to 0.0255 | EVEN, no difference beyond the noise |
| host CPU-seconds | 238 | 240 | +1.0% | -38.6 to 43.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.95 | 4.64 | -6.3% | -1.18 to 0.555 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 |  | 9.26 to 28.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
