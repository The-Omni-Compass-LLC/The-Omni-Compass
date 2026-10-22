# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.3% | -3.92 to 1.98 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.4% | -3.97 to 1.56 | EVEN, no difference beyond the noise |
| queries a second | 4,716 | 4,696 | -0.4% | -63.5 to 25 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.99 | 2.97 | -0.6% | -0.681 to 0.645 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.65 | 4.68 | +0.7% | -0.596 to 0.657 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.41 | 1.4 | -0.6% | -0.153 to 0.135 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 369 | -28.0% | -401 to 114 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 320 | -28.4% | -334 to 80.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,749 | 293,337 | +19.4% | -86,668 to 181,844 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.101 | +0.5% | -0.00901 to 0.0101 | EVEN, no difference beyond the noise |
| host CPU-seconds | 60.4 | 60.8 | +0.5% | -5.4 to 6.01 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.35 | 1.36 | +0.9% | -0.129 to 0.152 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | -3.87 to 18.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.0% | -3.09 to 3.19 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.0% | -2.7 to 2.53 | EVEN, no difference beyond the noise |
| queries a second | 4,725 | 4,723 | -0.0% | -43.1 to 40.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.71 | 3.55 | -4.1% | -0.271 to -0.0368 | GAIN |
| latency, 99th percentile (ms) | 5.25 | 4.88 | -7.0% | -0.804 to 0.0669 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.8 | 2.74 | -2.1% | -0.144 to 0.029 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 496 | -3.1% | -76.6 to 45.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 451 | -2.4% | -67.8 to 45.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 656,123 | 652,963 | -0.5% | -76,234 to 69,915 | shown, not judged |
| host CPU busy (share of the run) | 0.219 | 0.215 | -1.9% | -0.00916 to 0.000869 | EVEN, no difference beyond the noise |
| host CPU-seconds | 392 | 384 | -1.9% | -16.3 to 1.52 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.9 | 2.85 | -1.9% | -0.15 to 0.0398 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 14.9 to 17.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 157 | 148 | -5.7% | -16.6 to -1.49 | LOSS |
| throughput (transactions a second) | 197 | 197 | +0.2% | -1.99 to 2.89 | EVEN, no difference beyond the noise |
| queries a second | 3,936 | 3,945 | +0.2% | -39.8 to 57.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 104 | 134 | +28.8% | 19 to 41.1 | LOSS |
| latency, 99th percentile (ms) | 267 | 316 | +18.6% | -84.7 to 184 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 20.1 | 25.8 | +28.5% | 1.56 to 9.9 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 513 | +0.3% | -131 to 134 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 461 | +0.0% | -116 to 116 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,332 | 610,100 | -1.0% | -193,241 to 180,777 | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.215 | -2.6% | -0.0134 to 0.0019 | EVEN, no difference beyond the noise |
| host CPU-seconds | 392 | 382 | -2.4% | -24 to 5.36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.45 | 5.65 | +3.6% | -0.239 to 0.63 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19 |  | 9.06 to 28.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,939 | 2,937 | -0.0% | -7.48 to 4.93 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,940 | 2,940 | -0.0% | -6.66 to 6.15 | EVEN, no difference beyond the noise |
| queries a second | 2,940 | 2,940 | -0.0% | -6.66 to 6.15 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.267 | 0.252 | -5.9% | -0.0401 to 0.00872 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.414 | 0.407 | -1.9% | -0.0263 to 0.011 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.17 | 0.174 | +2.0% | -0.000854 to 0.0076 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 447 | -12.7% | -176 to 46.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 407 | -12.4% | -180 to 65.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,053 | 434,236 | +18.6% | -83,573 to 219,941 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.147 | +0.4% | -0.00299 to 0.00429 | EVEN, no difference beyond the noise |
| host CPU-seconds | 264 | 265 | +0.5% | -5.27 to 7.78 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.196 | 0.197 | +0.5% | -0.00386 to 0.00587 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | 3.55 to 18.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 24.5 | 26.2 | +7.2% | -9.05 to 12.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 985 | 984 | -0.0% | -5.8 to 5.04 | EVEN, no difference beyond the noise |
| queries a second | 985 | 984 | -0.0% | -5.8 to 5.04 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.57 | 1.54 | -2.0% | -0.225 to 0.163 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.95 | 2.99 | +1.5% | -1.13 to 1.22 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.15 | 1.13 | -2.0% | -0.644 to 0.599 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 485 | -5.3% | -69.8 to 15.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 452 | 408 | -9.8% | -101 to 11.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,942 | 215,288 | +13.3% | -14,135 to 64,826 | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.217 | -1.8% | -0.0344 to 0.0266 | EVEN, no difference beyond the noise |
| host CPU-seconds | 387 | 380 | -1.8% | -60.3 to 46.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 36.4 | 32.1 | -11.7% | -26.5 to 18 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
