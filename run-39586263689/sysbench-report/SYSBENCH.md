# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 294 | +0.8% | -3.03 to 7.48 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 295 | +0.8% | -2.12 to 6.74 | EVEN, no difference beyond the noise |
| queries a second | 4,686 | 4,723 | +0.8% | -33.9 to 108 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.18 | 5.22 | +0.6% | -0.32 to 0.381 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.39 | 7.48 | +1.2% | -0.685 to 0.857 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.29 | 3.29 | +0.1% | -0.0182 to 0.0254 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 482 | -5.9% | -77.7 to 17.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 446 | 414 | -7.2% | -101 to 37.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,113 | 250,591 | +2.2% | -26,084 to 37,040 | shown, not judged |
| host CPU busy (share of the run) | 0.252 | 0.254 | +0.8% | 0.00136 to 0.0026 | power given |
| host CPU-seconds | 150 | 151 | +0.6% | -0.345 to 2.21 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.36 | 3.36 | -0.0% | -0.0656 to 0.0639 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 2.7 to 11.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.1% | -1.61 to 2.36 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -1.7 to 2.51 | EVEN, no difference beyond the noise |
| queries a second | 4,721 | 4,727 | +0.1% | -27.2 to 40.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.98 | 3.89 | -2.4% | -0.297 to 0.109 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.44 | 5.25 | -3.5% | -0.603 to 0.22 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.01 | 3 | -0.3% | -0.0744 to 0.0538 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 489 | -4.4% | -37.5 to -7.62 | GAIN |
| pages holding data, mean (MB) | 462 | 436 | -5.5% | -61.8 to 11 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,935 | 700,700 | +7.2% | -53,542 to 147,071 | shown, not judged |
| host CPU busy (share of the run) | 0.239 | 0.238 | -0.2% | -0.00833 to 0.00749 | EVEN, no difference beyond the noise |
| host CPU-seconds | 424 | 423 | -0.2% | -14.8 to 13.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.15 | 3.13 | -0.3% | -0.0945 to 0.0732 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 10.9 to 18.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 192 | +1.1% | -3.06 to 7.09 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 197 | +0.4% | -0.275 to 1.81 | EVEN, no difference beyond the noise |
| queries a second | 3,929 | 3,945 | +0.4% | -5.51 to 36.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.35 | 8.75 | -6.5% | -3 to 1.79 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.9 | 13.2 | -4.9% | -4.86 to 3.5 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.55 | 5.39 | -2.9% | -1.18 to 0.858 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 554 | +8.2% | -52.4 to 136 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 495 | +7.5% | -45.4 to 114 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,311 | 539,670 | -12.3% | -261,326 to 110,044 | shown, not judged |
| host CPU busy (share of the run) | 0.29 | 0.284 | -2.1% | -0.047 to 0.0351 | EVEN, no difference beyond the noise |
| host CPU-seconds | 511 | 500 | -2.1% | -82.6 to 61.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.86 | 5.68 | -3.1% | -1.16 to 0.798 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 |  | 7.46 to 29.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,959 | 2,961 | +0.1% | -5.28 to 10.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,966 | +0.0% | -6.13 to 7.06 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,966 | +0.0% | -6.13 to 7.06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.206 | 0.162 | -21.2% | -0.183 to 0.0956 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.348 | 0.302 | -13.3% | -0.165 to 0.0719 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.105 | 0.0854 | -18.4% | -0.0338 to -0.00462 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 390 | -23.8% | -369 to 126 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 350 | -24.6% | -339 to 112 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,870 | 542,773 | +47.5% | -192,449 to 542,257 | shown, not judged |
| host CPU busy (share of the run) | 0.08 | 0.0653 | -18.3% | -0.0222 to -0.00712 | GAIN |
| host CPU-seconds | 143 | 117 | -18.2% | -39.3 to -12.6 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 0.106 | 0.0865 | -18.3% | -0.0291 to -0.00963 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | -2.83 to 18.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| throughput (transactions a second) | 976 | 978 | +0.2% | -4.52 to 7.92 | EVEN, no difference beyond the noise |
| queries a second | 976 | 978 | +0.2% | -4.52 to 7.92 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.96 | 2.02 | +3.1% | 0.00258 to 0.118 | LOSS |
| latency, 99th percentile (ms) | 5.45 | 111 | +1936.3% | -322 to 534 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.88 | 3.92 | +35.9% | -2.24 to 4.31 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 477 | -6.8% | -74.3 to 4.29 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 415 | -8.6% | -61 to -16.8 | GAIN |
| pages read from disk into the pool (misses) | 188,848 | 211,071 | +11.8% | 469 to 43,976 | shown, not judged |
| host CPU busy (share of the run) | 0.243 | 0.244 | +0.4% | -0.0229 to 0.0248 | EVEN, no difference beyond the noise |
| host CPU-seconds | 451 | 453 | +0.4% | -44.5 to 48.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 450,727 | 452,620 | +0.4% | -44,494 to 48,281 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 10.6 to 22.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
