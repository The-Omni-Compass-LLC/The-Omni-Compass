# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 292 | +0.1% | -5.01 to 5.76 | no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.2% | -5.02 to 5.97 | no difference beyond the noise |
| queries a second | 4,707 | 4,715 | +0.2% | -80.4 to 95.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.77 | 5.74 | -0.6% | -0.429 to 0.359 | no difference beyond the noise |
| latency, 99th percentile (ms) | 8.38 | 8.43 | +0.6% | -0.519 to 0.624 | no difference beyond the noise |
| latency, mean (ms) | 3.37 | 3.38 | +0.0% | -0.0613 to 0.0645 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 466 | -9.1% | -103 to 10.1 | no difference beyond the noise |
| pages holding data, mean (MB) | 448 | 387 | -13.6% | -99.4 to -22.3 | better |
| pages read from disk into the pool (misses) | 244,732 | 258,457 | +5.6% | -26,007 to 53,457 | shown, not judged |
| host CPU busy (share of the run) | 0.188 | 0.192 | +2.2% | 0.00173 to 0.00663 | **WORSE** |
| host CPU-seconds | 104 | 106 | +2.6% | 0.732 to 4.56 | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.38 | +2.3% | 0.00595 to 0.1 | **WORSE** |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 2.7 to 11.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | +0.1% | -2.92 to 3.25 | no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.1% | -2.92 to 3.24 | no difference beyond the noise |
| queries a second | 4,702 | 4,705 | +0.1% | -46.7 to 51.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 2.4 | 2.38 | -1.2% | -0.0904 to 0.0331 | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.75 | 3.7 | -1.2% | -0.298 to 0.209 | no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.74 | -0.4% | -0.0213 to 0.00828 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 305 | -40.4% | -227 to -187 | better |
| pages holding data, mean (MB) | 462 | 283 | -38.7% | -202 to -155 | better |
| pages read from disk into the pool (misses) | 653,474 | 1,288,459 | +97.2% | 529,894 to 740,076 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.139 | -0.2% | -0.00236 to 0.00173 | no difference beyond the noise |
| host CPU-seconds | 254 | 253 | -0.3% | -4.68 to 3.35 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.88 | 1.87 | -0.3% | -0.0325 to 0.0208 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | -0.00979 to 20.7 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 191 | -0.3% | -3.17 to 2.08 | no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.3% | -2.84 to 1.73 | no difference beyond the noise |
| queries a second | 3,943 | 3,932 | -0.3% | -56.8 to 34.7 | no difference beyond the noise |
| latency, 95th percentile (ms) | 9.12 | 9.23 | +1.2% | -0.128 to 0.348 | no difference beyond the noise |
| latency, 99th percentile (ms) | 13.6 | 13.6 | +0.5% | -0.823 to 0.972 | no difference beyond the noise |
| latency, mean (ms) | 5.45 | 5.47 | +0.4% | -0.0516 to 0.094 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 534 | +4.4% | -72.3 to 117 | no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 479 | +3.8% | -64.2 to 99 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,802 | 577,334 | -6.1% | -239,107 to 164,171 | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.214 | -0.0% | -0.00425 to 0.0041 | no difference beyond the noise |
| host CPU-seconds | 344 | 344 | +0.1% | -5.92 to 6.85 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.92 | 3.94 | +0.4% | -0.0946 to 0.128 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 20.3 |  | 6.65 to 34 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,910 | 2,914 | +0.1% | -10.8 to 17.7 | no difference beyond the noise |
| throughput (transactions a second) | 2,930 | 2,935 | +0.2% | -0.923 to 11.8 | no difference beyond the noise |
| queries a second | 2,930 | 2,935 | +0.2% | -0.923 to 11.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.305 | 0.332 | +8.9% | -0.112 to 0.166 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.521 | 0.531 | +1.9% | -0.118 to 0.137 | no difference beyond the noise |
| latency, mean (ms) | 0.29 | 0.157 | -45.8% | -0.645 to 0.379 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 415 | -19.0% | -306 to 112 | no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 373 | -19.3% | -281 to 102 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,291 | 502,048 | +36.7% | -189,177 to 458,691 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.115 | +1.0% | -0.0175 to 0.0197 | no difference beyond the noise |
| host CPU-seconds | 206 | 208 | +0.9% | -31.4 to 35.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.154 | 0.155 | +0.8% | -0.0239 to 0.0265 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.3 |  | 10.5 to 16.2 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4.83 | 5.4 | +11.8% | -2.03 to 3.18 | no difference beyond the noise |
| throughput (transactions a second) | 985 | 983 | -0.2% | -5 to 1.22 | no difference beyond the noise |
| queries a second | 985 | 983 | -0.2% | -5 to 1.22 | no difference beyond the noise |
| latency, 95th percentile (ms) | 1.67 | 1.63 | -2.6% | -0.291 to 0.206 | no difference beyond the noise |
| latency, 99th percentile (ms) | 2.91 | 2.9 | -0.6% | -0.321 to 0.284 | no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1.04 | -1.5% | -0.0977 to 0.0651 | no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 506 | -1.1% | -170 to 159 | no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 436 | -3.8% | -180 to 146 | no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,611 | 204,897 | +8.1% | -102,901 to 133,474 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.121 | -4.5% | -0.0446 to 0.0332 | no difference beyond the noise |
| host CPU-seconds | 196 | 187 | -4.3% | -67.3 to 50.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 93 | 75.8 | -18.5% | -103 to 68.4 | no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17.3 |  | 1.36 to 33.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
