# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | -0.0% | -4.49 to 4.34 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.0% | -4.78 to 4.94 | EVEN, no difference beyond the noise |
| queries a second | 4,707 | 4,709 | +0.0% | -76.5 to 79.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.25 | 5.12 | -2.4% | -0.259 to 0.00945 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.34 | 7.39 | +0.6% | -0.146 to 0.235 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.38 | 3.36 | -0.5% | -0.0316 to 0.000829 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 499 | -2.6% | -99.2 to 72.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 448 | 436 | -2.7% | -88 to 63.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,782 | 235,870 | -3.2% | -45,673 to 29,849 | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.201 | +1.5% | -0.000492 to 0.00639 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 111 | +1.8% | -0.342 to 4.29 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.43 | 2.48 | +1.8% | -0.0398 to 0.128 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 4.87 to 12.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | -0.0% | -3.83 to 3.69 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.0% | -3.91 to 3.63 | EVEN, no difference beyond the noise |
| queries a second | 4,714 | 4,712 | -0.0% | -62.6 to 58.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.18 | 4.08 | -2.4% | -0.204 to 0.00537 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.06 | 5.84 | -3.5% | -0.481 to 0.0512 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.17 | 3.14 | -0.8% | -0.0385 to -0.00966 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 498 | -2.8% | -69.1 to 40.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 447 | -3.2% | -50.1 to 21 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,094 | 646,584 | -1.3% | -82,452 to 65,433 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.186 | -0.5% | -0.00317 to 0.00146 | EVEN, no difference beyond the noise |
| host CPU-seconds | 309 | 307 | -0.4% | -5.08 to 2.61 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.29 | 2.28 | -0.4% | -0.0201 to 0.00325 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 |  | 12.4 to 24.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | -0.3% | -3.48 to 2.48 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.4% | -2.44 to 0.772 | EVEN, no difference beyond the noise |
| queries a second | 3,939 | 3,922 | -0.4% | -48.9 to 15.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.13 | 8.08 | -0.6% | -0.81 to 0.71 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.2 | 11.8 | -2.9% | -2.08 to 1.37 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.22 | 5.13 | -1.8% | -0.485 to 0.297 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 527 | +2.9% | -85.4 to 116 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 469 | +1.4% | -63 to 76 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,440 | 596,237 | -3.0% | -175,700 to 139,296 | shown, not judged |
| host CPU busy (share of the run) | 0.213 | 0.207 | -3.1% | -0.0336 to 0.0202 | EVEN, no difference beyond the noise |
| host CPU-seconds | 343 | 333 | -3.0% | -53.8 to 33 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.88 | 3.77 | -2.8% | -0.616 to 0.401 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18 |  | 9.39 to 26.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,943 | 2,941 | -0.1% | -14.2 to 10.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,953 | +0.0% | -8.3 to 8.45 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,953 | +0.0% | -8.3 to 8.45 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.361 | 0.363 | +0.6% | -0.0232 to 0.0272 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.499 | 0.506 | +1.3% | -0.0485 to 0.0618 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.225 | +3.9% | -0.0133 to 0.0303 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 490 | -4.4% | -47.6 to 2.72 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 444 | -4.2% | -33.8 to -4.97 | GAIN |
| pages read from disk into the pool (misses) | 367,354 | 387,737 | +5.5% | -32,033 to 72,799 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.119 | +4.7% | -0.00806 to 0.0187 | EVEN, no difference beyond the noise |
| host CPU-seconds | 188 | 197 | +4.8% | -13.3 to 31.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.14 | 0.146 | +4.9% | -0.01 to 0.0236 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 10.9 to 13.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0.738 | 0.756 | +2.5% | -1.74 to 1.78 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 982 | 984 | +0.2% | -1.47 to 4.49 | EVEN, no difference beyond the noise |
| queries a second | 982 | 984 | +0.2% | -1.47 to 4.49 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.14 | 1.82 | -14.7% | -0.854 to 0.226 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.3 | 4.8 | -9.3% | -2.85 to 1.86 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.16 | -7.1% | -0.353 to 0.177 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 499 | -2.5% | -69.9 to 44.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 429 | -5.4% | -71 to 21.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,980 | 200,777 | +6.2% | -27,118 to 50,712 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.133 | -8.7% | -0.0457 to 0.0204 | EVEN, no difference beyond the noise |
| host CPU-seconds | 223 | 204 | -8.5% | -68.7 to 30.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 810 | 721 | -11.0% | -2,083 to 1,905 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 13.5 to 18.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
