# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.0% | -1.34 to 1.58 | no difference beyond the noise |
| throughput (transactions a second) | 292 | 292 | +0.0% | -1 to 1 | no difference beyond the noise |
| queries a second | 4,676 | 4,676 | +0.0% | -16 to 16.1 | no difference beyond the noise |
| latency, 95th percentile (ms) | 3.39 | 3.33 | -1.8% | -0.207 to 0.0885 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.09 | 5.06 | -0.6% | -0.372 to 0.313 | no difference beyond the noise |
| latency, mean (ms) | 1.8 | 1.81 | +0.2% | -0.0405 to 0.0491 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 282 | -44.9% | -350 to -110 | better |
| pages holding data, mean (MB) | 442 | 239 | -46.0% | -307 to -99.6 | better |
| pages read from disk into the pool (misses) | 243,125 | 368,985 | +51.8% | 497 to 251,222 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.137 | +0.7% | -0.00148 to 0.00349 | no difference beyond the noise |
| host CPU-seconds | 82.9 | 83.5 | +0.7% | -1.1 to 2.29 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.85 | 1.86 | +0.7% | -0.028 to 0.0545 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | 1.46 to 7.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 297 | 296 | -0.3% | -1.29 to -0.198 | **WORSE** |
| throughput (transactions a second) | 297 | 296 | -0.2% | -1.3 to -0.139 | **WORSE** |
| queries a second | 4,753 | 4,741 | -0.2% | -20.9 to -2.23 | **WORSE** |
| latency, 95th percentile (ms) | 1.83 | 1.78 | -2.9% | -0.144 to 0.0364 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.64 | 3.6 | -1.2% | -0.37 to 0.286 | no difference beyond the noise |
| latency, mean (ms) | 1.21 | 1.22 | +0.5% | -0.0184 to 0.0308 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 348 | -32.0% | -232 to -95.5 | better |
| pages holding data, mean (MB) | 462 | 319 | -30.8% | -211 to -73.2 | better |
| pages read from disk into the pool (misses) | 654,588 | 1,204,655 | +84.0% | 342,596 to 757,538 | shown, not judged |
| host CPU busy (share of the run) | 0.0956 | 0.096 | +0.4% | -0.00175 to 0.00259 | no difference beyond the noise |
| host CPU-seconds | 172 | 173 | +0.4% | -3.12 to 4.61 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.27 | 1.28 | +0.7% | -0.0214 to 0.0391 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 2.03 to 12 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 192 | -0.0% | -1.83 to 1.64 | no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.0% | -1.86 to 1.94 | no difference beyond the noise |
| queries a second | 3,914 | 3,915 | +0.0% | -37.2 to 38.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 7 | 7.43 | +6.2% | 0.068 to 0.797 | **WORSE** |
| latency, 99th percentile (ms) | 69.8 | 57.8 | -17.1% | -28.4 to 4.47 | no difference beyond the noise |
| latency, mean (ms) | 6.47 | 6.39 | -1.3% | -1.03 to 0.855 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 431 | -15.8% | -138 to -24.1 | better |
| pages holding data, mean (MB) | 460 | 388 | -15.8% | -120 to -24.8 | better |
| pages read from disk into the pool (misses) | 616,393 | 829,272 | +34.5% | 14,709 to 411,049 | shown, not judged |
| host CPU busy (share of the run) | 0.183 | 0.183 | -0.2% | -0.0036 to 0.00297 | no difference beyond the noise |
| host CPU-seconds | 331 | 330 | -0.2% | -6.57 to 5.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.74 | 3.74 | -0.1% | -0.0922 to 0.0824 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 6.08 to 18.6 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,948 | -0.0% | -6.65 to 5.4 | no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,954 | -0.0% | -5.77 to 5.36 | no difference beyond the noise |
| queries a second | 2,954 | 2,954 | -0.0% | -5.77 to 5.36 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.334 | 0.332 | -0.6% | -0.0106 to 0.00661 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.456 | +0.0% | 0 to 0 | same |
| latency, mean (ms) | 0.203 | 0.206 | +1.4% | -0.000846 to 0.00642 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 447 | -12.7% | -165 to 34.2 | no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 407 | -12.2% | -141 to 28.2 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,251 | 455,445 | +24.0% | -76,456 to 252,845 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.104 | +3.0% | -0.000168 to 0.00626 | no difference beyond the noise |
| host CPU-seconds | 168 | 173 | +3.2% | -0.425 to 11.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.124 | 0.128 | +3.2% | -0.000391 to 0.00841 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 0.0313 to 9.97 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 327 | 329 | +0.5% | -123 to 127 | no difference beyond the noise |
| throughput (transactions a second) | 989 | 988 | -0.1% | -2.04 to 0.902 | no difference beyond the noise |
| queries a second | 989 | 988 | -0.1% | -2.04 to 0.902 | no difference beyond the noise |
| latency, 95th percentile (ms) | 2.7 | 2.45 | -9.3% | -0.49 to -0.0143 | better |
| latency, 99th percentile (ms) | 5.25 | 5.15 | -1.8% | -0.791 to 0.603 | no difference beyond the noise |
| latency, mean (ms) | 0.982 | 1.02 | +3.6% | -0.332 to 0.402 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 342 | -33.3% | -272 to -68.5 | better |
| pages holding data, mean (MB) | 454 | 274 | -39.7% | -270 to -90 | better |
| pages read from disk into the pool (misses) | 188,643 | 301,104 | +59.6% | 68,969 to 155,953 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.113 | +4.6% | -0.017 to 0.027 | no difference beyond the noise |
| host CPU-seconds | 190 | 199 | +4.7% | -29.3 to 47.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.35 | 1.34 | -0.8% | -0.923 to 0.901 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 12.5 to 18.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
