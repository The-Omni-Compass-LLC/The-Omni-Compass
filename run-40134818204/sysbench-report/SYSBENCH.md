# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `7743f2e82851`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | -0.1% | -5.46 to 5.14 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.0% | -4.9 to 4.91 | EVEN, no difference beyond the noise |
| queries a second | 4,691 | 4,691 | +0.0% | -78.4 to 78.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.18 | 5.18 | +0.0% | -0.231 to 0.231 | EVEN, the same |
| latency, 99th percentile (ms) | 7.17 | 7.26 | +1.2% | -0.295 to 0.474 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.31 | 3.31 | -0.0% | -0.0677 to 0.067 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 528 | +3.2% | -53.9 to 86.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 448 | 445 | -0.6% | -103 to 97.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,350 | 233,036 | -4.6% | -73,532 to 50,904 | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.193 | +2.1% | -0.0064 to 0.0142 | EVEN, no difference beyond the noise |
| host CPU-seconds | 104 | 107 | +2.4% | -3.34 to 8.34 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.39 | +2.3% | -0.0344 to 0.142 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `7743f2e82851`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.0% | -3.72 to 3.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.0% | -3.71 to 3.81 | EVEN, no difference beyond the noise |
| queries a second | 4,726 | 4,727 | +0.0% | -59.3 to 60.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.13 | 4.05 | -1.8% | -0.0765 to -0.0708 | GAIN |
| latency, 99th percentile (ms) | 5.67 | 5.64 | -0.6% | -0.179 to 0.111 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.19 | 3.16 | -1.1% | -0.0978 to 0.0289 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 581 | +13.5% | -94.1 to 233 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 501 | +8.4% | -57.8 to 135 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,391 | 546,293 | -16.4% | -399,438 to 185,243 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.188 | -1.0% | -0.0113 to 0.00755 | EVEN, no difference beyond the noise |
| host CPU-seconds | 314 | 311 | -0.9% | -18.8 to 12.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.31 | -1.0% | -0.112 to 0.0676 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18 |  | 11.4 to 24.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `7743f2e82851`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 192 | +0.4% | -1.69 to 3.04 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 197 | +0.0% | -2.32 to 2.46 | EVEN, no difference beyond the noise |
| queries a second | 3,930 | 3,931 | +0.0% | -46.5 to 49.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.74 | 8.43 | -3.5% | -0.69 to 0.0725 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.1 | 12.6 | -4.1% | -1.74 to 0.663 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.34 | 5.32 | -0.3% | -0.169 to 0.136 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 654 | +27.8% | 37.4 to 247 | power given |
| pages holding data, mean (MB) | 462 | 557 | +20.7% | 8.24 to 183 | power given |
| pages read from disk into the pool (misses) | 615,056 | 436,215 | -29.1% | -351,621 to -6,061 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.21 | +0.7% | -0.00511 to 0.00822 | EVEN, no difference beyond the noise |
| host CPU-seconds | 335 | 338 | +0.9% | -7.16 to 13.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.82 | 3.84 | +0.5% | -0.102 to 0.143 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 23 |  | 18.7 to 27.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `7743f2e82851`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,956 | 2,958 | +0.1% | -9.02 to 12.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,964 | -0.0% | -6.33 to 3.8 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,964 | -0.0% | -6.33 to 3.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.209 | 0.203 | -2.9% | -0.0198 to 0.00783 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.354 | 0.346 | -2.4% | -0.0184 to 0.00171 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.271 | 0.173 | -36.3% | -0.445 to 0.248 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 409 | -20.2% | -214 to 7.33 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 374 | -19.3% | -181 to 2.29 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,147 | 495,478 | +34.6% | -37,240 to 291,902 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.11 | -1.3% | -0.00812 to 0.00515 | EVEN, no difference beyond the noise |
| host CPU-seconds | 199 | 196 | -1.3% | -14.5 to 9.21 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.148 | 0.146 | -1.4% | -0.0109 to 0.00674 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | -1.4 to 10.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `7743f2e82851`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4.91 | 3.84 | -21.7% | -8.69 to 6.56 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 984 | -0.0% | -5.72 to 5.11 | EVEN, no difference beyond the noise |
| queries a second | 984 | 984 | -0.0% | -5.72 to 5.11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.84 | 1.99 | +8.0% | -0.572 to 0.868 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.86 | 4.21 | +9.0% | -0.852 to 1.54 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.11 | 1.15 | +3.6% | -0.161 to 0.242 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 565 | +10.3% | -63.9 to 169 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 464 | +2.3% | -43.9 to 65.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,569 | 187,818 | -0.4% | -30,960 to 29,459 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.171 | +39.3% | -0.103 to 0.2 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 265 | +39.8% | -160 to 311 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 98.5 | 166 | +68.3% | -130 to 265 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 22.7 |  | 8.98 to 36.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
