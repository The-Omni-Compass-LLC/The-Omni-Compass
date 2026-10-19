# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.2% | -2.78 to 4.05 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.2% | -2.55 to 3.73 | EVEN, no difference beyond the noise |
| queries a second | 4,688 | 4,698 | +0.2% | -40.7 to 59.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.31 | 5.31 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 7.3 | 7.3 | +0.0% | -0.326 to 0.328 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.4 | 3.38 | -0.7% | -0.115 to 0.0704 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.5% | -1.26 to 20.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 133 | +10.4% | 1.84 to 23.1 | power given |
| pages read from disk into the pool (misses) | 578,402 | 539,224 | -6.8% | -60,837 to -17,520 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.2 | -1.3% | -0.00986 to 0.00439 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 111 | -1.6% | -6.35 to 2.81 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.52 | 2.48 | -1.7% | -0.166 to 0.0802 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | -0.1% | -1.77 to 0.996 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.1% | -1.9 to 1.17 | EVEN, no difference beyond the noise |
| queries a second | 4,742 | 4,736 | -0.1% | -30.4 to 18.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.8 | 1.81 | +0.6% | -0.0341 to 0.0548 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.62 | 3.71 | +2.4% | -0.387 to 0.562 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.26 | +2.1% | -0.0424 to 0.0956 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.2% | 4.09 to 17 | power given |
| pages holding data, mean (MB) | 120 | 139 | +15.8% | 13.9 to 24 | power given |
| pages read from disk into the pool (misses) | 1,999,442 | 1,923,564 | -3.8% | -247,785 to 96,029 | shown, not judged |
| host CPU busy (share of the run) | 0.0976 | 0.1 | +2.7% | -0.00391 to 0.00911 | EVEN, no difference beyond the noise |
| host CPU-seconds | 175 | 180 | +2.7% | -7.19 to 16.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.3 | 1.34 | +2.8% | -0.0454 to 0.118 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 185 | 180 | -2.6% | -18 to 8.48 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.4% | -4.79 to 3.13 | EVEN, no difference beyond the noise |
| queries a second | 3,956 | 3,939 | -0.4% | -95.8 to 62.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 23.8 | 33.5 | +40.9% | -38 to 57.4 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 153 | 171 | +11.2% | -36.1 to 70.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 9.49 | 10.7 | +13.1% | -0.696 to 3.19 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 137 | +6.8% | 5.89 to 11.5 | power given |
| pages holding data, mean (MB) | 122 | 128 | +5.4% | 1.56 to 11.5 | power given |
| pages read from disk into the pool (misses) | 1,671,699 | 1,613,168 | -3.5% | -140,504 to 23,443 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.205 | -0.8% | -0.00568 to 0.00248 | EVEN, no difference beyond the noise |
| host CPU-seconds | 366 | 363 | -0.7% | -9.56 to 4.13 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.34 | 4.42 | +1.8% | -0.222 to 0.382 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,940 | 2,937 | -0.1% | -22.7 to 15.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,951 | -0.1% | -14.3 to 9.46 | EVEN, no difference beyond the noise |
| queries a second | 2,953 | 2,951 | -0.1% | -14.3 to 9.46 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.383 | 0.388 | +1.2% | -0.0612 to 0.0705 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.53 | 0.543 | +2.5% | -0.0482 to 0.0742 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.219 | 0.225 | +2.9% | -0.0187 to 0.0316 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.7% | 0.78 to 21.4 | power given |
| pages holding data, mean (MB) | 121 | 134 | +10.4% | -2.01 to 27.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,029,254 | 999,158 | -2.9% | -45,922 to -14,271 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.12 | +3.4% | -0.0105 to 0.0184 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 201 | +3.3% | -17 to 29.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.144 | 0.149 | +3.4% | -0.0132 to 0.023 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 10.9 | 9.36 | -14.0% | -8.62 to 5.58 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 985 | 985 | -0.0% | -6.66 to 6.12 | EVEN, no difference beyond the noise |
| queries a second | 985 | 985 | -0.0% | -6.66 to 6.12 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.27 | 2.34 | +2.9% | -1.36 to 1.49 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.01 | 5.1 | +1.9% | -3.45 to 3.64 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.25 | 1.26 | +0.7% | -0.425 to 0.442 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 169 | +31.8% | -88.7 to 170 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 119 | 151 | +27.8% | -83 to 149 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 415,831 | 387,856 | -6.7% | -114,553 to 58,603 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.228 | +23.7% | -0.286 to 0.373 | EVEN, no difference beyond the noise |
| host CPU-seconds | 289 | 357 | +23.9% | -451 to 589 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 73.3 | 83 | +13.3% | -169 to 188 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 2.93 to 14.4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
