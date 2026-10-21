# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.2% | -2.66 to 3.74 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.2% | -2.65 to 3.87 | EVEN, no difference beyond the noise |
| queries a second | 4,680 | 4,690 | +0.2% | -42.4 to 61.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4 | 4.03 | +0.6% | -0.0804 to 0.129 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.44 | 5.44 | +0.0% | -0.421 to 0.423 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.51 | 2.51 | +0.2% | -0.0413 to 0.0535 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 142 | +10.8% | 13.1 to 14.6 | power given |
| pages holding data, mean (MB) | 120 | 134 | +11.4% | 11.6 to 15.6 | power given |
| pages read from disk into the pool (misses) | 577,365 | 525,626 | -9.0% | -85,207 to -18,270 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.198 | +1.5% | -0.00356 to 0.00934 | EVEN, no difference beyond the noise |
| host CPU-seconds | 119 | 120 | +1.5% | -2.04 to 5.53 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.64 | 2.67 | +1.3% | -0.0356 to 0.103 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.2% | -4.29 to 3.19 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 292 | -0.3% | -3.08 to 1.1 | EVEN, no difference beyond the noise |
| queries a second | 4,695 | 4,679 | -0.3% | -49.3 to 17.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.83 | 2.79 | -1.2% | -0.179 to 0.111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.38 | 4.23 | -3.6% | -0.551 to 0.237 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.79 | 2.14 | -23.4% | -3.4 to 2.09 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.3% | 5.52 to 10.5 | power given |
| pages holding data, mean (MB) | 120 | 134 | +11.6% | 10.4 to 17.3 | power given |
| pages read from disk into the pool (misses) | 1,973,356 | 1,913,137 | -3.1% | -79,074 to -41,363 | shown, not judged |
| host CPU busy (share of the run) | 0.176 | 0.175 | -0.5% | -0.00354 to 0.00168 | EVEN, no difference beyond the noise |
| host CPU-seconds | 322 | 320 | -0.5% | -6.66 to 3.25 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.39 | 2.38 | -0.3% | -0.035 to 0.0195 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 100 | 94.5 | -5.5% | -34.6 to 23.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 197 | +0.8% | -0.949 to 4.02 | EVEN, no difference beyond the noise |
| queries a second | 3,917 | 3,948 | +0.8% | -19 to 80.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 563 | 626 | +11.2% | -412 to 538 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,709 | 1,980 | +15.8% | -1,444 to 1,984 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 118 | 133 | +12.2% | -58 to 87 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 147 | +15.1% | 14.8 to 23.9 | power given |
| pages holding data, mean (MB) | 122 | 140 | +14.7% | 11.3 to 24.5 | power given |
| pages read from disk into the pool (misses) | 1,658,388 | 1,581,631 | -4.6% | -121,502 to -32,011 | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.214 | -0.2% | -0.00407 to 0.00307 | EVEN, no difference beyond the noise |
| host CPU-seconds | 382 | 382 | -0.2% | -6.12 to 4.48 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 8.49 | 8.85 | +4.2% | -2.07 to 2.77 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9 |  | 4.7 to 13.3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,945 | -0.0% | -3.31 to 2.57 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,953 | +0.0% | 0.201 to 1.16 | GAIN |
| queries a second | 2,953 | 2,953 | +0.0% | 0.201 to 1.16 | GAIN |
| latency, 95th percentile (ms) | 0.361 | 0.37 | +2.4% | -0.0152 to 0.0325 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.482 | 0.49 | +1.8% | -0.0323 to 0.0497 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.222 | +2.6% | -0.00785 to 0.0189 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.8% | 0.839 to 14.1 | power given |
| pages holding data, mean (MB) | 121 | 131 | +7.8% | 3.79 to 15.1 | power given |
| pages read from disk into the pool (misses) | 1,029,320 | 1,006,912 | -2.2% | -36,872 to -7,944 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.12 | +2.5% | -0.0064 to 0.0122 | EVEN, no difference beyond the noise |
| host CPU-seconds | 196 | 200 | +2.3% | -10.8 to 19.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.146 | 0.149 | +2.3% | -0.00809 to 0.0147 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 13.6 | 16.3 | +19.2% | 2.42 to 2.82 | GAIN |
| throughput (transactions a second) | 984 | 983 | -0.1% | -3.25 to 1.13 | EVEN, no difference beyond the noise |
| queries a second | 984 | 983 | -0.1% | -3.25 to 1.13 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.97 | 2.07 | +4.9% | -0.0897 to 0.284 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.27 | 3.67 | +12.4% | -0.339 to 1.15 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.08 | 1.09 | +1.0% | -0.0213 to 0.0428 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.9% | 3.81 to 16.3 | power given |
| pages holding data, mean (MB) | 118 | 125 | +5.8% | 3.15 to 10.5 | power given |
| pages read from disk into the pool (misses) | 417,037 | 410,656 | -1.5% | -15,510 to 2,748 | shown, not judged |
| host CPU busy (share of the run) | 0.255 | 0.267 | +4.6% | -0.0165 to 0.0398 | EVEN, no difference beyond the noise |
| host CPU-seconds | 448 | 468 | +4.5% | -28.9 to 69.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 73.7 | 63.9 | -13.3% | -24.4 to 4.8 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
