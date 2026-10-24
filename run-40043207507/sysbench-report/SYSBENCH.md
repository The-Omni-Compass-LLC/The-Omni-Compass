# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 294 | +0.7% | -0.917 to 4.98 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 295 | +0.7% | -0.966 to 5.04 | EVEN, no difference beyond the noise |
| queries a second | 4,694 | 4,727 | +0.7% | -15.4 to 80.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.21 | 5.18 | -0.6% | -0.3 to 0.238 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.17 | 7.25 | +1.2% | -0.0998 to 0.273 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.35 | 3.34 | -0.3% | -0.0287 to 0.00722 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 514 | +0.4% | -50.7 to 54.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 420 | -5.9% | -104 to 51.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,473 | 242,899 | -0.6% | -49,114 to 45,965 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.198 | +1.0% | 0.000759 to 0.00317 | power given |
| host CPU-seconds | 108 | 109 | +1.0% | 0.243 to 1.96 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.41 | 2.42 | +0.5% | -0.0164 to 0.0393 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 5.8 to 11.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 296 | +0.1% | -0.529 to 0.985 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.1% | -0.366 to 1.05 | EVEN, no difference beyond the noise |
| queries a second | 4,727 | 4,732 | +0.1% | -5.86 to 16.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.91 | 3.82 | -2.4% | -0.195 to 0.00917 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.15 | 5.09 | -1.2% | -0.195 to 0.0714 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.07 | 3.05 | -0.5% | -0.0532 to 0.0244 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 576 | +12.6% | -30 to 159 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 500 | +8.3% | -28.7 to 105 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,960 | 541,886 | -17.4% | -355,447 to 127,301 | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.18 | -0.3% | -0.0025 to 0.00141 | EVEN, no difference beyond the noise |
| host CPU-seconds | 299 | 299 | -0.3% | -4.56 to 2.92 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.22 | 2.21 | -0.4% | -0.0383 to 0.0222 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 22 |  | 17.7 to 26.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 174 | 176 | +1.1% | -8.09 to 11.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.3% | -2.97 to 1.9 | EVEN, no difference beyond the noise |
| queries a second | 3,954 | 3,943 | -0.3% | -59.4 to 37.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 58.9 | 43.7 | -25.7% | -86.6 to 56.3 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 246 | 153 | -37.8% | -433 to 247 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 14.3 | 10.3 | -27.8% | -21.3 to 13.4 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 549 | +7.2% | -153 to 227 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 489 | +6.0% | -118 to 173 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,227 | 596,824 | -3.0% | -258,962 to 222,156 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.181 | -0.6% | -0.0105 to 0.0083 | EVEN, no difference beyond the noise |
| host CPU-seconds | 323 | 321 | -0.6% | -18.5 to 14.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.08 | 4 | -1.8% | -0.529 to 0.384 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.7 |  | 9.87 to 17.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,960 | -0.0% | -16.3 to 13.5 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,964 | 2,963 | -0.0% | -14.3 to 12.3 | EVEN, no difference beyond the noise |
| queries a second | 2,964 | 2,963 | -0.0% | -14.3 to 12.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.153 | 0.161 | +5.2% | -0.0971 to 0.113 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.327 | 0.332 | +1.6% | -0.0495 to 0.0601 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0898 | 0.0908 | +1.1% | -0.0453 to 0.0471 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 497 | -3.0% | -120 to 90.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 456 | -1.6% | -112 to 96.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,733 | 373,446 | +1.6% | -112,353 to 123,780 | shown, not judged |
| host CPU busy (share of the run) | 0.0696 | 0.0694 | -0.3% | -0.0358 to 0.0354 | EVEN, no difference beyond the noise |
| host CPU-seconds | 125 | 124 | -0.2% | -63.6 to 63 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0924 | 0.0922 | -0.2% | -0.0475 to 0.047 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 |  | 5.46 to 11.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 139 | 142 | +2.2% | -49.9 to 56.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 987 | -0.1% | -2.99 to 0.612 | EVEN, no difference beyond the noise |
| queries a second | 988 | 987 | -0.1% | -2.99 to 0.612 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 86.4 | 136 | +57.5% | -66.2 to 166 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 213 | 358 | +68.7% | -81.5 to 373 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 13.3 | 23 | +72.7% | -8.85 to 28.2 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 475 | -7.3% | -198 to 123 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 381 | -16.0% | -192 to 47 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 190,191 | 235,795 | +24.0% | 1,042 to 90,166 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.136 | -2.1% | -0.0185 to 0.0125 | EVEN, no difference beyond the noise |
| host CPU-seconds | 246 | 241 | -1.9% | -31.6 to 22 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.98 | 3.8 | -4.6% | -2.05 to 1.68 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17 |  | 9.55 to 24.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
