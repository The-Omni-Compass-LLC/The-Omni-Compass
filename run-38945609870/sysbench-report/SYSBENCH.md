# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 294 | +0.6% | -1.55 to 4.83 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.4% | 0.219 to 1.97 | GAIN |
| queries a second | 4,699 | 4,717 | +0.4% | 3.51 to 31.5 | GAIN |
| latency, 95th percentile (ms) | 5.18 | 5.09 | -1.8% | -0.493 to 0.304 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.54 | 7.12 | -5.5% | -2.22 to 1.39 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.35 | 3.27 | -2.3% | -0.366 to 0.214 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 502 | -1.9% | -53.2 to 33.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 448 | 439 | -2.0% | -117 to 99.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,412 | 245,739 | +0.1% | -32,703 to 33,357 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.189 | +1.8% | -0.00176 to 0.00828 | EVEN, no difference beyond the noise |
| host CPU-seconds | 102 | 104 | +1.9% | -1.04 to 4.99 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.29 | 2.32 | +1.4% | -0.0107 to 0.0728 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.3% | -5.47 to 7.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.3% | -5.33 to 7.27 | EVEN, no difference beyond the noise |
| queries a second | 4,712 | 4,728 | +0.3% | -85.2 to 116 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.33 | 4.2 | -2.9% | -0.237 to -0.0187 | GAIN |
| latency, 99th percentile (ms) | 5.71 | 5.57 | -2.4% | -0.283 to 0.0114 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.34 | 3.27 | -2.1% | -0.213 to 0.0715 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 505 | -1.3% | -54.7 to 41.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 457 | -1.2% | -54.8 to 43.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 652,581 | 645,203 | -1.1% | -79,503 to 64,748 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.2 | -2.8% | -0.0171 to 0.00576 | EVEN, no difference beyond the noise |
| host CPU-seconds | 341 | 331 | -2.8% | -30.5 to 11.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.53 | 2.45 | -3.1% | -0.262 to 0.104 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14 |  | 5.39 to 22.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194 | 194 | -0.1% | -3.8 to 3.49 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | -0.1% | -3.71 to 3.25 | EVEN, no difference beyond the noise |
| queries a second | 3,906 | 3,901 | -0.1% | -74.3 to 65.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.63 | 7 | +5.5% | -0.437 to 1.17 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.1 | 10.1 | +0.0% | -0.457 to 0.457 | EVEN, the same |
| latency, mean (ms) | 3.87 | 3.91 | +0.9% | -0.278 to 0.349 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 433 | -15.5% | -118 to -39.9 | GAIN |
| pages holding data, mean (MB) | 460 | 389 | -15.4% | -86.8 to -55.1 | GAIN |
| pages read from disk into the pool (misses) | 615,649 | 839,244 | +36.3% | 160,195 to 286,995 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.17 | -0.5% | -0.00463 to 0.00281 | EVEN, no difference beyond the noise |
| host CPU-seconds | 311 | 309 | -0.4% | -7.93 to 5.18 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.48 | 3.46 | -0.4% | -0.11 to 0.0794 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 4.74 to 19.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,946 | 2,947 | +0.0% | -3.71 to 5.23 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,950 | 2,951 | +0.0% | -4.62 to 6.75 | EVEN, no difference beyond the noise |
| queries a second | 2,950 | 2,951 | +0.0% | -4.62 to 6.75 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.332 | 0.338 | +1.8% | -0.0334 to 0.0454 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.451 | 0.445 | -1.2% | -0.0554 to 0.0447 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.209 | +2.3% | -0.0158 to 0.025 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 483 | -5.7% | -112 to 53 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 428 | -7.7% | -137 to 65.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,574 | 410,943 | +12.1% | -141,547 to 230,284 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.107 | +4.1% | -0.0169 to 0.0253 | EVEN, no difference beyond the noise |
| host CPU-seconds | 171 | 178 | +4.3% | -28.7 to 43.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.127 | 0.132 | +4.2% | -0.0214 to 0.0321 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 3.49 to 17.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 118 | 119 | +0.9% | -76 to 78.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 986 | 984 | -0.2% | -9.25 to 6.02 | EVEN, no difference beyond the noise |
| queries a second | 986 | 984 | -0.2% | -9.25 to 6.02 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 166 | 170 | +2.7% | -61.9 to 70.7 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 668 | 866 | +29.7% | -1,304 to 1,701 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 36.1 | 42.2 | +16.8% | -1.89 to 14.1 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 470 | -8.2% | -132 to 48.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 396 | -12.8% | -141 to 25.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 190,457 | 226,509 | +18.9% | -24,828 to 96,932 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.137 | -0.1% | -0.0184 to 0.0181 | EVEN, no difference beyond the noise |
| host CPU-seconds | 243 | 243 | -0.2% | -33.9 to 33 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.85 | 4.5 | -7.3% | -4.73 to 4.02 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 |  | 12.4 to 24.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
