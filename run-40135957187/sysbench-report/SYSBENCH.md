# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 291 | +0.0% | -4.75 to 4.89 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.0% | -4.13 to 3.87 | EVEN, no difference beyond the noise |
| queries a second | 4,719 | 4,717 | -0.0% | -66 to 62 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.06 | 5.88 | -2.9% | -0.737 to 0.38 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.69 | 8.58 | -1.2% | -0.692 to 0.486 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.49 | 3.48 | -0.4% | -0.109 to 0.0786 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 524 | +2.3% | -53.4 to 77.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 448 | 442 | -1.4% | -121 to 108 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 242,517 | 238,167 | -1.8% | -70,607 to 61,907 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.201 | +0.7% | -0.0129 to 0.0158 | EVEN, no difference beyond the noise |
| host CPU-seconds | 110 | 111 | +0.7% | -8.53 to 10.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.47 | 2.49 | +0.8% | -0.212 to 0.253 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 2.87 to 10.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 293 | -0.4% | -9.57 to 6.97 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.1% | -2.75 to 1.99 | EVEN, no difference beyond the noise |
| queries a second | 4,746 | 4,740 | -0.1% | -44 to 31.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.88 | 2.84 | -1.2% | -0.107 to 0.0392 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.45 | 37.1 | +580.0% | -108 to 171 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.71 | 4.49 | +66.0% | -7.56 to 11.1 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 492 | -3.9% | -127 to 87.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 440 | -4.6% | -150 to 107 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,608 | 691,621 | +5.8% | -219,445 to 295,471 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.173 | -0.9% | -0.00867 to 0.00559 | EVEN, no difference beyond the noise |
| host CPU-seconds | 314 | 312 | -0.9% | -15.4 to 9.82 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.34 | 2.33 | -0.5% | -0.0465 to 0.0251 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 10.9 to 18.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 192 | +1.1% | -0.832 to 4.88 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 197 | +0.5% | -1.06 to 2.93 | EVEN, no difference beyond the noise |
| queries a second | 3,923 | 3,942 | +0.5% | -21.2 to 58.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.18 | 8.58 | -6.4% | -1.12 to -0.0592 | GAIN |
| latency, 99th percentile (ms) | 13.5 | 12.8 | -4.7% | -1.01 to -0.254 | GAIN |
| latency, mean (ms) | 5.4 | 5.33 | -1.3% | -0.261 to 0.116 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 635 | +24.1% | 59.4 to 187 | power given |
| pages holding data, mean (MB) | 463 | 555 | +19.8% | 62.4 to 121 | power given |
| pages read from disk into the pool (misses) | 614,989 | 427,476 | -30.5% | -273,997 to -101,029 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.21 | -1.0% | -0.0081 to 0.00401 | EVEN, no difference beyond the noise |
| host CPU-seconds | 341 | 338 | -1.0% | -14.2 to 7.74 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.91 | 3.83 | -2.0% | -0.257 to 0.099 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19 |  | 9.06 to 28.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,961 | +0.0% | -6.27 to 7.55 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,962 | 2,964 | +0.0% | -5.5 to 8.06 | EVEN, no difference beyond the noise |
| queries a second | 2,962 | 2,964 | +0.0% | -5.5 to 8.06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.14 | 0.139 | -0.7% | -0.0358 to 0.0338 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.312 | 0.318 | +1.8% | -0.0195 to 0.0308 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0826 | 0.0852 | +3.2% | -0.00368 to 0.00897 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 487 | -4.8% | -97.4 to 48.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 445 | -4.0% | -80.3 to 43.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,647 | 382,182 | +4.0% | -70,443 to 99,512 | shown, not judged |
| host CPU busy (share of the run) | 0.0634 | 0.0654 | +3.2% | -0.00153 to 0.00555 | EVEN, no difference beyond the noise |
| host CPU-seconds | 114 | 117 | +3.2% | -2.74 to 10 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0842 | 0.0869 | +3.2% | -0.002 to 0.00733 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9 |  | 4.03 to 14 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 198 | +2.6% | -125 to 135 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 988 | -0.0% | -4.97 to 4.07 | EVEN, no difference beyond the noise |
| queries a second | 988 | 988 | -0.0% | -4.97 to 4.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 34.1 | 52.1 | +52.9% | -88.4 to 124 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 146 | 165 | +13.5% | -153 to 192 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7.07 | 9.23 | +30.5% | -11.7 to 16 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 455 | -11.2% | -256 to 142 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 387 | -14.6% | -280 to 147 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 190,211 | 236,794 | +24.5% | -78,021 to 171,188 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.136 | -0.8% | -0.0185 to 0.0162 | EVEN, no difference beyond the noise |
| host CPU-seconds | 243 | 241 | -0.7% | -31.6 to 28.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.89 | 2.68 | -7.3% | -2.59 to 2.17 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.7 |  | 11.2 to 14.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
