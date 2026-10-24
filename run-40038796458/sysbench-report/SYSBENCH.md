# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 294 | -0.6% | -6.29 to 2.88 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 297 | 295 | -0.8% | -4.03 to -0.476 | LOSS |
| queries a second | 4,751 | 4,715 | -0.8% | -64.5 to -7.62 | LOSS |
| latency, 95th percentile (ms) | 3.24 | 3.08 | -5.0% | -1 to 0.676 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.07 | 4.68 | -7.7% | -2.26 to 1.48 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.49 | 1.44 | -3.6% | -0.39 to 0.284 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 133 | +3.9% | -5.78 to 15.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 126 | +4.8% | -6.26 to 17.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 570,238 | 550,176 | -3.5% | -97,471 to 57,346 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.105 | -0.3% | -0.0153 to 0.0146 | EVEN, no difference beyond the noise |
| host CPU-seconds | 63.3 | 63.1 | -0.3% | -9.24 to 8.84 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.41 | 1.41 | +0.3% | -0.208 to 0.216 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.33 |  | -1.54 to 4.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 291 | -0.1% | -2.69 to 2.36 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 292 | -0.2% | -3.11 to 2.15 | EVEN, no difference beyond the noise |
| queries a second | 4,685 | 4,677 | -0.2% | -49.8 to 34.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.93 | 2.93 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 4.88 | 4.82 | -1.2% | -0.881 to 0.762 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.18 | 2.4 | -24.6% | -4.65 to 3.09 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.6% | 4.5 to 14.9 | power given |
| pages holding data, mean (MB) | 120 | 134 | +11.9% | 7.03 to 21.4 | power given |
| pages read from disk into the pool (misses) | 1,983,175 | 1,921,087 | -3.1% | -188,152 to 63,974 | shown, not judged |
| host CPU busy (share of the run) | 0.171 | 0.17 | -0.1% | -0.00282 to 0.00255 | EVEN, no difference beyond the noise |
| host CPU-seconds | 310 | 310 | -0.1% | -5.52 to 4.75 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.31 | 2.31 | -0.0% | -0.0171 to 0.016 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 189 | -0.2% | -1.67 to 0.781 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.4% | -1.74 to -0.00619 | LOSS |
| queries a second | 3,935 | 3,918 | -0.4% | -34.8 to -0.124 | LOSS |
| latency, 95th percentile (ms) | 9.85 | 9.62 | -2.4% | -0.484 to 0.0177 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.9 | 13.6 | -1.8% | -1.32 to 0.815 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.15 | 5.1 | -1.0% | -0.136 to 0.0294 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 141 | +10.4% | 10.4 to 16.1 | power given |
| pages holding data, mean (MB) | 120 | 132 | +10.0% | 3.18 to 20.9 | power given |
| pages read from disk into the pool (misses) | 1,667,496 | 1,597,945 | -4.2% | -119,690 to -19,412 | shown, not judged |
| host CPU busy (share of the run) | 0.28 | 0.277 | -1.1% | -0.00679 to 0.000355 | EVEN, no difference beyond the noise |
| host CPU-seconds | 494 | 489 | -1.1% | -11.6 to 0.524 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.69 | 5.64 | -0.9% | -0.156 to 0.0551 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 7.8 to 13.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,966 | 2,965 | -0.0% | -16.9 to 15.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,967 | 2,966 | -0.0% | -17.6 to 16 | EVEN, no difference beyond the noise |
| queries a second | 2,967 | 2,966 | -0.0% | -17.6 to 16 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.126 | 0.123 | -1.9% | -0.021 to 0.0163 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.273 | 0.272 | -0.5% | -0.019 to 0.0163 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.08 | 0.0789 | -1.4% | -0.00659 to 0.00426 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.2% | 1.11 to 14.8 | power given |
| pages holding data, mean (MB) | 121 | 131 | +8.0% | -3.21 to 22.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,029,846 | 1,005,878 | -2.3% | -51,596 to 3,659 | shown, not judged |
| host CPU busy (share of the run) | 0.0629 | 0.0622 | -1.2% | -0.00507 to 0.00357 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 111 | -1.2% | -9.14 to 6.37 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0836 | 0.0826 | -1.2% | -0.0064 to 0.00439 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 96.6 | 95.2 | -1.5% | -50 to 47.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 980 | 981 | +0.0% | -5.04 to 5.07 | EVEN, no difference beyond the noise |
| queries a second | 980 | 981 | +0.0% | -5.04 to 5.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.45 | 1.38 | -5.1% | -0.355 to 0.207 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.39 | 2.11 | -11.8% | -1.61 to 1.05 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.89 | 0.926 | +4.1% | 0.0111 to 0.0616 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.9% | 4.86 to 15.4 | power given |
| pages holding data, mean (MB) | 119 | 124 | +4.2% | -0.458 to 10.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 415,004 | 409,794 | -1.3% | -11,893 to 1,473 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.195 | -1.8% | -0.023 to 0.0157 | EVEN, no difference beyond the noise |
| host CPU-seconds | 352 | 346 | -1.7% | -39.2 to 27 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 8.82 | 8.45 | -4.2% | -4.2 to 3.46 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 2.7 to 11.3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
