# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 272 | 275 | +1.3% | -13.8 to 21.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 297 | +0.6% | -6.12 to 9.44 | EVEN, no difference beyond the noise |
| queries a second | 4,724 | 4,750 | +0.6% | -97.8 to 151 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 68.8 | 41.3 | -40.0% | -152 to 96.9 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 844 | 326 | -61.4% | -3,206 to 2,171 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 27.9 | 13 | -53.6% | -94 to 64 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 142 | +10.8% | -1.56 to 29.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 135 | +12.2% | -2.09 to 31.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 575,201 | 537,335 | -6.6% | -50,351 to -25,381 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.176 | +1.3% | -0.0017 to 0.00617 | EVEN, no difference beyond the noise |
| host CPU-seconds | 104 | 105 | +1.3% | -1.1 to 3.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.51 | 2.51 | -0.2% | -0.17 to 0.161 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | +0.2% | -3.53 to 4.98 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.2% | -3.47 to 4.92 | EVEN, no difference beyond the noise |
| queries a second | 4,715 | 4,726 | +0.2% | -55.5 to 78.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.03 | 4 | -0.6% | -0.127 to 0.0793 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.37 | 5.41 | +0.6% | -0.107 to 0.171 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.1 | 3.1 | +0.0% | -0.0787 to 0.0801 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.4% | 4.64 to 11.7 | power given |
| pages holding data, mean (MB) | 120 | 134 | +11.7% | 10.7 to 17.3 | power given |
| pages read from disk into the pool (misses) | 1,974,647 | 1,910,452 | -3.3% | -111,941 to -16,447 | shown, not judged |
| host CPU busy (share of the run) | 0.245 | 0.246 | +0.4% | -0.00491 to 0.00694 | EVEN, no difference beyond the noise |
| host CPU-seconds | 435 | 437 | +0.4% | -8.66 to 12.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.23 | 3.23 | +0.1% | -0.0869 to 0.0958 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 178 | 178 | +0.4% | -2.62 to 4.03 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.1% | -2.9 to 3.47 | EVEN, no difference beyond the noise |
| queries a second | 3,930 | 3,936 | +0.1% | -58.1 to 69.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 13.3 | 12.9 | -3.0% | -0.732 to -0.0533 | GAIN |
| latency, 99th percentile (ms) | 20.1 | 18.5 | -8.1% | -2.25 to -1 | GAIN |
| latency, mean (ms) | 7.38 | 6.5 | -11.9% | -3.34 to 1.59 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 142 | +11.1% | 10.7 to 17.6 | power given |
| pages holding data, mean (MB) | 120 | 134 | +11.5% | 9.62 to 18.2 | power given |
| pages read from disk into the pool (misses) | 1,666,212 | 1,595,762 | -4.2% | -116,264 to -24,637 | shown, not judged |
| host CPU busy (share of the run) | 0.254 | 0.256 | +0.8% | -0.00204 to 0.006 | EVEN, no difference beyond the noise |
| host CPU-seconds | 410 | 413 | +0.9% | -2.84 to 9.84 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.03 | 5.06 | +0.5% | -0.12 to 0.166 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 |  | 8.46 to 14.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,963 | 2,960 | -0.1% | -13.1 to 6.75 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,963 | -0.1% | -9.4 to 5.04 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,963 | -0.1% | -9.4 to 5.04 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.133 | 0.133 | +0.3% | -0.0114 to 0.0121 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.28 | 0.285 | +1.8% | -0.0422 to 0.0522 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0774 | 0.0845 | +9.2% | -0.0106 to 0.0249 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 134 | +5.0% | 3.24 to 9.5 | power given |
| pages holding data, mean (MB) | 121 | 132 | +8.7% | 7.31 to 13.7 | power given |
| pages read from disk into the pool (misses) | 1,030,134 | 1,008,489 | -2.1% | -33,176 to -10,113 | shown, not judged |
| host CPU busy (share of the run) | 0.0619 | 0.0659 | +6.4% | -0.00331 to 0.0113 | EVEN, no difference beyond the noise |
| host CPU-seconds | 111 | 118 | +6.4% | -6.03 to 20.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.082 | 0.0873 | +6.5% | -0.00446 to 0.0151 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 14.7 | 10.7 | -27.5% | -10 to 1.89 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 984 | +0.1% | -2.93 to 5.45 | EVEN, no difference beyond the noise |
| queries a second | 983 | 984 | +0.1% | -2.93 to 5.45 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.2 | 2.54 | +15.7% | 0.000269 to 0.691 | LOSS |
| latency, 99th percentile (ms) | 3.89 | 4.5 | +15.7% | 0.0201 to 1.2 | LOSS |
| latency, mean (ms) | 1.13 | 1.2 | +6.9% | -0.0306 to 0.186 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.5% | 7.28 to 14.5 | power given |
| pages holding data, mean (MB) | 118 | 124 | +5.2% | 1.38 to 10.9 | power given |
| pages read from disk into the pool (misses) | 416,117 | 410,251 | -1.4% | -15,188 to 3,457 | shown, not judged |
| host CPU busy (share of the run) | 0.249 | 0.288 | +15.6% | -0.0217 to 0.0992 | EVEN, no difference beyond the noise |
| host CPU-seconds | 437 | 504 | +15.4% | -37.6 to 172 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 67.1 | 127 | +89.0% | -85.6 to 205 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 5.8 to 11.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
