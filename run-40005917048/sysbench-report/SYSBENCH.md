# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.1% | -2.79 to 3.35 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.1% | -2.68 to 3.49 | EVEN, no difference beyond the noise |
| queries a second | 4,704 | 4,710 | +0.1% | -42.9 to 55.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.31 | 5.28 | -0.6% | -0.17 to 0.106 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.21 | 7.21 | +0.0% | -0.323 to 0.323 | EVEN, the same |
| latency, mean (ms) | 3.44 | 3.42 | -0.8% | -0.0772 to 0.0245 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 147 | +14.6% | 0.05 to 37.2 | power given |
| pages holding data, mean (MB) | 120 | 142 | +18.0% | -0.696 to 44.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 583,300 | 534,041 | -8.4% | -114,814 to 16,296 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.205 | -0.4% | -0.00618 to 0.00442 | EVEN, no difference beyond the noise |
| host CPU-seconds | 115 | 114 | -0.5% | -3.48 to 2.39 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.56 | 2.55 | -0.6% | -0.0525 to 0.0234 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.2% | -4.86 to 5.81 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.2% | -4.83 to 5.77 | EVEN, no difference beyond the noise |
| queries a second | 4,716 | 4,724 | +0.2% | -77.2 to 92.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.2 | 4.15 | -1.2% | -0.159 to 0.058 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.57 | 5.44 | -2.4% | -0.28 to 0.0144 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.3 | 3.28 | -0.8% | -0.0379 to -0.0158 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +8.2% | 1.56 to 19.4 | power given |
| pages holding data, mean (MB) | 120 | 136 | +13.6% | 5.77 to 26.9 | power given |
| pages read from disk into the pool (misses) | 1,979,103 | 1,897,963 | -4.1% | -114,208 to -48,073 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.205 | -0.5% | -0.00479 to 0.00266 | EVEN, no difference beyond the noise |
| host CPU-seconds | 345 | 343 | -0.5% | -8.23 to 4.72 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.56 | 2.54 | -0.7% | -0.0631 to 0.0284 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 178 | 179 | +0.4% | -2.45 to 3.83 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.0% | -1.5 to 1.35 | EVEN, no difference beyond the noise |
| queries a second | 3,923 | 3,922 | -0.0% | -30 to 27 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 13.1 | 12.9 | -1.1% | -1.59 to 1.31 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 18.6 | 18 | -3.4% | -2.76 to 1.49 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.56 | 6.46 | -1.5% | -0.602 to 0.403 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 142 | +10.6% | 11.5 to 15.5 | power given |
| pages holding data, mean (MB) | 122 | 134 | +10.1% | 11 to 13.6 | power given |
| pages read from disk into the pool (misses) | 1,665,825 | 1,591,692 | -4.5% | -156,928 to 8,663 | shown, not judged |
| host CPU busy (share of the run) | 0.266 | 0.26 | -2.4% | -0.0317 to 0.019 | EVEN, no difference beyond the noise |
| host CPU-seconds | 429 | 419 | -2.4% | -49.6 to 29.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.27 | 5.13 | -2.7% | -0.709 to 0.428 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 8.9 to 11.8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,941 | 2,938 | -0.1% | -6.56 to -0.219 | LOSS |
| throughput (transactions a second) | 2,954 | 2,949 | -0.2% | -8.5 to -1.31 | LOSS |
| queries a second | 2,954 | 2,949 | -0.2% | -8.5 to -1.31 | LOSS |
| latency, 95th percentile (ms) | 0.357 | 0.34 | -4.7% | -0.0408 to 0.00746 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.53 | 0.52 | -1.8% | -0.0513 to 0.0319 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.209 | -3.0% | -0.0132 to 0.000295 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.2% | 3.2 to 10 | power given |
| pages holding data, mean (MB) | 121 | 130 | +7.0% | 1.29 to 15.6 | power given |
| pages read from disk into the pool (misses) | 1,029,843 | 1,005,526 | -2.4% | -37,334 to -11,299 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.108 | -3.9% | -0.00788 to -0.000957 | GAIN |
| host CPU-seconds | 188 | 180 | -3.9% | -12.9 to -1.81 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 0.14 | 0.134 | -3.8% | -0.00953 to -0.00105 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 109 | 94.5 | -13.5% | -82.3 to 52.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 989 | 988 | -0.1% | -3.77 to 2.71 | EVEN, no difference beyond the noise |
| queries a second | 989 | 988 | -0.1% | -3.77 to 2.71 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 187 | 138 | -26.1% | -309 to 211 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 772 | 273 | -64.6% | -2,241 to 1,244 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 40.8 | 24.6 | -39.7% | -88.8 to 56.4 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 144 | +12.6% | 10.2 to 21.9 | power given |
| pages holding data, mean (MB) | 119 | 129 | +8.9% | 4.3 to 16.9 | power given |
| pages read from disk into the pool (misses) | 418,440 | 408,999 | -2.3% | -19,538 to 657 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.161 | -1.1% | -0.0248 to 0.0213 | EVEN, no difference beyond the noise |
| host CPU-seconds | 288 | 285 | -1.0% | -42.9 to 37 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 6.57 | 6.74 | +2.6% | -5.05 to 5.4 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 8 to 8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
