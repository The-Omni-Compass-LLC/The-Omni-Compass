# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.3% | -6.63 to 4.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.4% | -6.58 to 4.26 | EVEN, no difference beyond the noise |
| queries a second | 4,715 | 4,696 | -0.4% | -105 to 68.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.5 | 5.54 | +0.6% | -0.347 to 0.415 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.89 | 7.84 | -0.6% | -0.253 to 0.157 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.32 | 3.33 | +0.4% | -0.0772 to 0.106 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 459 | -10.3% | -105 to -0.33 | GAIN |
| pages holding data, mean (MB) | 447 | 382 | -14.6% | -114 to -16.7 | GAIN |
| pages read from disk into the pool (misses) | 244,502 | 259,570 | +6.2% | -21,063 to 51,198 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.189 | +1.6% | 8.1e-06 to 0.0059 | power given |
| host CPU-seconds | 102 | 104 | +1.9% | 0.459 to 3.35 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.28 | 2.33 | +2.2% | 0.0109 to 0.0895 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 5.9 to 8.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 295 | -0.3% | -2.9 to 1.37 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.2% | -2.88 to 1.44 | EVEN, no difference beyond the noise |
| queries a second | 4,730 | 4,719 | -0.2% | -46.1 to 23.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.34 | 3.3 | -1.2% | -0.126 to 0.0461 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.41 | 4.38 | -0.6% | -0.138 to 0.0859 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.62 | 2.63 | +0.2% | -0.0554 to 0.0648 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 426 | -16.8% | -152 to -19.6 | GAIN |
| pages holding data, mean (MB) | 462 | 380 | -17.8% | -142 to -23 | GAIN |
| pages read from disk into the pool (misses) | 654,239 | 876,307 | +33.9% | 25,936 to 418,200 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.209 | +0.1% | -0.00567 to 0.00592 | EVEN, no difference beyond the noise |
| host CPU-seconds | 374 | 374 | +0.1% | -9.88 to 10.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.77 | 2.77 | +0.3% | -0.0479 to 0.0658 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17 |  | 12 to 22 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 197 | 197 | -0.2% | -1.14 to 0.164 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | +0.1% | -1.53 to 1.84 | EVEN, no difference beyond the noise |
| queries a second | 3,956 | 3,959 | +0.1% | -30.5 to 36.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.49 | 5.16 | +14.9% | 0.123 to 1.22 | LOSS |
| latency, 99th percentile (ms) | 7.3 | 9.31 | +27.5% | -4.05 to 8.06 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.58 | 2.76 | +6.9% | -0.0114 to 0.367 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 414 | -19.1% | -300 to 105 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 369 | -20.2% | -297 to 110 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 613,424 | 852,767 | +39.0% | -305,126 to 783,813 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.128 | +3.0% | -0.00293 to 0.0105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 228 | +3.0% | -4.97 to 18.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.46 | 2.54 | +3.3% | -0.0491 to 0.212 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 7.8 to 13.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,942 | 2,937 | -0.1% | -19.3 to 10.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,943 | 2,940 | -0.1% | -18.4 to 11.2 | EVEN, no difference beyond the noise |
| queries a second | 2,943 | 2,940 | -0.1% | -18.4 to 11.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.247 | 0.237 | -4.2% | -0.0334 to 0.0128 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.4 | 0.395 | -1.2% | -0.0312 to 0.0219 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.159 | 0.162 | +2.3% | -0.000501 to 0.0079 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 465 | -9.2% | -88.9 to -5.3 | GAIN |
| pages holding data, mean (MB) | 464 | 418 | -9.8% | -112 to 21.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 365,665 | 422,559 | +15.6% | -27,790 to 141,578 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.131 | +1.5% | 0.000131 to 0.00364 | power given |
| host CPU-seconds | 233 | 236 | +1.5% | 0.331 to 6.53 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.172 | 0.175 | +1.6% | 0.00132 to 0.00428 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 14 |  | 9.7 to 18.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.86 | 6.55 | -4.6% | -4.16 to 3.53 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 983 | +0.1% | -3.46 to 4.89 | EVEN, no difference beyond the noise |
| queries a second | 983 | 983 | +0.1% | -3.46 to 4.89 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.68 | 1.7 | +1.0% | -0.232 to 0.265 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.06 | 3.23 | +5.5% | 0.0414 to 0.296 | LOSS |
| latency, mean (ms) | 1.04 | 1.06 | +1.2% | -0.0546 to 0.0797 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -45.4 to 24.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 429 | -5.5% | -72.3 to 22.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,751 | 202,439 | +7.3% | -25,156 to 52,530 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.134 | +7.3% | -0.0543 to 0.0727 | EVEN, no difference beyond the noise |
| host CPU-seconds | 193 | 207 | +7.5% | -83.3 to 112 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 63.6 | 74.1 | +16.7% | -2.76 to 23.9 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 |  | 13.2 to 23.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
