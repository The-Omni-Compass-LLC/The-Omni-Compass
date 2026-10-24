# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 291 | -1.2% | -6.62 to -0.283 | LOSS |
| throughput (transactions a second) | 295 | 292 | -1.2% | -6.9 to -0.0355 | LOSS |
| queries a second | 4,723 | 4,667 | -1.2% | -110 to -0.569 | LOSS |
| latency, 95th percentile (ms) | 4.88 | 4.88 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 6.63 | 6.55 | -1.2% | -0.424 to 0.264 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.26 | 3.29 | +0.7% | 0.00256 to 0.045 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 504 | -1.5% | -57.5 to 41.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 430 | -3.8% | -113 to 78.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,140 | 245,019 | +0.4% | -39,080 to 40,838 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.191 | +0.2% | -0.007 to 0.00769 | EVEN, no difference beyond the noise |
| host CPU-seconds | 105 | 105 | +0.4% | -3.83 to 4.66 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.36 | +1.6% | -0.034 to 0.106 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 1.03 to 11 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | +0.1% | -2.62 to 3.29 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.1% | -2.55 to 3.26 | EVEN, no difference beyond the noise |
| queries a second | 4,709 | 4,715 | +0.1% | -40.8 to 52.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.3 | 4.18 | -3.0% | -0.344 to 0.0903 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.02 | 5.95 | -1.2% | -0.482 to 0.34 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.27 | 3.22 | -1.5% | -0.123 to 0.0222 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 513 | +0.1% | -40.6 to 42.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 456 | -1.3% | -11.5 to -0.838 | GAIN |
| pages read from disk into the pool (misses) | 653,159 | 633,056 | -3.1% | -87,784 to 47,577 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.194 | -1.4% | -0.0126 to 0.00718 | EVEN, no difference beyond the noise |
| host CPU-seconds | 326 | 322 | -1.3% | -21.5 to 12.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.42 | 2.39 | -1.4% | -0.138 to 0.0687 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19 |  | 3.89 to 34.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | +0.1% | -1.66 to 2.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.1% | -1.44 to 1.08 | EVEN, no difference beyond the noise |
| queries a second | 3,945 | 3,941 | -0.1% | -28.8 to 21.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.33 | 8.03 | -3.5% | -1.26 to 0.671 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.3 | 12 | -2.3% | -1.95 to 1.37 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.3 | 5.21 | -1.6% | -0.331 to 0.158 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 579 | +13.1% | 32.4 to 101 | power given |
| pages holding data, mean (MB) | 462 | 508 | +9.9% | 4.69 to 86.7 | power given |
| pages read from disk into the pool (misses) | 617,647 | 522,957 | -15.3% | -105,547 to -83,833 | shown, not judged |
| host CPU busy (share of the run) | 0.217 | 0.211 | -2.8% | -0.0193 to 0.00712 | EVEN, no difference beyond the noise |
| host CPU-seconds | 349 | 340 | -2.8% | -31.7 to 12.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.95 | 3.84 | -2.9% | -0.401 to 0.173 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 |  | 10.3 to 26.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,960 | 2,960 | -0.0% | -10 to 9.83 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,964 | -0.0% | -7.09 to 5.57 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,964 | -0.0% | -7.09 to 5.57 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.196 | 0.186 | -5.4% | -0.0633 to 0.042 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.315 | 0.313 | -0.6% | -0.0546 to 0.0506 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.091 | 0.0901 | -0.9% | -0.0217 to 0.02 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 456 | -10.9% | -138 to 26.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 418 | -9.8% | -111 to 19.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,806 | 421,989 | +14.7% | -85,411 to 193,776 | shown, not judged |
| host CPU busy (share of the run) | 0.0682 | 0.0713 | +4.5% | -0.00113 to 0.00732 | EVEN, no difference beyond the noise |
| host CPU-seconds | 122 | 128 | +4.5% | -2.04 to 13.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0908 | 0.0949 | +4.5% | -0.00161 to 0.00982 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 2.55 to 17.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.05 | 2.52 | -17.2% | -3.08 to 2.03 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 980 | 980 | +0.0% | -1.8 to 1.85 | EVEN, no difference beyond the noise |
| queries a second | 980 | 980 | +0.0% | -1.8 to 1.85 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.82 | 1.75 | -3.8% | -0.706 to 0.568 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.21 | 3.85 | -8.8% | -1.09 to 0.347 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.14 | 1.12 | -1.7% | -0.16 to 0.122 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 401 | -21.7% | -152 to -69.6 | GAIN |
| pages holding data, mean (MB) | 452 | 336 | -25.8% | -171 to -62.9 | GAIN |
| pages read from disk into the pool (misses) | 189,065 | 274,799 | +45.3% | 53,982 to 117,486 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.16 | +0.6% | -0.0179 to 0.0197 | EVEN, no difference beyond the noise |
| host CPU-seconds | 284 | 285 | +0.5% | -31.9 to 35.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 241 | 263 | +9.3% | -279 to 324 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17.3 |  | 7.29 to 27.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
