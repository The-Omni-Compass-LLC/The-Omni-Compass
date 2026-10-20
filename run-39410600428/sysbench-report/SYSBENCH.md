# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 287 | 289 | +0.7% | -22.2 to 26.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 294 | -0.4% | -8.17 to 5.96 | EVEN, no difference beyond the noise |
| queries a second | 4,728 | 4,711 | -0.4% | -131 to 95.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.52 | 4.08 | -37.5% | -13.9 to 9.03 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 46.1 | 29.7 | -35.6% | -170 to 138 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.54 | 2.95 | -16.9% | -4.87 to 3.67 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 351 | -31.5% | -280 to -42.5 | GAIN |
| pages holding data, mean (MB) | 446 | 295 | -33.9% | -233 to -68.9 | GAIN |
| pages read from disk into the pool (misses) | 246,962 | 299,890 | +21.4% | -35,248 to 141,103 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.165 | +0.2% | -0.00522 to 0.00588 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98.7 | 98.9 | +0.2% | -3.03 to 3.47 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.25 | 2.24 | -0.5% | -0.204 to 0.179 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.0% | -4.73 to 4.69 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.0% | -4.62 to 4.73 | EVEN, no difference beyond the noise |
| queries a second | 4,724 | 4,725 | +0.0% | -73.9 to 75.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.03 | 3.96 | -1.8% | -0.252 to 0.108 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.6 | -1.8% | -0.355 to 0.152 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.03 | 3.01 | -0.8% | -0.0828 to 0.0372 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 495 | -3.4% | -115 to 80.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 446 | -3.5% | -84.9 to 52.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,207 | 664,503 | +1.4% | -210,202 to 228,794 | shown, not judged |
| host CPU busy (share of the run) | 0.239 | 0.238 | -0.6% | -0.0104 to 0.00744 | EVEN, no difference beyond the noise |
| host CPU-seconds | 425 | 423 | -0.6% | -18.5 to 13.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.15 | 3.13 | -0.6% | -0.0887 to 0.0498 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 |  | 10.4 to 22.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | +0.1% | -0.441 to 0.869 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.4% | -0.304 to 1.84 | EVEN, no difference beyond the noise |
| queries a second | 3,936 | 3,951 | +0.4% | -6.07 to 36.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.33 | 8.43 | +1.2% | -0.478 to 0.681 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.4 | 12.8 | +3.0% | -1.02 to 1.77 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.28 | 5.3 | +0.4% | -0.00971 to 0.0507 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 528 | +3.1% | 5.84 to 26 | power given |
| pages holding data, mean (MB) | 462 | 472 | +2.2% | -4.62 to 24.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,658 | 586,919 | -4.8% | -125,453 to 65,974 | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.214 | +0.0% | -0.00583 to 0.00591 | EVEN, no difference beyond the noise |
| host CPU-seconds | 344 | 344 | +0.1% | -9.3 to 9.87 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.89 | 3.89 | -0.0% | -0.1 to 0.0988 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 4.99 to 25.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,963 | 2,960 | -0.1% | -10.6 to 4.64 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,966 | 2,964 | -0.1% | -13.4 to 9.67 | EVEN, no difference beyond the noise |
| queries a second | 2,966 | 2,964 | -0.1% | -13.4 to 9.67 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.218 | 0.215 | -1.2% | -0.0234 to 0.018 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.352 | 0.352 | -0.1% | -0.0165 to 0.0158 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.169 | 0.179 | +5.8% | -0.0636 to 0.0833 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 401 | -21.7% | -236 to 13.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 366 | -20.9% | -195 to 1.16 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,194 | 501,193 | +36.5% | -54,068 to 322,066 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.115 | +1.7% | -0.00443 to 0.00833 | EVEN, no difference beyond the noise |
| host CPU-seconds | 201 | 205 | +1.7% | -7.83 to 14.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.149 | 0.152 | +1.8% | -0.00603 to 0.0114 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | -6.15 to 20.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| throughput (transactions a second) | 978 | 977 | -0.2% | -6.93 to 3.86 | EVEN, no difference beyond the noise |
| queries a second | 978 | 977 | -0.2% | -6.93 to 3.86 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.98 | 1.94 | -2.0% | -0.353 to 0.275 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.93 | 2.79 | -4.5% | -1.22 to 0.956 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.33 | -1.1% | -0.15 to 0.12 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 508 | -0.9% | -125 to 116 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 433 | -4.6% | -120 to 78 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 187,713 | 196,930 | +4.9% | -44,325 to 62,758 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.209 | -1.6% | -0.0246 to 0.0177 | EVEN, no difference beyond the noise |
| host CPU-seconds | 378 | 372 | -1.6% | -43.4 to 31.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 377,930 | 371,950 | -1.6% | -43,408 to 31,448 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19 |  | 11.5 to 26.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
