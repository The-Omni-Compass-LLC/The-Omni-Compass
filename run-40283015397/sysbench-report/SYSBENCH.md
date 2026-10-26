# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 292 | +0.4% | -6.77 to 9.35 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 294 | +0.5% | -6.56 to 9.47 | EVEN, no difference beyond the noise |
| queries a second | 4,677 | 4,700 | +0.5% | -105 to 151 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.44 | 5.47 | +0.6% | -0.11 to 0.177 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.39 | 7.57 | +2.4% | -0.207 to 0.567 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.46 | 3.46 | -0.0% | -0.0121 to 0.0105 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.4% | 5.73 to 8.12 | power given |
| pages holding data, mean (MB) | 120 | 130 | +8.1% | 6.7 to 12.8 | power given |
| pages read from disk into the pool (misses) | 566,927 | 543,604 | -4.1% | -61,646 to 15,000 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.206 | +1.2% | -0.000969 to 0.00582 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 114 | +1.2% | -0.511 to 3.23 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.54 | 2.56 | +0.8% | -0.0114 to 0.0496 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.1% | -2 to 1.67 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.1% | -2.2 to 1.8 | EVEN, no difference beyond the noise |
| queries a second | 4,718 | 4,715 | -0.1% | -35.2 to 28.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.3 | 4.33 | +0.6% | -0.0848 to 0.136 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.88 | 5.88 | -0.0% | -0.264 to 0.263 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.35 | 3.34 | -0.1% | -0.0564 to 0.0492 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 132 | +3.2% | 0.674 to 7.52 | power given |
| pages holding data, mean (MB) | 120 | 128 | +6.6% | -1.7 to 17.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,980,818 | 2,024,744 | +2.2% | -68,952 to 156,804 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.209 | +0.3% | -0.00534 to 0.00651 | EVEN, no difference beyond the noise |
| host CPU-seconds | 348 | 350 | +0.3% | -9.23 to 11.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.58 | 2.59 | +0.4% | -0.0624 to 0.0815 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 196 | 196 | +0.2% | -3.02 to 3.69 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | +0.2% | -3.03 to 3.74 | EVEN, no difference beyond the noise |
| queries a second | 3,954 | 3,961 | +0.2% | -60.7 to 74.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.55 | 6.71 | +2.4% | -0.0143 to 0.333 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.3 | 10.4 | +1.2% | -0.142 to 0.386 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.05 | 3.23 | +6.0% | -0.0635 to 0.427 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.1% | -4.24 to 20 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 122 | 128 | +4.9% | -4.77 to 16.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,668,306 | 1,616,831 | -3.1% | -154,325 to 51,373 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.154 | +4.7% | 0.0046 to 0.00931 | power given |
| host CPU-seconds | 261 | 274 | +4.7% | 8.31 to 16.3 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.93 | 3.06 | +4.5% | 0.124 to 0.139 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | 0.538 to 8.13 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,944 | 2,946 | +0.1% | -7.43 to 10.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,951 | 2,953 | +0.1% | -8.27 to 11.7 | EVEN, no difference beyond the noise |
| queries a second | 2,951 | 2,953 | +0.1% | -8.27 to 11.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.35 | 0.346 | -1.1% | -0.0126 to 0.00461 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.461 | 0.456 | -1.2% | -0.0168 to 0.00614 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.212 | 0.21 | -0.9% | -0.00313 to -0.00076 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 131 | +2.6% | -0.266 to 6.98 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 127 | +4.6% | -2.17 to 13.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,028,437 | 1,018,780 | -0.9% | -12,943 to -6,371 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.113 | -1.1% | -0.00292 to 0.000317 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 188 | -1.1% | -4.99 to 0.621 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.141 | 0.14 | -1.2% | -0.00393 to 0.000509 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 80.5 | 88.6 | +10.1% | -0.672 to 16.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 985 | +0.1% | -3.27 to 5.54 | EVEN, no difference beyond the noise |
| queries a second | 984 | 985 | +0.1% | -3.27 to 5.54 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.44 | 1.48 | +2.8% | -0.186 to 0.266 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.38 | 2.59 | +8.8% | -0.955 to 1.37 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.886 | 0.905 | +2.2% | -0.0362 to 0.0747 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 128 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 119 | 119 | -0.4% | -6.76 to 5.77 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 416,912 | 416,411 | -0.1% | -9,628 to 8,627 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.233 | +5.9% | -0.04 to 0.0659 | EVEN, no difference beyond the noise |
| host CPU-seconds | 381 | 404 | +5.9% | -69.9 to 115 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 10.5 | 10.3 | -2.3% | -3.23 to 2.76 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
