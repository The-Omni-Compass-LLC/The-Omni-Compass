# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.3% | -2.6 to 4.55 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.3% | -2.33 to 4.22 | EVEN, no difference beyond the noise |
| queries a second | 4,686 | 4,701 | +0.3% | -37.3 to 67.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.06 | 5 | -1.2% | -0.191 to 0.0699 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.79 | 6.71 | -1.2% | -0.543 to 0.38 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.32 | 3.29 | -1.1% | -0.0727 to -4.79e-05 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.4% | 1.63 to 19.8 | power given |
| pages holding data, mean (MB) | 120 | 136 | +13.4% | 14.8 to 17.4 | power given |
| pages read from disk into the pool (misses) | 576,209 | 548,696 | -4.8% | -70,560 to 15,534 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.194 | -1.0% | -0.0107 to 0.00655 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 107 | -1.2% | -6.15 to 3.63 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.43 | 2.39 | -1.5% | -0.121 to 0.0488 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | -0.1% | -3.69 to 2.91 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.1% | -3.68 to 2.89 | EVEN, no difference beyond the noise |
| queries a second | 4,707 | 4,701 | -0.1% | -58.8 to 46.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.06 | 2.97 | -3.0% | -0.297 to 0.117 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.05 | 3.98 | -1.8% | -0.0778 to -0.0675 | GAIN |
| latency, mean (ms) | 2.38 | 2.31 | -2.7% | -0.213 to 0.0868 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.8% | 7.03 to 7.8 | power given |
| pages holding data, mean (MB) | 120 | 135 | +12.0% | 12.3 to 16.6 | power given |
| pages read from disk into the pool (misses) | 1,984,537 | 1,936,544 | -2.4% | -192,501 to 96,517 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.186 | -2.6% | -0.0169 to 0.00711 | EVEN, no difference beyond the noise |
| host CPU-seconds | 346 | 338 | -2.5% | -30.1 to 12.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.56 | 2.5 | -2.4% | -0.22 to 0.0971 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 185 | 184 | -0.4% | -4.23 to 2.73 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.1% | -3.34 to 3.06 | EVEN, no difference beyond the noise |
| queries a second | 3,931 | 3,928 | -0.1% | -66.9 to 61.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 11.3 | 11.4 | +1.2% | -0.158 to 0.433 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 15.9 | 16.5 | +3.7% | -0.885 to 2.05 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.88 | 6.37 | +8.3% | -1.52 to 2.5 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 141 | +10.3% | 9.8 to 16.7 | power given |
| pages holding data, mean (MB) | 121 | 133 | +10.0% | 5.52 to 18.7 | power given |
| pages read from disk into the pool (misses) | 1,666,443 | 1,602,319 | -3.8% | -90,399 to -37,849 | shown, not judged |
| host CPU busy (share of the run) | 0.237 | 0.237 | -0.3% | -0.013 to 0.0117 | EVEN, no difference beyond the noise |
| host CPU-seconds | 382 | 382 | -0.1% | -20.4 to 19.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.52 | 4.53 | +0.3% | -0.262 to 0.287 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 7.8 to 13.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,954 | 2,953 | -0.1% | -13.3 to 10.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,956 | 2,955 | -0.0% | -7.02 to 6.78 | EVEN, no difference beyond the noise |
| queries a second | 2,956 | 2,955 | -0.0% | -7.02 to 6.78 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.298 | 0.301 | +1.2% | -0.0164 to 0.0237 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.37 | 0.379 | +2.4% | -0.0297 to 0.0477 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.185 | 0.186 | +0.5% | -0.00509 to 0.00682 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 134 | +4.6% | 2.27 to 9.5 | power given |
| pages holding data, mean (MB) | 121 | 131 | +7.8% | 3.04 to 15.8 | power given |
| pages read from disk into the pool (misses) | 1,030,380 | 1,012,991 | -1.7% | -26,512 to -8,265 | shown, not judged |
| host CPU busy (share of the run) | 0.148 | 0.148 | +0.2% | -0.00341 to 0.00403 | EVEN, no difference beyond the noise |
| host CPU-seconds | 263 | 264 | +0.2% | -6.11 to 7.18 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.195 | 0.196 | +0.3% | -0.00479 to 0.00579 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2.15 | 1.77 | -17.6% | -0.986 to 0.227 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 982 | -0.1% | -4.59 to 3.53 | EVEN, no difference beyond the noise |
| queries a second | 983 | 982 | -0.1% | -4.59 to 3.53 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.05 | 4.11 | +34.8% | -1.34 to 3.46 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.96 | 11.9 | +70.7% | -12.7 to 22.5 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.37 | 1.82 | +32.7% | -0.401 to 1.3 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 160 | +25.3% | -17.8 to 82.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 117 | 143 | +21.9% | -12.6 to 64 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 415,440 | 391,319 | -5.8% | -71,584 to 23,341 | shown, not judged |
| host CPU busy (share of the run) | 0.188 | 0.2 | +6.7% | -0.00641 to 0.0315 | EVEN, no difference beyond the noise |
| host CPU-seconds | 291 | 311 | +7.1% | -7.6 to 48.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 363 | 479 | +32.0% | -101 to 333 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | 2.04 to 20 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
