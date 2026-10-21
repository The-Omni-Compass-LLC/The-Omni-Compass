# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 290 | -0.2% | -2.78 to 1.37 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 291 | -0.5% | -2.57 to -0.176 | LOSS |
| queries a second | 4,680 | 4,658 | -0.5% | -41.1 to -2.81 | LOSS |
| latency, 95th percentile (ms) | 3.73 | 3.53 | -5.3% | -0.37 to -0.0245 | GAIN |
| latency, 99th percentile (ms) | 17.2 | 6.14 | -64.3% | -59 to 36.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.02 | 2.17 | -28.0% | -3.88 to 2.19 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 380 | -25.8% | -335 to 70.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 441 | 321 | -27.3% | -262 to 21.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,172 | 291,691 | +19.5% | -33,425 to 128,461 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.163 | +0.0% | -0.00797 to 0.00807 | EVEN, no difference beyond the noise |
| host CPU-seconds | 99.5 | 99.6 | +0.1% | -5.2 to 5.35 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.23 | 2.23 | +0.3% | -0.0948 to 0.106 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | -1.5 to 8.84 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | +0.2% | -2.45 to 3.89 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.3% | -2.5 to 4.09 | EVEN, no difference beyond the noise |
| queries a second | 4,732 | 4,745 | +0.3% | -40 to 65.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.07 | 2.08 | +0.3% | -0.496 to 0.508 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.79 | 3.86 | +1.8% | -0.227 to 0.367 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.33 | 1.34 | +0.6% | -0.142 to 0.157 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 363 | -29.0% | -266 to -31.2 | GAIN |
| pages holding data, mean (MB) | 461 | 335 | -27.3% | -250 to -1.57 | GAIN |
| pages read from disk into the pool (misses) | 654,860 | 1,035,429 | +58.1% | 25,588 to 735,549 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.108 | +0.5% | -0.0128 to 0.0139 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 193 | +0.5% | -22.9 to 24.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.43 | 1.43 | +0.2% | -0.183 to 0.191 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 6.87 to 14.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 192 | -0.0% | -2.65 to 2.53 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 197 | +0.2% | -1.9 to 2.59 | EVEN, no difference beyond the noise |
| queries a second | 3,926 | 3,933 | +0.2% | -38 to 51.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.63 | 8.58 | -0.6% | -0.267 to 0.166 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.4 | 12.8 | +3.7% | 0.423 to 0.484 | LOSS |
| latency, mean (ms) | 5.41 | 5.37 | -0.7% | -0.257 to 0.179 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 553 | +8.1% | -80.4 to 163 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 491 | +6.2% | -52.6 to 110 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,238 | 537,107 | -12.7% | -303,156 to 146,894 | shown, not judged |
| host CPU busy (share of the run) | 0.222 | 0.217 | -1.9% | -0.0114 to 0.00287 | EVEN, no difference beyond the noise |
| host CPU-seconds | 357 | 350 | -1.8% | -19.1 to 5.97 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.05 | 3.98 | -1.8% | -0.267 to 0.118 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17.3 |  | 9.74 to 24.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,952 | 2,950 | -0.1% | -14.7 to 11.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,953 | -0.0% | -12.6 to 9.87 | EVEN, no difference beyond the noise |
| queries a second | 2,954 | 2,953 | -0.0% | -12.6 to 9.87 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.286 | 0.284 | -0.7% | -0.0433 to 0.0393 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.395 | 0.386 | -2.4% | -0.0359 to 0.0172 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.177 | 0.179 | +1.4% | -0.00793 to 0.0128 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 460 | -10.1% | -80.5 to -23.2 | GAIN |
| pages holding data, mean (MB) | 464 | 422 | -9.1% | -46.6 to -37.6 | GAIN |
| pages read from disk into the pool (misses) | 367,442 | 418,512 | +13.9% | 20,197 to 81,943 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.142 | +0.5% | -0.00606 to 0.00755 | EVEN, no difference beyond the noise |
| host CPU-seconds | 251 | 252 | +0.5% | -10.7 to 13.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.186 | 0.187 | +0.5% | -0.00867 to 0.0107 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 |  | 7.54 to 15.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| throughput (transactions a second) | 979 | 977 | -0.2% | -3.11 to -1.05 | LOSS |
| queries a second | 979 | 977 | -0.2% | -3.11 to -1.05 | LOSS |
| latency, 95th percentile (ms) | 2.27 | 2.25 | -0.8% | -0.449 to 0.412 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 42.9 | 17.9 | -58.3% | -168 to 118 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.31 | 2.91 | -12.3% | -4.35 to 3.54 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 515 | +0.6% | -51.9 to 58.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 445 | -1.7% | -77.1 to 61.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,939 | 193,645 | +2.0% | -42,427 to 49,838 | shown, not judged |
| host CPU busy (share of the run) | 0.207 | 0.208 | +0.4% | -0.0229 to 0.0247 | EVEN, no difference beyond the noise |
| host CPU-seconds | 368 | 371 | +0.7% | -36.1 to 41 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 368,497 | 370,953 | +0.7% | -36,053 to 40,967 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | -1.85 to 28.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
