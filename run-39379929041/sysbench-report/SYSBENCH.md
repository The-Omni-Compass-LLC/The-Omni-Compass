# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.4% | -3.73 to 6.29 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 295 | +0.6% | -2.79 to 6.15 | EVEN, no difference beyond the noise |
| queries a second | 4,689 | 4,716 | +0.6% | -44.6 to 98.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.31 | 5.25 | -1.2% | -0.2 to 0.073 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.34 | 7.57 | +3.0% | 0.0329 to 0.414 | LOSS |
| latency, mean (ms) | 3.33 | 3.34 | +0.3% | -0.0368 to 0.0551 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 460 | -10.1% | -143 to 39.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 393 | -12.1% | -154 to 46.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,509 | 262,187 | +7.7% | -54,511 to 91,869 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.196 | +1.6% | -0.00496 to 0.0111 | EVEN, no difference beyond the noise |
| host CPU-seconds | 106 | 108 | +1.7% | -3.29 to 6.82 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.38 | 2.41 | +1.3% | -0.0432 to 0.107 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 |  | 4.54 to 12.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.0% | -1.05 to 1.02 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | +0.0% | -1.04 to 1.06 | EVEN, no difference beyond the noise |
| queries a second | 4,730 | 4,730 | +0.0% | -16.7 to 17 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.88 | 1.93 | +2.5% | -0.17 to 0.263 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.64 | 3.66 | +0.7% | -0.723 to 0.773 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.28 | 1.3 | +1.6% | -0.0192 to 0.0608 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 362 | -29.3% | -227 to -73.4 | GAIN |
| pages holding data, mean (MB) | 462 | 334 | -27.7% | -215 to -40.6 | GAIN |
| pages read from disk into the pool (misses) | 655,755 | 1,048,015 | +59.8% | 178,493 to 606,027 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.104 | +2.3% | -0.00493 to 0.00955 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 187 | +2.3% | -8.71 to 17 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.36 | 1.39 | +2.2% | -0.0684 to 0.129 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 |  | 0.131 to 22.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 191 | -0.8% | -6.04 to 2.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.7% | -3.19 to 0.45 | EVEN, no difference beyond the noise |
| queries a second | 3,959 | 3,932 | -0.7% | -63.9 to 9.01 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.74 | 7.11 | +5.5% | -3.14 to 3.89 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 22.5 | 26.5 | +17.6% | -30.5 to 38.4 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.54 | 3.74 | +5.5% | -1.23 to 1.62 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 435 | -15.1% | -119 to -35.9 | GAIN |
| pages holding data, mean (MB) | 462 | 392 | -15.1% | -109 to -30 | GAIN |
| pages read from disk into the pool (misses) | 618,586 | 811,497 | +31.2% | 125,951 to 259,871 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.138 | +3.4% | -0.00239 to 0.0115 | EVEN, no difference beyond the noise |
| host CPU-seconds | 237 | 245 | +3.4% | -4.14 to 20.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.7 | 2.81 | +4.2% | 0.0386 to 0.19 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 |  | 7.54 to 15.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,955 | 2,949 | -0.2% | -23.7 to 11.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,962 | 2,961 | -0.0% | -16.7 to 14.1 | EVEN, no difference beyond the noise |
| queries a second | 2,962 | 2,961 | -0.0% | -16.7 to 14.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.214 | 0.212 | -1.2% | -0.0141 to 0.00881 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.363 | 0.365 | +0.6% | -0.0232 to 0.0272 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.353 | +77.0% | -0.305 to 0.613 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 428 | -16.5% | -168 to -0.273 | GAIN |
| pages holding data, mean (MB) | 464 | 391 | -15.6% | -146 to 1.04 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 365,322 | 461,733 | +26.4% | -21,967 to 214,789 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.111 | +0.3% | -0.00184 to 0.00243 | EVEN, no difference beyond the noise |
| host CPU-seconds | 198 | 198 | +0.3% | -3.27 to 4.36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.147 | +0.4% | -0.00214 to 0.00336 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 |  | 2.6 to 14.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 204 | 246 | +20.5% | -114 to 198 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 988 | -0.0% | -6.41 to 5.64 | EVEN, no difference beyond the noise |
| queries a second | 988 | 988 | -0.0% | -6.41 to 5.64 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.87 | 2.7 | -6.1% | -1.13 to 0.783 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.56 | 5.31 | -19.0% | -7.05 to 4.56 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.08 | 1.02 | -5.7% | -0.376 to 0.252 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 450 | -12.1% | -100 to -23.4 | GAIN |
| pages holding data, mean (MB) | 452 | 380 | -15.9% | -83 to -61.1 | GAIN |
| pages read from disk into the pool (misses) | 189,515 | 230,352 | +21.5% | 13,778 to 67,896 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.119 | -3.4% | -0.0282 to 0.0199 | EVEN, no difference beyond the noise |
| host CPU-seconds | 217 | 210 | -3.3% | -49.3 to 34.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.4 | 1.99 | -17.3% | -2.53 to 1.7 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 |  | 7.94 to 25.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
