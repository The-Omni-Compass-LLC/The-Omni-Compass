# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 296 | +0.2% | 0.158 to 1.03 | GAIN |
| throughput (transactions a second) | 296 | 296 | +0.3% | 0.506 to 0.989 | GAIN |
| queries a second | 4,730 | 4,742 | +0.3% | 8.1 to 15.8 | GAIN |
| latency, 95th percentile (ms) | 2.9 | 2.86 | -1.2% | -0.109 to 0.04 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.49 | 4.6 | +2.4% | -0.196 to 0.41 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.38 | +1.6% | -0.0979 to 0.142 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 403 | -21.2% | -344 to 127 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 444 | 356 | -19.7% | -310 to 134 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 242,730 | 285,543 | +17.6% | -57,645 to 143,271 | shown, not judged |
| host CPU busy (share of the run) | 0.099 | 0.1 | +1.2% | -0.00266 to 0.00507 | EVEN, no difference beyond the noise |
| host CPU-seconds | 59.4 | 60.1 | +1.2% | -1.6 to 3.02 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.32 | 1.34 | +1.0% | -0.0361 to 0.0625 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | -1.4 to 10.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.2% | -3.83 to 2.92 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.2% | -3.96 to 3.06 | EVEN, no difference beyond the noise |
| queries a second | 4,715 | 4,708 | -0.2% | -63.4 to 48.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.15 | 4.05 | -2.4% | -0.205 to 0.0075 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.5 | -1.8% | -0.344 to 0.145 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.21 | 3.17 | -1.1% | -0.107 to 0.035 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 549 | +7.2% | -55.8 to 130 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 492 | +6.6% | -57.3 to 118 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,463 | 538,468 | -17.7% | -350,840 to 118,850 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.191 | -1.3% | -0.0126 to 0.00754 | EVEN, no difference beyond the noise |
| host CPU-seconds | 320 | 316 | -1.3% | -21.1 to 12.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.37 | 2.35 | -1.1% | -0.126 to 0.0724 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 5.13 to 27.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 197 | 195 | -0.7% | -4.61 to 1.84 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | -0.3% | -3.09 to 1.91 | EVEN, no difference beyond the noise |
| queries a second | 3,965 | 3,954 | -0.3% | -61.9 to 38.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.8 | 5.34 | +11.4% | 0.332 to 0.761 | LOSS |
| latency, 99th percentile (ms) | 9.48 | 12.3 | +30.1% | -0.896 to 6.61 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.65 | 2.86 | +7.8% | 0.19 to 0.225 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 398 | -22.2% | -183 to -44.4 | GAIN |
| pages holding data, mean (MB) | 462 | 359 | -22.4% | -178 to -29.3 | GAIN |
| pages read from disk into the pool (misses) | 617,540 | 873,710 | +41.5% | 169,482 to 342,858 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.124 | +2.7% | -0.000131 to 0.00657 | EVEN, no difference beyond the noise |
| host CPU-seconds | 215 | 221 | +2.7% | -0.19 to 11.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.4 | 2.48 | +3.4% | 0.0541 to 0.11 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | -5.15 to 21.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,948 | -0.0% | -5.68 to 3.5 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,955 | 2,954 | -0.0% | -2.68 to 1.82 | EVEN, no difference beyond the noise |
| queries a second | 2,955 | 2,954 | -0.0% | -2.68 to 1.82 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.334 | 0.328 | -1.8% | -0.0743 to 0.0623 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.443 | -3.0% | -0.0757 to 0.0484 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.204 | +0.2% | -0.0303 to 0.0309 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 437 | -14.6% | -170 to 20.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 394 | -15.0% | -145 to 5.29 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,361 | 473,934 | +29.0% | -76,862 to 290,007 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.102 | -1.5% | -0.0308 to 0.0277 | EVEN, no difference beyond the noise |
| host CPU-seconds | 171 | 169 | -1.4% | -51.6 to 46.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.127 | 0.125 | -1.4% | -0.0384 to 0.0349 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13 |  | 6.43 to 19.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.76 | 6.23 | -7.9% | -8.86 to 7.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 983 | -0.0% | -1.8 to 1.46 | EVEN, no difference beyond the noise |
| queries a second | 983 | 983 | -0.0% | -1.8 to 1.46 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.84 | 1.86 | +1.4% | -0.224 to 0.274 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.67 | 3.77 | +2.9% | -0.229 to 0.445 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.08 | 1.3 | +20.1% | -0.771 to 1.21 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 515 | +0.5% | -116 to 121 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 428 | -5.5% | -108 to 58.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,581 | 204,771 | +8.6% | -15,663 to 48,043 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.16 | +28.7% | -0.0792 to 0.151 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 247 | +29.2% | -125 to 237 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 85.6 | 97.5 | +14.0% | -104 to 128 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 21.3 |  | 11 to 31.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
