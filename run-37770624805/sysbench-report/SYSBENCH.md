# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 288 | 290 | +0.8% | -7.95 to 12.3 | no difference beyond the noise |
| throughput (transactions a second) | 291 | 292 | +0.2% | -4.93 to 5.87 | no difference beyond the noise |
| queries a second | 4,657 | 4,664 | +0.2% | -78.9 to 93.9 | no difference beyond the noise |
| latency, 95th percentile (ms) | 6.17 | 5.99 | -3.0% | -1.02 to 0.657 | no difference beyond the noise |
| latency, 99th percentile (ms) | 8.86 | 7.71 | -13.1% | -4.91 to 2.6 | no difference beyond the noise |
| latency, mean (ms) | 3.62 | 3.53 | -2.4% | -0.437 to 0.26 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 171 | -66.7% | -343 to -340 | better |
| pages holding data, mean (MB) | 438 | 146 | -66.7% | -316 to -269 | better |
| pages read from disk into the pool (misses) | 167,269 | 337,934 | +102.0% | 163,348 to 177,982 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.209 | -1.5% | -0.0214 to 0.0152 | no difference beyond the noise |
| host CPU-seconds | 78.7 | 77.8 | -1.1% | -8.1 to 6.34 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.65 | 2.61 | -1.9% | -0.385 to 0.286 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 291 | +0.2% | -0.668 to 1.6 | no difference beyond the noise |
| throughput (transactions a second) | 291 | 291 | +0.2% | -0.665 to 1.64 | no difference beyond the noise |
| queries a second | 4,653 | 4,661 | +0.2% | -10.6 to 26.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 3.13 | 3.23 | +3.0% | -0.201 to 0.392 | no difference beyond the noise |
| latency, 99th percentile (ms) | 4.33 | 4.35 | +0.6% | -0.27 to 0.318 | no difference beyond the noise |
| latency, mean (ms) | 2.33 | 2.37 | +1.5% | -0.105 to 0.175 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 248 | -51.7% | -469 to -59.6 | better |
| pages holding data, mean (MB) | 462 | 232 | -49.7% | -435 to -24 | better |
| pages read from disk into the pool (misses) | 457,414 | 1,018,254 | +122.6% | 231,021 to 890,657 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.196 | +1.3% | -0.00857 to 0.0137 | no difference beyond the noise |
| host CPU-seconds | 236 | 239 | +1.3% | -10.4 to 16.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.62 | 2.65 | +1.1% | -0.127 to 0.187 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 189 | 190 | +0.5% | -0.956 to 3.01 | no difference beyond the noise |
| throughput (transactions a second) | 196 | 194 | -0.6% | -3.62 to 1.28 | no difference beyond the noise |
| queries a second | 3,910 | 3,887 | -0.6% | -72.4 to 25.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 9.51 | 8.44 | -11.3% | -2.53 to 0.375 | no difference beyond the noise |
| latency, 99th percentile (ms) | 14.7 | 14.8 | +0.3% | -5.53 to 5.61 | no difference beyond the noise |
| latency, mean (ms) | 5.69 | 5.6 | -1.5% | -0.7 to 0.53 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 917 | +79.2% | 119 to 692 | **WORSE** |
| pages holding data, mean (MB) | 463 | 789 | +70.4% | 188 to 464 | **WORSE** |
| pages read from disk into the pool (misses) | 435,307 | 239,067 | -45.1% | -268,345 to -124,136 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.215 | -5.3% | -0.027 to 0.00271 | no difference beyond the noise |
| host CPU-seconds | 246 | 234 | -5.2% | -29.3 to 3.55 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.23 | 3.99 | -5.7% | -0.564 to 0.0776 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 24.7 |  | 18.9 to 30.4 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,920 | 2,914 | -0.2% | -19.9 to 7.2 | no difference beyond the noise |
| throughput (transactions a second) | 2,929 | 2,927 | -0.1% | -10.9 to 6.35 | no difference beyond the noise |
| queries a second | 2,929 | 2,927 | -0.1% | -10.9 to 6.35 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.372 | 0.395 | +6.2% | -0.0195 to 0.0655 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.49 | 0.508 | +3.7% | -0.0267 to 0.0627 | no difference beyond the noise |
| latency, mean (ms) | 0.219 | 0.241 | +10.4% | -0.046 to 0.0915 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 628 | +22.6% | -655 to 886 | no difference beyond the noise |
| pages holding data, mean (MB) | 468 | 519 | +10.8% | -436 to 536 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 264,686 | 281,205 | +6.2% | -211,725 to 244,763 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.122 | +2.4% | -0.021 to 0.0268 | no difference beyond the noise |
| host CPU-seconds | 132 | 135 | +2.4% | -23.4 to 29.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.151 | +2.6% | -0.0264 to 0.0342 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | 1.17 to 22.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 1.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `a033fd09b6d5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1.44 | 1.41 | -1.8% | -0.513 to 0.46 | no difference beyond the noise |
| throughput (transactions a second) | 973 | 975 | +0.2% | -0.337 to 4.21 | no difference beyond the noise |
| queries a second | 973 | 975 | +0.2% | -0.337 to 4.21 | no difference beyond the noise |
| latency, 95th percentile (ms) | 2.23 | 2.08 | -6.5% | -0.46 to 0.17 | no difference beyond the noise |
| latency, 99th percentile (ms) | 13.1 | 4.15 | -68.3% | -43.6 to 25.7 | no difference beyond the noise |
| latency, mean (ms) | 1.66 | 1.19 | -27.9% | -1.52 to 0.601 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 562 | +9.8% | -130 to 231 | no difference beyond the noise |
| pages holding data, mean (MB) | 451 | 470 | +4.3% | -149 to 188 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 139,229 | 143,196 | +2.8% | -42,329 to 50,264 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.139 | -1.1% | -0.0304 to 0.0271 | no difference beyond the noise |
| host CPU-seconds | 146 | 144 | -1.2% | -31.4 to 27.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 350 | 338 | -3.6% | -150 to 125 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 24.3 |  | 10.7 to 38 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
