# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 294 | +0.5% | -3.86 to 6.69 | no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.5% | -3.48 to 6.58 | no difference beyond the noise |
| queries a second | 4,684 | 4,708 | +0.5% | -55.7 to 105 | no difference beyond the noise |
| latency, 95th percentile (ms) | 3.7 | 3.66 | -1.2% | -0.519 to 0.431 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.09 | 5.09 | +0.0% | -0.396 to 0.396 | same |
| latency, mean (ms) | 1.63 | 1.61 | -1.5% | -0.145 to 0.0949 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 283 | -44.8% | -803 to 344 | no difference beyond the noise |
| pages holding data, mean (MB) | 439 | 253 | -42.3% | -692 to 321 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 168,778 | 278,789 | +65.2% | -155,047 to 375,069 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.117 | -2.4% | -0.0106 to 0.00489 | no difference beyond the noise |
| host CPU-seconds | 48.5 | 47.4 | -2.4% | -4.25 to 1.92 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.62 | 1.58 | -2.8% | -0.149 to 0.0579 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | -2.5 to 11.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.4% | -4.03 to 1.97 | no difference beyond the noise |
| throughput (transactions a second) | 293 | 292 | -0.2% | -3.7 to 2.26 | no difference beyond the noise |
| queries a second | 4,688 | 4,677 | -0.2% | -59.2 to 36.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 3.66 | 3.7 | +1.2% | -0.0511 to 0.14 | no difference beyond the noise |
| latency, 99th percentile (ms) | 4.94 | 5.09 | +3.1% | 0.0175 to 0.284 | **WORSE** |
| latency, mean (ms) | 2.72 | 2.77 | +1.5% | -0.0212 to 0.105 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 493 | -3.7% | -541 to 503 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 405 | -12.2% | -465 to 352 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 458,003 | 782,316 | +70.8% | 144,978 to 503,648 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.222 | +1.0% | -0.00208 to 0.00633 | no difference beyond the noise |
| host CPU-seconds | 265 | 267 | +0.9% | -2.66 to 7.66 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.94 | 2.98 | +1.3% | -0.0469 to 0.123 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 7.35 to 23.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 1.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 194 | +1.2% | -3.16 to 7.8 | no difference beyond the noise |
| throughput (transactions a second) | 194 | 196 | +0.8% | -0.445 to 3.68 | no difference beyond the noise |
| queries a second | 3,886 | 3,918 | +0.8% | -8.89 to 73.5 | no difference beyond the noise |
| latency, 95th percentile (ms) | 7.94 | 7.56 | -4.8% | -2.28 to 1.52 | no difference beyond the noise |
| latency, 99th percentile (ms) | 11.7 | 10.7 | -9.0% | -4.82 to 2.71 | no difference beyond the noise |
| latency, mean (ms) | 5.08 | 4.99 | -1.9% | -0.508 to 0.319 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 708 | +38.3% | -430 to 822 | no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 611 | +32.5% | -314 to 614 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 431,242 | 318,781 | -26.1% | -593,652 to 368,730 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.204 | -2.5% | -0.0346 to 0.0241 | no difference beyond the noise |
| host CPU-seconds | 226 | 221 | -2.5% | -37.5 to 26.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.85 | 3.71 | -3.6% | -0.769 to 0.489 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19.7 |  | 7.41 to 31.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,916 | 2,917 | +0.0% | -10.7 to 12.3 | no difference beyond the noise |
| throughput (transactions a second) | 2,928 | 2,929 | +0.0% | -11.2 to 12.8 | no difference beyond the noise |
| queries a second | 2,928 | 2,929 | +0.0% | -11.2 to 12.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.386 | 0.388 | +0.6% | -0.00771 to 0.0124 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.505 | 0.496 | -1.8% | -0.0314 to 0.0134 | no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.227 | +1.2% | -0.012 to 0.0174 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 362 | -29.3% | -553 to 252 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 337 | -27.1% | -498 to 248 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 262,404 | 396,278 | +51.0% | -240,072 to 507,820 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.127 | +0.9% | -0.00158 to 0.0038 | no difference beyond the noise |
| host CPU-seconds | 140 | 142 | +1.0% | -1.17 to 3.87 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.157 | 0.158 | +0.9% | -0.000709 to 0.00365 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | -2.37 to 17.7 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `23f6ca4cf9c8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1.38 | 2.28 | +65.2% | -1.43 to 3.23 | no difference beyond the noise |
| throughput (transactions a second) | 975 | 976 | +0.1% | -5.91 to 7.79 | no difference beyond the noise |
| queries a second | 975 | 976 | +0.1% | -5.91 to 7.79 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.8 | 1.84 | +2.3% | -0.518 to 0.6 | no difference beyond the noise |
| latency, 99th percentile (ms) | 2.96 | 3.19 | +8.1% | -0.869 to 1.35 | no difference beyond the noise |
| latency, mean (ms) | 1.11 | 1.12 | +1.0% | -0.163 to 0.185 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 615 | +20.0% | -162 to 367 | no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 500 | +11.3% | -105 to 207 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 138,795 | 123,169 | -11.3% | -40,290 to 9,038 | shown, not judged |
| host CPU busy (share of the run) | 0.151 | 0.181 | +19.7% | -0.133 to 0.193 | no difference beyond the noise |
| host CPU-seconds | 156 | 188 | +20.1% | -139 to 201 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 441 | 276 | -37.5% | -977 to 646 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 25.7 |  | 16.9 to 34.4 | shown, not judged |

Every omni arm handed back to the operator's pool size: NO; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
