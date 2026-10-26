# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 277 | 274 | -1.3% | -8.71 to 1.59 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.3% | -4.56 to 6.21 | EVEN, no difference beyond the noise |
| queries a second | 4,712 | 4,725 | +0.3% | -72.9 to 99.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 15.4 | 54.6 | +255.1% | -85.3 to 164 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 126 | 321 | +155.2% | -425 to 816 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.25 | 13.6 | +116.8% | -15.8 to 30.4 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 140 | +9.0% | -7.53 to 30.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 131 | +9.5% | -4.56 to 27.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 568,352 | 530,255 | -6.7% | -76,692 to 498 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.173 | +0.7% | 0.000722 to 0.00179 | power given |
| host CPU-seconds | 103 | 103 | +0.8% | 0.432 to 1.13 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.43 | 2.48 | +2.1% | 0.00332 to 0.0974 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | -0.0% | -2.25 to 2.02 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | +0.0% | -2.06 to 2.19 | EVEN, no difference beyond the noise |
| queries a second | 4,736 | 4,737 | +0.0% | -32.9 to 35.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.68 | 2.68 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 4.54 | 4.47 | -1.6% | -2.12 to 1.97 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.3 | 2.5 | +8.7% | -0.921 to 1.32 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 131 | +2.6% | -0.255 to 6.99 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 128 | +6.7% | 2.94 to 13.1 | power given |
| pages read from disk into the pool (misses) | 1,984,027 | 2,033,603 | +2.5% | -79,049 to 178,200 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.164 | -0.5% | -0.00263 to 0.00103 | EVEN, no difference beyond the noise |
| host CPU-seconds | 295 | 294 | -0.5% | -4.92 to 1.82 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.2 | 2.19 | -0.5% | -0.0194 to -0.00154 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 181 | 181 | +0.3% | -1.82 to 2.92 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.2% | -3.83 to 3.19 | EVEN, no difference beyond the noise |
| queries a second | 3,927 | 3,921 | -0.2% | -76.6 to 63.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 12.3 | 12.2 | -1.2% | -0.976 to 0.684 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 17.1 | 16.9 | -1.2% | -0.644 to 0.235 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.18 | 6.15 | -0.5% | -0.181 to 0.116 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 146 | +14.2% | 11.5 to 24.8 | power given |
| pages holding data, mean (MB) | 121 | 138 | +14.8% | 15.3 to 20.4 | power given |
| pages read from disk into the pool (misses) | 1,666,497 | 1,581,119 | -5.1% | -163,248 to -7,508 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.249 | -0.9% | -0.00613 to 0.00158 | EVEN, no difference beyond the noise |
| host CPU-seconds | 406 | 403 | -0.9% | -8.63 to 1.69 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.91 | 4.85 | -1.2% | -0.168 to 0.0536 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,960 | 2,957 | -0.1% | -9.45 to 3.5 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,963 | -0.1% | -6.35 to 3.11 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,963 | -0.1% | -6.35 to 3.11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.213 | 0.23 | +8.0% | 0.00617 to 0.0278 | LOSS |
| latency, 99th percentile (ms) | 0.324 | 0.348 | +7.4% | -0.00333 to 0.0513 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0902 | 0.0982 | +8.8% | -0.00578 to 0.0217 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 129 | +1.2% | -4.94 to 7.94 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 124 | +2.2% | -8.43 to 13.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,029,199 | 1,026,365 | -0.3% | -11,597 to 5,929 | shown, not judged |
| host CPU busy (share of the run) | 0.0689 | 0.0768 | +11.4% | -0.000132 to 0.0158 | EVEN, no difference beyond the noise |
| host CPU-seconds | 124 | 138 | +11.3% | -0.202 to 28.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0917 | 0.102 | +11.4% | -0.000231 to 0.0212 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.667 |  | -2.2 to 3.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.46 | 2.93 | -15.4% | -4.39 to 3.33 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 981 | 981 | +0.0% | -6.13 to 6.79 | EVEN, no difference beyond the noise |
| queries a second | 981 | 981 | +0.0% | -6.13 to 6.79 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.94 | 1.88 | -3.2% | -0.631 to 0.507 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.01 | 3.59 | -10.4% | -4.33 to 3.49 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.14 | 1.17 | +2.8% | -0.258 to 0.322 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 128 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 119 | 118 | -1.0% | -2.63 to 0.372 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 414,971 | 413,991 | -0.2% | -10,452 to 8,492 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.173 | +0.2% | -0.023 to 0.0237 | EVEN, no difference beyond the noise |
| host CPU-seconds | 309 | 310 | +0.2% | -40.6 to 41.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 223 | 232 | +4.0% | -290 to 308 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
