# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.2% | -0.683 to 1.93 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.3% | -0.776 to 2.68 | EVEN, no difference beyond the noise |
| queries a second | 4,708 | 4,723 | +0.3% | -12.4 to 42.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.15 | 5.09 | -1.2% | -0.415 to 0.294 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.21 | 7.26 | +0.6% | -0.324 to 0.417 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.33 | 3.32 | -0.2% | -0.12 to 0.104 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 554 | +8.2% | 9.31 to 74.9 | power given |
| pages holding data, mean (MB) | 451 | 486 | +7.9% | 17.3 to 54.2 | power given |
| pages read from disk into the pool (misses) | 245,212 | 213,586 | -12.9% | -39,845 to -23,407 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.196 | +1.3% | -0.00784 to 0.013 | EVEN, no difference beyond the noise |
| host CPU-seconds | 107 | 108 | +1.5% | -4.31 to 7.47 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.38 | 2.41 | +1.3% | -0.099 to 0.16 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 5.9 to 8.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 293 | +0.8% | 1.43 to 2.96 | GAIN |
| throughput (transactions a second) | 295 | 296 | +0.5% | 0.37 to 2.34 | GAIN |
| queries a second | 4,720 | 4,742 | +0.5% | 5.93 to 37.5 | GAIN |
| latency, 95th percentile (ms) | 2.71 | 2.68 | -1.2% | -0.101 to 0.0368 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 27.6 | 21.3 | -22.8% | -36.7 to 24.1 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.14 | 2.86 | -8.9% | -1.7 to 1.14 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 515 | +0.5% | -311 to 316 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 448 | -3.0% | -266 to 239 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 649,743 | 688,285 | +5.9% | -715,340 to 792,424 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.161 | +0.8% | -0.000559 to 0.0032 | EVEN, no difference beyond the noise |
| host CPU-seconds | 286 | 288 | +0.8% | -1.26 to 5.99 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.16 | 2.16 | +0.1% | -0.0293 to 0.0318 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 7.46 to 13.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 192 | +0.6% | -0.41 to 2.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.2% | -0.475 to 1.37 | EVEN, no difference beyond the noise |
| queries a second | 3,913 | 3,922 | +0.2% | -9.5 to 27.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7 | 6.9 | -1.5% | -1.97 to 1.77 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 126 | 71.4 | -43.3% | -166 to 56.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7.71 | 6.21 | -19.4% | -6.01 to 3.02 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 522 | +2.0% | -309 to 330 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 457 | -0.8% | -259 to 251 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,694 | 660,359 | +7.4% | -506,599 to 597,930 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.176 | +0.6% | -0.0158 to 0.018 | EVEN, no difference beyond the noise |
| host CPU-seconds | 315 | 317 | +0.6% | -28.5 to 32.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.58 | 3.58 | +0.0% | -0.342 to 0.344 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 12.5 to 17.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,947 | -0.1% | -7.24 to 1.32 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,952 | -0.1% | -6.62 to 1.01 | EVEN, no difference beyond the noise |
| queries a second | 2,954 | 2,952 | -0.1% | -6.62 to 1.01 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.316 | -0.6% | -0.0106 to 0.00661 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.453 | 0.448 | -1.2% | -0.0168 to 0.00614 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.198 | 0.198 | +0.3% | -0.000748 to 0.00201 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 504 | -1.6% | -84.2 to 67.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 454 | -2.1% | -47.8 to 28 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,346 | 381,577 | +3.9% | -48,589 to 77,053 | shown, not judged |
| host CPU busy (share of the run) | 0.0946 | 0.0963 | +1.7% | -0.000468 to 0.00376 | EVEN, no difference beyond the noise |
| host CPU-seconds | 156 | 160 | +1.9% | -0.697 to 6.76 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.116 | 0.118 | +2.0% | -0.000231 to 0.00495 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | 6.03 to 16 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.63 | 6.32 | -4.7% | -8.2 to 7.58 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 983 | +0.0% | -2.01 to 2.75 | EVEN, no difference beyond the noise |
| queries a second | 983 | 983 | +0.0% | -2.01 to 2.75 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.67 | 1.83 | +9.6% | -0.156 to 0.476 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.88 | 3.51 | +21.9% | -0.667 to 1.93 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 1.12 | +5.8% | -0.037 to 0.159 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 534 | +4.3% | -73.9 to 118 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 454 | +0.1% | -88.5 to 89.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,677 | 192,914 | +1.7% | -37,719 to 44,194 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.218 | +72.0% | -0.0893 to 0.272 | EVEN, no difference beyond the noise |
| host CPU-seconds | 195 | 337 | +73.2% | -141 to 426 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 65.1 | 125 | +92.6% | -100 to 221 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 21 |  | 8.09 to 33.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
