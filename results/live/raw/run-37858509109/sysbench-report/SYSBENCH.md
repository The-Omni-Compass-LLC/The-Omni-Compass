# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.6% | -5.12 to 1.86 | no difference beyond the noise |
| throughput (transactions a second) | 294 | 292 | -0.6% | -4.71 to 0.994 | no difference beyond the noise |
| queries a second | 4,699 | 4,669 | -0.6% | -75.4 to 15.9 | no difference beyond the noise |
| latency, 95th percentile (ms) | 3.37 | 3.19 | -5.3% | -0.194 to -0.16 | better |
| latency, 99th percentile (ms) | 4.82 | 4.43 | -8.1% | -0.701 to -0.0772 | better |
| latency, mean (ms) | 1.51 | 1.5 | -0.8% | -0.0849 to 0.0601 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 262 | -48.9% | -371 to -129 | better |
| pages holding data, mean (MB) | 440 | 213 | -51.5% | -296 to -157 | better |
| pages read from disk into the pool (misses) | 168,336 | 274,614 | +63.1% | 56,688 to 155,868 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.112 | +0.3% | -0.00546 to 0.00609 | no difference beyond the noise |
| host CPU-seconds | 45.2 | 45.3 | +0.2% | -2.36 to 2.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.51 | 1.52 | +0.8% | -0.0643 to 0.0894 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | 1.46 to 7.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.3% | -2.13 to 4.18 | no difference beyond the noise |
| throughput (transactions a second) | 292 | 293 | +0.3% | -2.11 to 4.1 | no difference beyond the noise |
| queries a second | 4,677 | 4,693 | +0.3% | -33.8 to 65.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 4.35 | 4.25 | -2.4% | -0.211 to 0.00563 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.88 | 5.81 | -1.2% | -0.223 to 0.0814 | no difference beyond the noise |
| latency, mean (ms) | 3.24 | 3.21 | -0.9% | -0.0871 to 0.0303 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 516 | +0.8% | -185 to 193 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 458 | -0.7% | -159 to 152 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 455,778 | 514,876 | +13.0% | -174,277 to 292,472 | shown, not judged |
| host CPU busy (share of the run) | 0.2 | 0.2 | +0.1% | -0.00903 to 0.00936 | no difference beyond the noise |
| host CPU-seconds | 222 | 223 | +0.2% | -10.5 to 11.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.48 | 2.47 | -0.1% | -0.109 to 0.103 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 10.7 to 19.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 125 | 127 | +1.8% | -77 to 81.3 | no difference beyond the noise |
| throughput (transactions a second) | 195 | 196 | +0.6% | -1.74 to 4.23 | no difference beyond the noise |
| queries a second | 3,893 | 3,918 | +0.6% | -34.9 to 84.7 | no difference beyond the noise |
| latency, 95th percentile (ms) | 189 | 192 | +1.7% | -271 to 278 | no difference beyond the noise |
| latency, 99th percentile (ms) | 440 | 542 | +23.1% | -447 to 651 | no difference beyond the noise |
| latency, mean (ms) | 40.2 | 44.6 | +11.0% | -64.2 to 73.1 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 833 | +62.6% | -11.1 to 652 | no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 662 | +43.7% | 85.6 to 317 | **WORSE** |
| pages read from disk into the pool (misses) | 430,616 | 259,436 | -39.8% | -295,264 to -47,097 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.185 | -4.1% | -0.0149 to -0.000826 | better |
| host CPU-seconds | 232 | 222 | -4.2% | -16.3 to -3.02 | better |
| host CPU-seconds per 1,000 transactions inside the line | 6.07 | 5.83 | -3.9% | -3.52 to 3.04 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19.7 |  | 15.9 to 23.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,920 | 2,924 | +0.1% | -1.63 to 7.77 | no difference beyond the noise |
| throughput (transactions a second) | 2,928 | 2,929 | +0.0% | -6.22 to 8.77 | no difference beyond the noise |
| queries a second | 2,928 | 2,929 | +0.0% | -6.22 to 8.77 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.374 | 0.359 | -4.2% | -0.0707 to 0.0393 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.474 | 0.453 | -4.4% | -0.114 to 0.0715 | no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.2 | -2.9% | -0.037 to 0.0249 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 575 | +12.2% | -379 to 505 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 499 | +7.9% | -284 to 357 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 262,671 | 242,790 | -7.6% | -259,721 to 219,958 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.1 | -5.0% | -0.0323 to 0.0217 | no difference beyond the noise |
| host CPU-seconds | 117 | 111 | -5.0% | -36.2 to 24.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.131 | 0.124 | -5.1% | -0.0407 to 0.0274 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 1.43 to 14.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0.0311 | 0.0331 | +6.4% | -0.0355 to 0.0395 | no difference beyond the noise |
| throughput (transactions a second) | 911 | 899 | -1.2% | -167 to 145 | no difference beyond the noise |
| queries a second | 911 | 899 | -1.2% | -167 to 145 | no difference beyond the noise |
| latency, 95th percentile (ms) | 2,365 | 2,357 | -0.4% | -6,635 to 6,618 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3,665 | 3,867 | +5.5% | -8,601 to 9,005 | no difference beyond the noise |
| latency, mean (ms) | 459 | 391 | -14.8% | -896 to 760 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 452 | -11.7% | -356 to 237 | no difference beyond the noise |
| pages holding data, mean (MB) | 452 | 363 | -19.7% | -271 to 92.6 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 130,203 | 167,578 | +28.7% | -41,004 to 115,754 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.135 | -1.9% | -0.035 to 0.0299 | no difference beyond the noise |
| host CPU-seconds | 168 | 166 | -1.3% | -40 to 35.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 21,973 | 20,701 | -5.8% | -19,416 to 16,873 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | -0.208 to 32.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
