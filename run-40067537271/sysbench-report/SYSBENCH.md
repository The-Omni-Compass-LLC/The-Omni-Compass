# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | -0.1% | -4.32 to 3.83 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.2% | -4.98 to 3.78 | EVEN, no difference beyond the noise |
| queries a second | 4,699 | 4,690 | -0.2% | -79.7 to 60.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.37 | 5.28 | -1.8% | -0.331 to 0.141 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.34 | 7.17 | -2.3% | -0.984 to 0.641 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.43 | 3.38 | -1.4% | -0.112 to 0.0153 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 147 | +14.7% | -1.55 to 39.2 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 145 | +20.6% | 8.61 to 40.9 | power given |
| pages read from disk into the pool (misses) | 576,142 | 536,355 | -6.9% | -90,565 to 10,992 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.203 | -0.4% | -0.0102 to 0.00869 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 112 | -0.4% | -5.81 to 4.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.52 | 2.52 | -0.3% | -0.11 to 0.0932 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 297 | 296 | -0.1% | -4.68 to 4.03 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.1% | -4.66 to 3.91 | EVEN, no difference beyond the noise |
| queries a second | 4,747 | 4,741 | -0.1% | -74.6 to 62.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.66 | 1.63 | -1.8% | -0.181 to 0.12 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.93 | 2.84 | -3.0% | -0.366 to 0.188 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.18 | -1.6% | -0.0887 to 0.0501 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 132 | +3.3% | 0.622 to 7.73 | power given |
| pages holding data, mean (MB) | 120 | 129 | +7.9% | 2.59 to 16.4 | power given |
| pages read from disk into the pool (misses) | 1,995,522 | 1,983,039 | -0.6% | -140,842 to 115,876 | shown, not judged |
| host CPU busy (share of the run) | 0.0959 | 0.0947 | -1.2% | -0.00514 to 0.00283 | EVEN, no difference beyond the noise |
| host CPU-seconds | 172 | 170 | -1.2% | -9.37 to 5.18 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.28 | 1.26 | -1.1% | -0.0769 to 0.0492 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 179 | 181 | +1.0% | -1.04 to 4.49 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 197 | +0.3% | -0.197 to 1.36 | EVEN, no difference beyond the noise |
| queries a second | 3,928 | 3,940 | +0.3% | -3.94 to 27.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 12.9 | 12.6 | -2.4% | -1.19 to 0.57 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 19.7 | 17.8 | -10.0% | -9.24 to 5.3 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7.09 | 6.37 | -10.2% | -3.99 to 2.54 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 143 | +11.5% | 8.81 to 20.6 | power given |
| pages holding data, mean (MB) | 122 | 135 | +10.3% | 6.74 to 18.4 | power given |
| pages read from disk into the pool (misses) | 1,665,536 | 1,595,244 | -4.2% | -151,538 to 10,953 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.248 | -1.1% | -0.00681 to 0.00114 | EVEN, no difference beyond the noise |
| host CPU-seconds | 405 | 401 | -1.1% | -10 to 1.31 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.95 | 4.85 | -2.0% | -0.216 to 0.0148 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 7.8 to 13.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,957 | 2,955 | -0.1% | -32 to 28.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,967 | +0.1% | -12.9 to 16.5 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,967 | +0.1% | -12.9 to 16.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.237 | 0.237 | +0.0% | -0.00994 to 0.00994 | EVEN, the same |
| latency, 99th percentile (ms) | 0.354 | 0.357 | +0.7% | -0.0493 to 0.054 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.275 | +21.9% | -0.266 to 0.365 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 133 | +3.9% | 5.05 to 5.05 | power given |
| pages holding data, mean (MB) | 121 | 128 | +5.5% | 2.19 to 11.2 | power given |
| pages read from disk into the pool (misses) | 1,029,140 | 1,016,269 | -1.3% | -16,391 to -9,350 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.115 | +1.0% | -0.00269 to 0.00494 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 205 | +1.0% | -4.82 to 8.78 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.151 | 0.152 | +1.0% | -0.00369 to 0.00685 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 235 | 239 | +1.6% | -86.1 to 93.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 987 | 986 | -0.1% | -2.03 to 0.302 | EVEN, no difference beyond the noise |
| queries a second | 987 | 986 | -0.1% | -2.03 to 0.302 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 16 | 7.52 | -52.9% | -71.4 to 54.5 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 456 | 122 | -73.1% | -2,021 to 1,354 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 14.3 | 4.76 | -66.7% | -57.3 to 38.3 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.8% | 5.46 to 9.5 | power given |
| pages holding data, mean (MB) | 117 | 124 | +6.2% | 0.363 to 14.2 | power given |
| pages read from disk into the pool (misses) | 418,617 | 412,867 | -1.4% | -15,970 to 4,471 | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.169 | +0.6% | -0.062 to 0.064 | EVEN, no difference beyond the noise |
| host CPU-seconds | 295 | 297 | +0.6% | -106 to 110 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.88 | 2.73 | -4.9% | -2.44 to 2.15 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | -3.51 to 10.8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
