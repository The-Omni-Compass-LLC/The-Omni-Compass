# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | +0.1% | -1.36 to 1.89 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.1% | -1.88 to 2.28 | EVEN, no difference beyond the noise |
| queries a second | 4,706 | 4,709 | +0.1% | -30 to 36.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.94 | 4.85 | -1.8% | -0.306 to 0.131 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.79 | 6.63 | -2.4% | -0.331 to 0.01 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.22 | 3.23 | +0.2% | -0.0283 to 0.0413 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 499 | -2.5% | -14.3 to -11.8 | GAIN |
| pages holding data, mean (MB) | 448 | 438 | -2.1% | -15 to -3.93 | GAIN |
| pages read from disk into the pool (misses) | 245,398 | 232,203 | -5.4% | -13,731 to -12,660 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.19 | +2.6% | -0.0023 to 0.012 | EVEN, no difference beyond the noise |
| host CPU-seconds | 102 | 105 | +3.0% | -1.4 to 7.43 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.27 | 2.33 | +2.8% | -0.0132 to 0.138 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.1% | -1.84 to 2.28 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.1% | -1.97 to 2.3 | EVEN, no difference beyond the noise |
| queries a second | 4,715 | 4,718 | +0.1% | -31.5 to 36.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.25 | 4.18 | -1.8% | -0.266 to 0.114 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.64 | -3.0% | -0.319 to -0.0238 | GAIN |
| latency, mean (ms) | 3.28 | 3.25 | -0.6% | -0.0625 to 0.0202 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 542 | +5.9% | -92.9 to 154 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 492 | +6.4% | -98 to 158 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,058 | 546,637 | -16.6% | -399,845 to 183,002 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.2 | -0.1% | -0.00689 to 0.00635 | EVEN, no difference beyond the noise |
| host CPU-seconds | 332 | 332 | -0.1% | -11.4 to 11.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.46 | 2.46 | -0.1% | -0.0678 to 0.0619 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | 8.16 to 18.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 192 | +0.7% | -0.828 to 3.42 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.0% | -0.838 to 0.769 | EVEN, no difference beyond the noise |
| queries a second | 3,927 | 3,926 | -0.0% | -16.8 to 15.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.28 | 8.74 | -5.8% | -1.15 to 0.0691 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.9 | 12.9 | -6.9% | -2.17 to 0.241 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.61 | 5.47 | -2.4% | -0.454 to 0.179 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 630 | +23.1% | 79.7 to 156 | power given |
| pages holding data, mean (MB) | 463 | 555 | +19.9% | 67.8 to 117 | power given |
| pages read from disk into the pool (misses) | 613,351 | 430,126 | -29.9% | -274,578 to -91,873 | shown, not judged |
| host CPU busy (share of the run) | 0.218 | 0.212 | -2.7% | -0.0159 to 0.00399 | EVEN, no difference beyond the noise |
| host CPU-seconds | 351 | 342 | -2.7% | -25.3 to 6.17 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.03 | 3.89 | -3.4% | -0.337 to 0.066 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 |  | 13.5 to 23.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,947 | 2,950 | +0.1% | -1.99 to 6.82 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,956 | +0.1% | -0.653 to 6 | EVEN, no difference beyond the noise |
| queries a second | 2,953 | 2,956 | +0.1% | -0.653 to 6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.32 | 0.318 | -0.6% | -0.0106 to 0.00661 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.451 | -1.2% | -0.0168 to 0.00614 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.2 | +0.9% | -0.0027 to 0.00613 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 566 | +10.6% | -99.5 to 208 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 489 | +5.3% | -68.6 to 118 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,544 | 325,093 | -11.5% | -162,746 to 77,845 | shown, not judged |
| host CPU busy (share of the run) | 0.0975 | 0.0993 | +1.9% | -0.00288 to 0.00666 | EVEN, no difference beyond the noise |
| host CPU-seconds | 162 | 165 | +2.0% | -4.79 to 11.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.12 | 0.122 | +1.9% | -0.00382 to 0.00849 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.7 |  | -4.78 to 30.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 5.48 | 5.29 | -3.5% | -1.75 to 1.36 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 982 | 984 | +0.3% | -2.87 to 7.93 | EVEN, no difference beyond the noise |
| queries a second | 982 | 984 | +0.3% | -2.87 to 7.93 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.94 | 1.9 | -2.0% | -0.364 to 0.286 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.8 | 4.77 | -0.6% | -0.363 to 0.303 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.16 | 1.15 | -1.1% | -0.102 to 0.0762 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 454 | 451 | -0.7% | -15.1 to 9.09 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,178 | 186,783 | -1.3% | -10,789 to 6,000 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.114 | -4.1% | -0.0337 to 0.0239 | EVEN, no difference beyond the noise |
| host CPU-seconds | 184 | 176 | -4.1% | -51.1 to 36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 76.8 | 73.4 | -4.4% | -48.8 to 42.1 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
