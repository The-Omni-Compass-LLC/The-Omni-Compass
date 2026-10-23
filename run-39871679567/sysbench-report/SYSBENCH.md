# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 296 | +0.4% | -3.41 to 5.72 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 297 | +0.4% | -3.93 to 6.18 | EVEN, no difference beyond the noise |
| queries a second | 4,726 | 4,744 | +0.4% | -62.8 to 98.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.02 | 3.04 | +0.6% | -0.293 to 0.328 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.57 | 4.55 | -0.6% | -0.338 to 0.288 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.46 | 1.47 | +0.7% | -0.0852 to 0.104 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 439 | -14.2% | -231 to 85.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 382 | -14.6% | -207 to 76.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 247,950 | 262,163 | +5.7% | -27,915 to 56,339 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.109 | +0.7% | -0.00797 to 0.00948 | EVEN, no difference beyond the noise |
| host CPU-seconds | 65.2 | 65.6 | +0.6% | -4.95 to 5.71 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.45 | 1.45 | +0.3% | -0.103 to 0.111 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | -0.2% | -4.2 to 3.13 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.1% | -3.83 to 3.38 | EVEN, no difference beyond the noise |
| queries a second | 4,707 | 4,704 | -0.1% | -61.3 to 54.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.21 | 3.17 | -1.2% | -0.203 to 0.127 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5 | 5.06 | +1.2% | -0.203 to 0.325 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.41 | 2.42 | +0.1% | -0.0753 to 0.0811 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 573 | +11.9% | -65.7 to 188 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 514 | +11.3% | -79.9 to 184 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 656,282 | 493,431 | -24.8% | -454,335 to 128,634 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.19 | -0.8% | -0.011 to 0.00796 | EVEN, no difference beyond the noise |
| host CPU-seconds | 347 | 344 | -0.8% | -19.7 to 14.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.57 | 2.55 | -0.6% | -0.121 to 0.089 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.7 |  | 7.68 to 23.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 196 | 196 | -0.3% | -3.19 to 1.85 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.2% | -2.57 to 1.92 | EVEN, no difference beyond the noise |
| queries a second | 3,948 | 3,941 | -0.2% | -51.4 to 38.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.18 | -0.7% | -0.743 to 0.671 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 9.01 | 9.39 | +4.3% | -0.802 to 1.57 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.85 | 2.9 | +1.9% | -0.371 to 0.478 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 555 | +8.4% | -174 to 260 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 487 | +5.3% | -106 to 155 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,656 | 585,734 | -5.0% | -300,623 to 238,778 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.131 | -3.9% | -0.0195 to 0.00889 | EVEN, no difference beyond the noise |
| host CPU-seconds | 242 | 232 | -3.9% | -34.4 to 15.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.7 | 2.61 | -3.5% | -0.406 to 0.215 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 |  | 7.94 to 25.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,917 | 2,909 | -0.3% | -61.2 to 44.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,935 | 2,933 | -0.1% | -8.43 to 4.68 | EVEN, no difference beyond the noise |
| queries a second | 2,935 | 2,933 | -0.1% | -8.43 to 4.68 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.281 | 0.278 | -1.1% | -0.0585 to 0.0525 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.549 | 0.625 | +13.8% | -0.36 to 0.512 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.275 | +39.8% | -0.275 to 0.431 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 525 | +2.6% | -65.6 to 92.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 463 | -0.0% | -97.7 to 97.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,627 | 354,102 | -3.7% | -147,333 to 120,284 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.138 | +0.3% | -0.00302 to 0.00389 | EVEN, no difference beyond the noise |
| host CPU-seconds | 248 | 249 | +0.4% | -5.43 to 7.29 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.185 | 0.186 | +0.7% | -0.00662 to 0.00908 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.7 |  | 1.19 to 24.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 10.5 | 7.54 | -28.0% | -8.92 to 3.06 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 984 | +0.0% | -12.7 to 13.3 | EVEN, no difference beyond the noise |
| queries a second | 984 | 984 | +0.0% | -12.7 to 13.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.73 | 1.74 | +0.4% | -0.432 to 0.446 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.54 | 4.57 | +0.6% | -0.49 to 0.542 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.08 | 1.09 | +0.8% | -0.0952 to 0.113 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 585 | +14.2% | -167 to 313 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 475 | +4.8% | -92.9 to 137 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,426 | 178,835 | -5.6% | -50,905 to 29,723 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.121 | +3.8% | -0.0417 to 0.0507 | EVEN, no difference beyond the noise |
| host CPU-seconds | 180 | 187 | +3.8% | -63.8 to 77.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 42 | 57.1 | +35.8% | -11.9 to 42.1 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 |  | 6.63 to 26.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
