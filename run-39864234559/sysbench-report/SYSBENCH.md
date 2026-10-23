# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 296 | +0.5% | -5.52 to 8.23 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.4% | -4.37 to 6.86 | EVEN, no difference beyond the noise |
| queries a second | 4,723 | 4,743 | +0.4% | -69.9 to 110 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.83 | 2.74 | -3.0% | -0.372 to 0.204 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.55 | 4.36 | -4.1% | -1.22 to 0.845 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.31 | 1.28 | -2.1% | -0.129 to 0.0756 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +5.9% | 7.53 to 7.53 | power given |
| pages holding data, mean (MB) | 120 | 132 | +10.2% | 3.33 to 21.2 | power given |
| pages read from disk into the pool (misses) | 568,453 | 549,846 | -3.3% | -39,401 to 2,187 | shown, not judged |
| host CPU busy (share of the run) | 0.0943 | 0.0931 | -1.3% | -0.00354 to 0.00111 | EVEN, no difference beyond the noise |
| host CPU-seconds | 56.6 | 55.8 | -1.4% | -2.17 to 0.639 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.26 | 1.24 | -1.8% | -0.0312 to -0.014 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.2% | -2.4 to 0.981 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.2% | -2.69 to 1.25 | EVEN, no difference beyond the noise |
| queries a second | 4,728 | 4,716 | -0.2% | -43 to 20 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.49 | 3.49 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 4.57 | 4.57 | +0.0% | -0.205 to 0.205 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.77 | 2.77 | -0.2% | -0.0478 to 0.0384 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.5% | 4.85 to 11.8 | power given |
| pages holding data, mean (MB) | 120 | 134 | +11.6% | 10.4 to 17.4 | power given |
| pages read from disk into the pool (misses) | 1,989,279 | 1,910,144 | -4.0% | -207,625 to 49,355 | shown, not judged |
| host CPU busy (share of the run) | 0.219 | 0.218 | -0.2% | -0.00416 to 0.00344 | EVEN, no difference beyond the noise |
| host CPU-seconds | 391 | 390 | -0.2% | -7.85 to 6.57 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.89 | 2.89 | +0.1% | -0.0394 to 0.0442 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 194 | +1.3% | -5.23 to 10.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.5% | -0.891 to 2.76 | EVEN, no difference beyond the noise |
| queries a second | 3,938 | 3,957 | +0.5% | -17.8 to 55.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.57 | 6.76 | -10.7% | -3.77 to 2.15 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 22.9 | 16.5 | -28.1% | -35.9 to 23 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.49 | 3.27 | -6.3% | -1.06 to 0.623 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 132 | +3.2% | -2.74 to 11 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 122 | 126 | +3.2% | -0.476 to 8.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,662,445 | 1,643,247 | -1.2% | -88,032 to 49,637 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.142 | -0.2% | -0.0225 to 0.0219 | EVEN, no difference beyond the noise |
| host CPU-seconds | 254 | 253 | -0.2% | -39.5 to 38.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.9 | 2.86 | -1.5% | -0.364 to 0.278 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | -2.4 to 9.07 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,943 | -0.2% | -22 to 11.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,956 | 2,952 | -0.2% | -18.3 to 8.9 | EVEN, no difference beyond the noise |
| queries a second | 2,956 | 2,952 | -0.2% | -18.3 to 8.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.342 | 0.342 | +0.0% | -0.0298 to 0.0298 | EVEN, the same |
| latency, 99th percentile (ms) | 0.459 | 0.459 | +0.1% | -0.0208 to 0.0215 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.208 | -0.2% | -0.0171 to 0.0163 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +5.9% | 7.41 to 7.62 | power given |
| pages holding data, mean (MB) | 121 | 132 | +8.6% | 9.97 to 11 | power given |
| pages read from disk into the pool (misses) | 1,031,154 | 1,003,551 | -2.7% | -31,012 to -24,195 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.11 | -0.9% | -0.0121 to 0.0102 | EVEN, no difference beyond the noise |
| host CPU-seconds | 185 | 183 | -0.9% | -20.3 to 16.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.137 | 0.136 | -0.7% | -0.0155 to 0.0135 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 124 | 124 | +0.2% | -91.3 to 91.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 986 | 987 | +0.1% | -0.0411 to 1.32 | EVEN, no difference beyond the noise |
| queries a second | 986 | 987 | +0.1% | -0.0411 to 1.32 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 170 | 156 | -8.0% | -24.7 to -2.61 | GAIN |
| latency, 99th percentile (ms) | 906 | 753 | -17.0% | -2,824 to 2,517 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 38.8 | 36.5 | -5.9% | -66.8 to 62.2 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 144 | +12.5% | 9.36 to 22.6 | power given |
| pages holding data, mean (MB) | 119 | 130 | +8.8% | 3.53 to 17.5 | power given |
| pages read from disk into the pool (misses) | 418,172 | 407,624 | -2.5% | -16,455 to -4,641 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.164 | +0.9% | -0.00953 to 0.0125 | EVEN, no difference beyond the noise |
| host CPU-seconds | 287 | 289 | +0.9% | -18.7 to 23.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.09 | 5.38 | +5.7% | -3.41 to 4 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 5.8 to 11.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
