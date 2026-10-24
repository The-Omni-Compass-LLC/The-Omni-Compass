# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.3% | -1.38 to 2.85 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.3% | -1.41 to 2.96 | EVEN, no difference beyond the noise |
| queries a second | 4,697 | 4,709 | +0.3% | -22.5 to 47.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.18 | 5.09 | -1.8% | -0.492 to 0.307 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.13 | 7.08 | -0.6% | -0.524 to 0.438 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.3 | 3.28 | -0.8% | -0.15 to 0.1 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 480 | -6.2% | -106 to 42.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 446 | 427 | -4.1% | -106 to 69 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,807 | 247,580 | +1.5% | -10,013 to 17,560 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.191 | +0.6% | -0.0213 to 0.0237 | EVEN, no difference beyond the noise |
| host CPU-seconds | 104 | 105 | +0.9% | -12.5 to 14.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.34 | +0.5% | -0.274 to 0.298 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 1.5 to 11.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.2% | -6.97 to 5.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.2% | -7.08 to 5.64 | EVEN, no difference beyond the noise |
| queries a second | 4,732 | 4,721 | -0.2% | -113 to 90.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.1 | 4.05 | -1.2% | -0.153 to 0.056 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.6 | -2.9% | -0.458 to 0.118 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.15 | 3.14 | -0.4% | -0.126 to 0.104 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -37.3 to 29.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 461 | -0.1% | -25.8 to 24.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,483 | 632,679 | -3.5% | -105,767 to 60,158 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.187 | +0.1% | -0.015 to 0.0155 | EVEN, no difference beyond the noise |
| host CPU-seconds | 309 | 310 | +0.2% | -24.9 to 26.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.29 | 2.3 | +0.5% | -0.131 to 0.152 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.7 |  | 6.94 to 24.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 192 | -0.5% | -3.63 to 1.61 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.4% | -3.72 to 2.18 | EVEN, no difference beyond the noise |
| queries a second | 3,933 | 3,918 | -0.4% | -74.3 to 43.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.28 | 8.38 | +1.2% | -0.835 to 1.04 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.3 | 12.4 | +0.6% | -1.07 to 1.22 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.28 | 5.25 | -0.5% | -0.153 to 0.0999 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 517 | +0.9% | -22.8 to 32.2 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 461 | -0.2% | -37.5 to 35.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,847 | 613,531 | -0.5% | -98,041 to 91,410 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.212 | -1.8% | -0.00722 to -0.000698 | GAIN |
| host CPU-seconds | 348 | 342 | -1.7% | -12.5 to 0.623 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.94 | 3.9 | -1.2% | -0.172 to 0.0783 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 11.8 to 17.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,959 | 2,961 | +0.1% | -21.1 to 26.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,965 | -0.0% | -13 to 12.1 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,965 | -0.0% | -13 to 12.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.214 | 0.227 | +5.8% | -0.0498 to 0.0745 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.365 | 0.361 | -1.3% | -0.0725 to 0.0632 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.664 | 0.156 | -76.5% | -2.78 to 1.76 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 415 | -18.9% | -204 to 11 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 380 | -18.0% | -191 to 24.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,230 | 486,955 | +32.6% | -7,863 to 247,314 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.118 | +4.8% | -0.0164 to 0.0272 | EVEN, no difference beyond the noise |
| host CPU-seconds | 201 | 210 | +4.8% | -29.3 to 48.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.149 | 0.156 | +4.7% | -0.023 to 0.0369 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | -3.87 to 18.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 233 | 223 | -4.4% | -137 to 117 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 987 | -0.1% | -7.58 to 5.21 | EVEN, no difference beyond the noise |
| queries a second | 988 | 987 | -0.1% | -7.58 to 5.21 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 45.6 | 51 | +11.9% | -151 to 162 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 154 | 169 | +9.4% | -196 to 225 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 8.01 | 9.85 | +23.0% | -19.2 to 22.9 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 355 | -30.6% | -267 to -46.6 | GAIN |
| pages holding data, mean (MB) | 452 | 298 | -34.2% | -251 to -57.8 | GAIN |
| pages read from disk into the pool (misses) | 190,326 | 294,747 | +54.9% | 43,111 to 165,730 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.14 | +2.0% | -0.0186 to 0.0241 | EVEN, no difference beyond the noise |
| host CPU-seconds | 242 | 247 | +2.0% | -32.7 to 42.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.34 | 2.49 | +6.2% | -1.36 to 1.65 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | 8.52 to 13.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
