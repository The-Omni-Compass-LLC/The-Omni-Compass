# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.2% | -3.25 to 4.38 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | +0.1% | -1.7 to 2.12 | EVEN, no difference beyond the noise |
| queries a second | 4,729 | 4,732 | +0.1% | -27.2 to 33.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.09 | 3 | -3.0% | -0.303 to 0.119 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.82 | 4.83 | +0.0% | -0.868 to 0.872 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.55 | 1.48 | -4.7% | -0.162 to 0.0171 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 393 | -23.3% | -347 to 108 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 442 | 338 | -23.5% | -317 to 109 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,371 | 285,033 | +16.2% | -82,833 to 162,157 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.107 | -0.7% | -0.00294 to 0.0015 | EVEN, no difference beyond the noise |
| host CPU-seconds | 64.8 | 64.3 | -0.7% | -1.78 to 0.883 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.44 | 1.43 | -0.9% | -0.0381 to 0.0126 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 0.0313 to 9.97 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.3% | -8.03 to 6.18 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.3% | -7.81 to 6.07 | EVEN, no difference beyond the noise |
| queries a second | 4,730 | 4,716 | -0.3% | -125 to 97.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.05 | 4.03 | -0.6% | -0.129 to 0.0804 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.54 | 5.5 | -0.6% | -0.177 to 0.11 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.15 | 3.14 | -0.2% | -0.0304 to 0.018 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 603 | +17.8% | -68.2 to 251 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 519 | +12.5% | -36 to 152 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,464 | 484,262 | -26.1% | -417,649 to 75,244 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.187 | -0.1% | -0.00824 to 0.00781 | EVEN, no difference beyond the noise |
| host CPU-seconds | 309 | 309 | -0.0% | -13.4 to 13.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.29 | 2.3 | +0.3% | -0.0378 to 0.0497 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18 |  | 8.06 to 27.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 192 | +0.4% | -2.87 to 4.39 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.3% | -3.33 to 2.28 | EVEN, no difference beyond the noise |
| queries a second | 3,938 | 3,928 | -0.3% | -66.6 to 45.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.17 | 8.7 | -5.1% | -2.28 to 1.34 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 14 | 13 | -7.4% | -4.94 to 2.86 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.79 | 5.35 | -7.7% | -2.26 to 1.38 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 658 | +28.5% | -178 to 470 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 556 | +20.3% | -105 to 293 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 618,056 | 434,535 | -29.7% | -602,232 to 235,191 | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.206 | -2.1% | -0.0204 to 0.0115 | EVEN, no difference beyond the noise |
| host CPU-seconds | 339 | 332 | -2.0% | -32.1 to 18.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.87 | 3.78 | -2.4% | -0.44 to 0.254 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 20 |  | 7.09 to 32.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,920 | 2,923 | +0.1% | -25.2 to 31.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,934 | 2,933 | -0.1% | -6.33 to 3.18 | EVEN, no difference beyond the noise |
| queries a second | 2,934 | 2,933 | -0.1% | -6.33 to 3.18 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.24 | 0.229 | -4.6% | -0.0694 to 0.0474 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.52 | 0.49 | -5.7% | -0.234 to 0.175 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.535 | 0.167 | -68.7% | -1.98 to 1.25 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 504 | -1.6% | -64.7 to 48 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 441 | -4.8% | -70.3 to 25.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,269 | 380,386 | +3.6% | -44,187 to 70,422 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.122 | -0.5% | -0.0202 to 0.0191 | EVEN, no difference beyond the noise |
| host CPU-seconds | 222 | 221 | -0.5% | -36.4 to 34.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.165 | 0.164 | -0.6% | -0.0288 to 0.0269 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | -1.84 to 23.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4.11 | 4.13 | +0.6% | -7.96 to 8.01 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 984 | -0.0% | -0.61 to 0.498 | EVEN, no difference beyond the noise |
| queries a second | 984 | 984 | -0.0% | -0.61 to 0.498 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.81 | 1.83 | +1.2% | -0.661 to 0.705 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.49 | 3.41 | -2.5% | -0.962 to 0.79 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 1.1 | -6.8% | -0.602 to 0.441 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 583 | +14.0% | -77.6 to 221 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 479 | +5.8% | -13.8 to 66 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,979 | 176,993 | -6.3% | -29,117 to 5,144 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.153 | +24.7% | -0.139 to 0.2 | EVEN, no difference beyond the noise |
| host CPU-seconds | 189 | 237 | +25.2% | -215 to 311 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 118 | 154 | +30.7% | -405 to 477 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19.7 |  | 5.98 to 33.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
