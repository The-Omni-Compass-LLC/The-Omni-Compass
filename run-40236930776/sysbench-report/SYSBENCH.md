# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 293 | +0.6% | -1.04 to 4.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.6% | -0.12 to 3.73 | EVEN, no difference beyond the noise |
| queries a second | 4,698 | 4,727 | +0.6% | -1.91 to 59.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.57 | 5.57 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 8.08 | 8.03 | -0.6% | -0.602 to 0.504 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.44 | 3.41 | -0.9% | -0.202 to 0.14 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.4% | 5.68 to 8.21 | power given |
| pages holding data, mean (MB) | 120 | 130 | +8.0% | 8.01 to 11.1 | power given |
| pages read from disk into the pool (misses) | 572,987 | 560,449 | -2.2% | -23,272 to -1,803 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.2 | +1.8% | -0.0044 to 0.0117 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 111 | +1.9% | -2.65 to 6.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.45 | 2.48 | +1.2% | -0.0954 to 0.155 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.0% | -5.46 to 5.21 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.0% | -5.38 to 5.09 | EVEN, no difference beyond the noise |
| queries a second | 4,727 | 4,725 | -0.0% | -86.1 to 81.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.91 | 3.89 | -0.6% | -0.225 to 0.179 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.54 | 5.47 | -1.2% | -0.446 to 0.314 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.05 | 3.04 | -0.4% | -0.14 to 0.118 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 131 | +2.5% | -0.258 to 6.59 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 126 | +4.7% | -6.28 to 17.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,988,214 | 2,036,938 | +2.5% | -27,862 to 125,310 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.185 | +0.0% | -0.00992 to 0.00992 | EVEN, no difference beyond the noise |
| host CPU-seconds | 309 | 309 | +0.1% | -16.2 to 16.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.29 | 2.29 | +0.1% | -0.128 to 0.133 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 194 | 194 | +0.1% | -8.21 to 8.49 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.0% | -2.41 to 2.45 | EVEN, no difference beyond the noise |
| queries a second | 3,948 | 3,948 | +0.0% | -48.1 to 49 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.66 | 6.66 | +0.0% | -3.59 to 3.59 | EVEN, the same |
| latency, 99th percentile (ms) | 18 | 17 | -5.5% | -47.5 to 45.5 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.19 | 3.15 | -1.1% | -1.57 to 1.5 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 146 | +14.1% | 0.634 to 35.5 | power given |
| pages holding data, mean (MB) | 122 | 138 | +13.5% | -3.62 to 36.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,665,755 | 1,573,790 | -5.5% | -239,743 to 55,813 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.135 | -1.9% | -0.00883 to 0.00347 | EVEN, no difference beyond the noise |
| host CPU-seconds | 246 | 241 | -2.0% | -16.1 to 6.46 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.78 | 2.72 | -2.0% | -0.243 to 0.13 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 7.23 to 10.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,944 | 2,947 | +0.1% | 1.06 to 4.11 | GAIN |
| throughput (transactions a second) | 2,951 | 2,954 | +0.1% | 0.719 to 5.67 | GAIN |
| queries a second | 2,951 | 2,954 | +0.1% | 0.719 to 5.67 | GAIN |
| latency, 95th percentile (ms) | 0.346 | 0.348 | +0.6% | -0.0208 to 0.0248 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.451 | 0.453 | +0.6% | -0.00881 to 0.0141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.212 | +1.1% | -0.00873 to 0.0134 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 130 | +1.9% | 2.02 to 2.82 | power given |
| pages holding data, mean (MB) | 121 | 124 | +2.5% | -0.0195 to 6.04 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,028,019 | 1,020,820 | -0.7% | -8,659 to -5,738 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.114 | +1.8% | -0.00803 to 0.012 | EVEN, no difference beyond the noise |
| host CPU-seconds | 187 | 190 | +1.7% | -13.6 to 20.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.139 | 0.141 | +1.6% | -0.0102 to 0.0147 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 158 | 137 | -13.4% | -108 to 66 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 988 | -0.0% | -3.85 to 2.87 | EVEN, no difference beyond the noise |
| queries a second | 988 | 988 | -0.0% | -3.85 to 2.87 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.32 | 2.18 | -6.4% | -0.636 to 0.34 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.92 | 4.52 | -8.0% | -1.41 to 0.618 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1.06 | +1.6% | -0.187 to 0.221 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 128 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 117 | 118 | +0.8% | -4.18 to 5.98 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 415,683 | 414,343 | -0.3% | -9,349 to 6,667 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.146 | +2.0% | -0.00894 to 0.0146 | EVEN, no difference beyond the noise |
| host CPU-seconds | 252 | 257 | +2.0% | -15.8 to 25.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.62 | 4.22 | +16.7% | -1.98 to 3.18 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
