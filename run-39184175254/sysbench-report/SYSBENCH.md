# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | -0.0% | -4.23 to 4.05 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.1% | -4.38 to 3.86 | EVEN, no difference beyond the noise |
| queries a second | 4,704 | 4,700 | -0.1% | -70.1 to 61.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.31 | 5.15 | -3.0% | -0.293 to -0.0214 | GAIN |
| latency, 99th percentile (ms) | 7.43 | 7.34 | -1.2% | -0.279 to 0.102 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.39 | 3.34 | -1.5% | -0.0907 to -0.00799 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 511 | -0.1% | -87.6 to 86.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 436 | -2.5% | -133 to 111 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,724 | 241,683 | -1.2% | -52,565 to 46,484 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.195 | -0.9% | -0.00605 to 0.00251 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 108 | -0.8% | -3.56 to 1.74 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.43 | 2.41 | -0.8% | -0.0788 to 0.0402 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 0.427 to 13.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.0% | -4.25 to 4.03 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.0% | -4.09 to 3.94 | EVEN, no difference beyond the noise |
| queries a second | 4,723 | 4,721 | -0.0% | -65.5 to 63.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.1 | 4.05 | -1.2% | -0.153 to 0.056 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.64 | 5.5 | -2.4% | -0.278 to 0.0102 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.19 | 3.17 | -0.6% | -0.0407 to -1.65e-06 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 597 | +16.7% | -42.4 to 213 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 515 | +11.5% | -25 to 131 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,652 | 508,872 | -22.4% | -286,417 to -7,143 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.19 | -0.8% | -0.00307 to -9.43e-05 | GAIN |
| host CPU-seconds | 318 | 315 | -0.8% | -4.76 to -0.538 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.36 | 2.34 | -0.8% | -0.0369 to -0.000383 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 4.62 to 27.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194 | 193 | -0.2% | -1.77 to 1.15 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.2% | -2.13 to 2.94 | EVEN, no difference beyond the noise |
| queries a second | 3,949 | 3,957 | +0.2% | -42.6 to 58.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.1 | 6.6 | +8.1% | -0.594 to 1.58 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 18.2 | 17.1 | -5.7% | -10.8 to 8.75 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.72 | 3.23 | -13.1% | -2.73 to 1.75 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 525 | +2.5% | -133 to 159 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 472 | +2.3% | -105 to 126 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,118 | 602,326 | -2.2% | -307,214 to 279,630 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.133 | -0.5% | -0.0129 to 0.0116 | EVEN, no difference beyond the noise |
| host CPU-seconds | 239 | 238 | -0.5% | -22.8 to 20.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.71 | 2.7 | -0.3% | -0.238 to 0.22 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 6.08 to 18.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,942 | 2,942 | -0.0% | -11.6 to 10.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,952 | -0.0% | -8.24 to 6.29 | EVEN, no difference beyond the noise |
| queries a second | 2,953 | 2,952 | -0.0% | -8.24 to 6.29 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.328 | 0.324 | -1.2% | -0.0212 to 0.0132 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.524 | 0.517 | -1.3% | -0.021 to 0.00768 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.203 | 0.204 | +0.3% | -0.00598 to 0.00702 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 537 | +4.8% | -121 to 171 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 461 | -0.5% | -120 to 115 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,907 | 359,086 | -2.1% | -121,572 to 105,930 | shown, not judged |
| host CPU busy (share of the run) | 0.0983 | 0.0996 | +1.3% | -0.000633 to 0.00324 | EVEN, no difference beyond the noise |
| host CPU-seconds | 163 | 165 | +1.5% | -0.851 to 5.62 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.121 | 0.123 | +1.5% | -0.000252 to 0.00387 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 |  | 4.16 to 18.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0.0029 | 0.00218 | -25.0% | -0.012 to 0.0105 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 980 | 979 | -0.1% | -8.14 to 6.51 | EVEN, no difference beyond the noise |
| queries a second | 980 | 979 | -0.1% | -8.14 to 6.51 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.15 | 1.97 | -8.1% | -1.16 to 0.813 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.55 | 3.73 | -32.8% | -11.7 to 8.01 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.48 | 1.51 | +2.1% | -0.355 to 0.418 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 556 | +8.5% | -91.6 to 179 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 475 | +4.7% | -66.3 to 109 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 187,472 | 176,814 | -5.7% | -41,458 to 20,140 | shown, not judged |
| host CPU busy (share of the run) | 0.408 | 0.404 | -1.1% | -0.0279 to 0.0191 | EVEN, no difference beyond the noise |
| host CPU-seconds | 717 | 708 | -1.2% | -55.6 to 37.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 482,685 | 589,320 | +22.1% | -954,696 to 1,167,966 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | -2.31 to 35 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
