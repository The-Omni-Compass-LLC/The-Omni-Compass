# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.3% | -3.43 to 1.71 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.2% | -2.9 to 1.78 | EVEN, no difference beyond the noise |
| queries a second | 4,698 | 4,689 | -0.2% | -46.3 to 28.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.15 | 5.18 | +0.6% | -0.323 to 0.386 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.96 | 7.04 | +1.2% | -0.0967 to 0.265 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.3 | 3.28 | -0.7% | -0.102 to 0.0585 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 142 | +11.0% | 12.5 to 15.8 | power given |
| pages holding data, mean (MB) | 120 | 139 | +15.4% | 6.12 to 30.8 | power given |
| pages read from disk into the pool (misses) | 579,897 | 529,234 | -8.7% | -101,217 to -110 | shown, not judged |
| host CPU busy (share of the run) | 0.252 | 0.251 | -0.6% | -0.00353 to 0.000752 | EVEN, no difference beyond the noise |
| host CPU-seconds | 150 | 149 | -0.6% | -2.3 to 0.614 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.35 | 3.34 | -0.3% | -0.0703 to 0.0529 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.3% | -4.46 to 2.95 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | -0.3% | -3.89 to 2.28 | EVEN, no difference beyond the noise |
| queries a second | 4,695 | 4,682 | -0.3% | -62.2 to 36.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.88 | 2.88 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 4.77 | 4.74 | -0.6% | -0.572 to 0.511 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.53 | 2.22 | -12.6% | -2.14 to 1.51 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.3% | -0.602 to 16.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 134 | +11.8% | 4.84 to 23.6 | power given |
| pages read from disk into the pool (misses) | 1,975,917 | 1,912,370 | -3.2% | -149,463 to 22,369 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.165 | -1.5% | -0.00264 to -0.00222 | GAIN |
| host CPU-seconds | 304 | 300 | -1.5% | -4.75 to -4.23 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.26 | 2.23 | -1.2% | -0.0582 to 0.00355 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 196 | 196 | +0.0% | -0.966 to 1.08 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | -0.1% | -2.03 to 1.5 | EVEN, no difference beyond the noise |
| queries a second | 3,956 | 3,951 | -0.1% | -40.6 to 29.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.75 | 6.55 | -2.9% | -0.528 to 0.132 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 11.4 | 10.7 | -6.7% | -2.82 to 1.3 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.26 | 3.13 | -4.0% | -0.158 to -0.105 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 140 | +9.6% | 6.66 to 17.9 | power given |
| pages holding data, mean (MB) | 121 | 133 | +10.1% | 5.98 to 18.5 | power given |
| pages read from disk into the pool (misses) | 1,670,485 | 1,605,603 | -3.9% | -198,811 to 69,047 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.147 | -3.4% | -0.0158 to 0.00544 | EVEN, no difference beyond the noise |
| host CPU-seconds | 271 | 262 | -3.4% | -28.1 to 9.88 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.04 | 2.94 | -3.4% | -0.328 to 0.123 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,946 | +0.0% | -5.84 to 8.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,955 | +0.0% | -4.2 to 6.1 | EVEN, no difference beyond the noise |
| queries a second | 2,954 | 2,955 | +0.0% | -4.2 to 6.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.344 | 0.336 | -2.3% | -0.0166 to 0.000606 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.47 | 0.456 | -3.0% | -0.0269 to -0.00109 | GAIN |
| latency, mean (ms) | 0.207 | 0.204 | -1.8% | -0.0103 to 0.00304 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.0% | 2.35 to 13 | power given |
| pages holding data, mean (MB) | 121 | 132 | +8.5% | 3.79 to 16.9 | power given |
| pages read from disk into the pool (misses) | 1,029,911 | 1,011,754 | -1.8% | -24,625 to -11,689 | shown, not judged |
| host CPU busy (share of the run) | 0.166 | 0.163 | -1.4% | -0.00881 to 0.0041 | EVEN, no difference beyond the noise |
| host CPU-seconds | 291 | 287 | -1.4% | -15.8 to 7.87 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.216 | 0.213 | -1.4% | -0.012 to 0.0059 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.33 |  | 2.54 to 10.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 201 | 206 | +2.5% | -72.1 to 82 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 989 | 986 | -0.2% | -4.27 to 0.0614 | EVEN, no difference beyond the noise |
| queries a second | 989 | 986 | -0.2% | -4.27 to 0.0614 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.15 | 2.08 | -2.9% | -0.56 to 0.436 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.37 | 4.41 | +1.1% | -0.339 to 0.433 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.967 | 1.02 | +5.8% | -0.096 to 0.208 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 141 | +9.9% | 1.72 to 23.6 | power given |
| pages holding data, mean (MB) | 118 | 126 | +6.3% | 1.36 to 13.7 | power given |
| pages read from disk into the pool (misses) | 415,779 | 407,107 | -2.1% | -25,337 to 7,993 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.133 | -2.3% | -0.0255 to 0.0193 | EVEN, no difference beyond the noise |
| host CPU-seconds | 240 | 234 | -2.2% | -44.5 to 33.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.01 | 2.62 | -13.1% | -2.85 to 2.06 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.7 to 12.3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
