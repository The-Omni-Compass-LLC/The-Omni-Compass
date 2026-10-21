# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 289 | 290 | +0.4% | -2.56 to 5.06 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.3% | -3.99 to 5.96 | EVEN, no difference beyond the noise |
| queries a second | 4,691 | 4,706 | +0.3% | -63.9 to 95.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.02 | 5.88 | -2.4% | -0.557 to 0.269 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.79 | 8.69 | -1.2% | -0.33 to 0.121 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.46 | 3.46 | +0.1% | -0.0668 to 0.0719 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 495 | -3.4% | -53.8 to 18.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 416 | -7.1% | -109 to 45.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,651 | 248,254 | +1.9% | -22,098 to 31,304 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.198 | +2.6% | -0.00508 to 0.0152 | EVEN, no difference beyond the noise |
| host CPU-seconds | 107 | 110 | +2.7% | -2.83 to 8.61 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.41 | 2.46 | +2.4% | -0.0392 to 0.154 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | 3.87 to 11.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.1% | -1.65 to 2.27 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.1% | -1.64 to 2.22 | EVEN, no difference beyond the noise |
| queries a second | 4,724 | 4,728 | +0.1% | -26.3 to 35.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.33 | 4.25 | -1.8% | -0.27 to 0.115 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.32 | 6.28 | -0.6% | -0.203 to 0.127 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.27 | 3.21 | -1.6% | -0.136 to 0.031 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 500 | -2.3% | -29.6 to 6.46 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 452 | -2.1% | -31.2 to 11.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,799 | 662,501 | +1.0% | -48,162 to 61,565 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.191 | -2.1% | -0.0134 to 0.00532 | EVEN, no difference beyond the noise |
| host CPU-seconds | 323 | 317 | -2.1% | -22.2 to 8.95 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.4 | 2.35 | -2.1% | -0.151 to 0.0484 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 |  | 9.08 to 24.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 196 | 196 | -0.3% | -0.994 to -0.0284 | LOSS |
| throughput (transactions a second) | 197 | 197 | -0.1% | -0.989 to 0.545 | EVEN, no difference beyond the noise |
| queries a second | 3,947 | 3,942 | -0.1% | -19.8 to 10.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.47 | 5.74 | +4.9% | 0.103 to 0.438 | LOSS |
| latency, 99th percentile (ms) | 9.06 | 9.57 | +5.6% | -0.249 to 1.27 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3 | 3.1 | +3.3% | -0.113 to 0.313 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 471 | -7.9% | -195 to 113 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 426 | -7.7% | -172 to 101 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,443 | 736,920 | +19.7% | -352,808 to 595,762 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.145 | +0.3% | -0.00922 to 0.0101 | EVEN, no difference beyond the noise |
| host CPU-seconds | 257 | 257 | +0.3% | -16.5 to 18.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.87 | 2.88 | +0.6% | -0.178 to 0.213 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 12.5 to 20.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,940 | 2,943 | +0.1% | -14 to 21.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,954 | +0.1% | -12.8 to 16 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,954 | +0.1% | -12.8 to 16 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.357 | 0.334 | -6.4% | -0.0307 to -0.0147 | GAIN |
| latency, 99th percentile (ms) | 0.505 | 0.479 | -5.2% | -0.0475 to -0.0052 | GAIN |
| latency, mean (ms) | 0.216 | 0.207 | -3.9% | -0.0141 to -0.00284 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 453 | -11.5% | -261 to 143 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 407 | -12.2% | -233 to 121 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,211 | 437,277 | +18.8% | -208,218 to 346,350 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.164 | -4.7% | -0.0165 to 0.000279 | EVEN, no difference beyond the noise |
| host CPU-seconds | 303 | 289 | -4.7% | -29.2 to 0.528 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.226 | 0.215 | -4.8% | -0.0207 to -0.00113 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | 4.43 to 17.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| throughput (transactions a second) | 977 | 977 | +0.0% | -6.87 to 7.01 | EVEN, no difference beyond the noise |
| queries a second | 977 | 977 | +0.0% | -6.87 to 7.01 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.11 | 2.03 | -3.8% | -0.562 to 0.403 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.07 | 3.67 | -9.8% | -2.69 to 1.89 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.43 | 1.4 | -1.9% | -0.145 to 0.0917 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 510 | -0.5% | -21.7 to 17.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 432 | -4.8% | -57.1 to 13.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,716 | 198,802 | +4.8% | -11,669 to 29,841 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.204 | -1.9% | -0.0263 to 0.0184 | EVEN, no difference beyond the noise |
| host CPU-seconds | 371 | 364 | -1.9% | -45.7 to 31.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 371,193 | 364,180 | -1.9% | -45,729 to 31,703 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 20.7 |  | 13.1 to 28.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
