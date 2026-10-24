# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 292 | +0.2% | -5.66 to 6.72 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 294 | +0.5% | -1.47 to 4.4 | EVEN, no difference beyond the noise |
| queries a second | 4,677 | 4,701 | +0.5% | -23.6 to 70.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.15 | 5.34 | +3.7% | -0.289 to 0.672 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.21 | 7.78 | +7.9% | -1.6 to 2.73 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.31 | 3.46 | +4.5% | -0.361 to 0.659 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 474 | -7.5% | -174 to 96.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 405 | -9.8% | -157 to 69.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 242,140 | 257,686 | +6.4% | -50,636 to 81,727 | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.192 | +2.0% | -0.00106 to 0.00869 | EVEN, no difference beyond the noise |
| host CPU-seconds | 104 | 106 | +2.2% | -0.6 to 5.22 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.38 | +2.0% | -0.0143 to 0.11 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 2.03 to 12 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.2% | -2.97 to 2.04 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.1% | -2.94 to 2.11 | EVEN, no difference beyond the noise |
| queries a second | 4,722 | 4,716 | -0.1% | -47.1 to 33.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.08 | 4 | -1.8% | -0.253 to 0.107 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.47 | 5.34 | -2.4% | -0.41 to 0.15 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.18 | 3.15 | -0.8% | -0.0851 to 0.0324 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 599 | +17.0% | -49.8 to 224 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 518 | +12.3% | -32.3 to 146 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,702 | 493,630 | -24.6% | -459,021 to 136,875 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.189 | -0.7% | -0.00667 to 0.00388 | EVEN, no difference beyond the noise |
| host CPU-seconds | 314 | 312 | -0.7% | -11.6 to 7.23 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.32 | -0.6% | -0.0951 to 0.0694 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19 |  | 12.4 to 25.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 189 | 192 | +1.4% | 2.28 to 3.17 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.6% | -0.519 to 2.83 | EVEN, no difference beyond the noise |
| queries a second | 3,920 | 3,943 | +0.6% | -10.4 to 56.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.62 | 9.01 | -6.4% | -1.07 to -0.159 | GAIN |
| latency, 99th percentile (ms) | 15 | 13.6 | -9.0% | -3.1 to 0.397 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.01 | 5.57 | -7.2% | -0.782 to -0.0877 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 617 | +20.5% | 40.8 to 170 | power given |
| pages holding data, mean (MB) | 462 | 536 | +16.1% | 16.5 to 132 | power given |
| pages read from disk into the pool (misses) | 616,535 | 466,122 | -24.4% | -222,196 to -78,630 | shown, not judged |
| host CPU busy (share of the run) | 0.225 | 0.219 | -2.7% | -0.0117 to -0.000647 | GAIN |
| host CPU-seconds | 362 | 352 | -2.7% | -20.1 to 0.387 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.18 | 4.01 | -4.1% | -0.293 to -0.0501 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 19.3 |  | 14.2 to 24.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,942 | 2,939 | -0.1% | -10.6 to 3.81 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,943 | 2,941 | -0.1% | -9.28 to 3.43 | EVEN, no difference beyond the noise |
| queries a second | 2,943 | 2,941 | -0.1% | -9.28 to 3.43 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.173 | 0.164 | -5.4% | -0.0181 to -0.000609 | GAIN |
| latency, 99th percentile (ms) | 0.361 | 0.346 | -4.1% | -0.0402 to 0.0108 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.113 | 0.117 | +4.2% | -0.0123 to 0.0218 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 418 | -18.4% | -171 to -16.9 | GAIN |
| pages holding data, mean (MB) | 464 | 384 | -17.2% | -159 to -0.265 | GAIN |
| pages read from disk into the pool (misses) | 368,588 | 473,304 | +28.4% | 8,633 to 200,799 | shown, not judged |
| host CPU busy (share of the run) | 0.0922 | 0.0923 | +0.0% | -0.00311 to 0.00319 | EVEN, no difference beyond the noise |
| host CPU-seconds | 167 | 167 | +0.0% | -5.48 to 5.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.124 | 0.124 | +0.2% | -0.00418 to 0.00456 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | -1.74 to 17.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0.000724 | 0 | -100.0% | -0.00384 to 0.00239 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 978 | 978 | +0.0% | -3.47 to 4.19 | EVEN, no difference beyond the noise |
| queries a second | 978 | 978 | +0.0% | -3.47 to 4.19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.05 | 2.03 | -0.7% | -0.314 to 0.285 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.29 | 3.33 | +1.4% | -1.18 to 1.27 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.41 | 1.38 | -1.9% | -0.213 to 0.159 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 555 | +8.3% | -71.2 to 156 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 458 | +0.9% | -84.2 to 92.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,700 | 187,033 | -1.4% | -70,634 to 65,301 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.208 | -0.5% | -0.0202 to 0.0181 | EVEN, no difference beyond the noise |
| host CPU-seconds | 373 | 371 | -0.5% | -35.9 to 32 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 373,167 | 371,203 | -0.5% | -35,916 to 31,989 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
