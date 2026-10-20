# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 291 | -0.5% | -20 to 16.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.2% | -13.6 to 12.4 | EVEN, no difference beyond the noise |
| queries a second | 4,718 | 4,709 | -0.2% | -218 to 198 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.52 | 4.46 | -1.3% | -0.782 to 0.663 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.88 | 21.4 | +140.9% | -51.7 to 76.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.95 | 3.4 | +15.1% | -1.5 to 2.39 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.7% | -0.692 to 20.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 135 | +12.1% | -5.62 to 34.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 577,964 | 557,367 | -3.6% | -61,191 to 19,998 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.204 | -1.9% | -0.0052 to -0.00278 | GAIN |
| host CPU-seconds | 124 | 122 | -1.9% | -2.76 to -1.97 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.78 | 2.74 | -1.4% | -0.2 to 0.123 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.2% | -1.5 to 0.526 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.1% | -1.66 to 0.773 | EVEN, no difference beyond the noise |
| queries a second | 4,720 | 4,713 | -0.1% | -26.5 to 12.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4 | 3.84 | -4.1% | -0.266 to -0.0638 | GAIN |
| latency, 99th percentile (ms) | 5.54 | 5.44 | -1.8% | -0.35 to 0.149 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.06 | 2.97 | -3.1% | -0.129 to -0.0585 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 137 | +7.0% | 5.73 to 12.2 | power given |
| pages holding data, mean (MB) | 120 | 135 | +12.7% | 11.9 to 18.6 | power given |
| pages read from disk into the pool (misses) | 1,971,673 | 1,901,083 | -3.6% | -128,365 to -12,816 | shown, not judged |
| host CPU busy (share of the run) | 0.239 | 0.232 | -2.9% | -0.00959 to -0.00432 | GAIN |
| host CPU-seconds | 425 | 413 | -2.9% | -16.8 to -7.68 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.16 | 3.07 | -2.7% | -0.13 to -0.0401 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194 | 195 | +0.7% | -0.283 to 2.81 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.1% | -2.26 to 1.71 | EVEN, no difference beyond the noise |
| queries a second | 3,947 | 3,942 | -0.1% | -45.2 to 34.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.33 | 5.84 | -7.7% | -1.69 to 0.718 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 18.3 | 10.8 | -41.0% | -26.5 to 11.5 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.03 | 2.85 | -6.1% | -0.469 to 0.1 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 132 | +3.3% | -8.85 to 17.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 122 | 126 | +3.1% | -11.1 to 18.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,664,805 | 1,632,169 | -2.0% | -92,662 to 27,390 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.127 | -0.3% | -0.00526 to 0.00453 | EVEN, no difference beyond the noise |
| host CPU-seconds | 227 | 226 | -0.3% | -9.13 to 7.98 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.57 | 2.54 | -0.9% | -0.137 to 0.0898 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | -7.01 to 13.7 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,944 | 2,944 | -0.0% | -6.83 to 6.03 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,953 | +0.0% | -4.01 to 5.1 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,953 | +0.0% | -4.01 to 5.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.344 | 0.342 | -0.6% | -0.0192 to 0.0152 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.464 | +1.8% | -0.0327 to 0.0493 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.209 | +0.3% | -0.011 to 0.0121 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 140 | +9.4% | -3.21 to 27.2 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 136 | +12.0% | 0.871 to 28.2 | power given |
| pages read from disk into the pool (misses) | 1,029,160 | 993,739 | -3.4% | -85,161 to 14,319 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.111 | +0.3% | -0.00725 to 0.00793 | EVEN, no difference beyond the noise |
| host CPU-seconds | 185 | 185 | +0.2% | -12.3 to 13.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.137 | 0.138 | +0.3% | -0.00937 to 0.0101 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 1.03 to 11 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.62 | 4.09 | -38.2% | -5.58 to 0.523 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 985 | 983 | -0.1% | -2.6 to 0.311 | EVEN, no difference beyond the noise |
| queries a second | 985 | 983 | -0.1% | -2.6 to 0.311 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.22 | 2.53 | +13.8% | -0.0943 to 0.707 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.87 | 4.79 | +23.8% | -1.17 to 3.02 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.29 | 1.45 | +12.4% | -0.487 to 0.806 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.5% | 3.03 to 16.2 | power given |
| pages holding data, mean (MB) | 117 | 124 | +5.9% | 5.41 to 8.34 | power given |
| pages read from disk into the pool (misses) | 416,363 | 410,622 | -1.4% | -18,411 to 6,928 | shown, not judged |
| host CPU busy (share of the run) | 0.257 | 0.288 | +11.9% | -0.0333 to 0.0946 | EVEN, no difference beyond the noise |
| host CPU-seconds | 452 | 505 | +11.8% | -58.3 to 165 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 159 | 310 | +95.1% | -112 to 414 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
