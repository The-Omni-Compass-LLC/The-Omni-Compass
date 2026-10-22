# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 289 | 290 | +0.1% | -5.09 to 5.42 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 292 | +0.1% | -4.41 to 4.81 | EVEN, no difference beyond the noise |
| queries a second | 4,675 | 4,678 | +0.1% | -70.5 to 77 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.77 | 5.71 | -1.2% | -0.216 to 0.0791 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.28 | 8.28 | -0.0% | -0.372 to 0.369 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.38 | 3.34 | -1.2% | -0.084 to 0.0045 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 142 | +10.9% | 12.9 to 15.1 | power given |
| pages holding data, mean (MB) | 120 | 140 | +16.8% | 12.8 to 27.6 | power given |
| pages read from disk into the pool (misses) | 578,671 | 531,485 | -8.2% | -80,721 to -13,652 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.248 | -1.0% | -0.00495 to -0.000309 | GAIN |
| host CPU-seconds | 150 | 148 | -1.8% | -6.76 to 1.29 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.37 | 3.33 | -1.1% | -0.072 to -0.00164 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | +0.2% | -1.96 to 2.85 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.2% | -1.76 to 2.93 | EVEN, no difference beyond the noise |
| queries a second | 4,711 | 4,720 | +0.2% | -28.1 to 46.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.96 | 3.98 | +0.6% | -0.0793 to 0.127 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.5 | 5.64 | +2.4% | -0.0102 to 0.278 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.01 | 3.06 | +1.5% | -0.0101 to 0.102 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.3% | 4.74 to 11.5 | power given |
| pages holding data, mean (MB) | 120 | 133 | +11.1% | 11.4 to 15.3 | power given |
| pages read from disk into the pool (misses) | 1,980,456 | 1,907,591 | -3.7% | -167,873 to 22,142 | shown, not judged |
| host CPU busy (share of the run) | 0.235 | 0.238 | +1.5% | -0.00331 to 0.0105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 418 | 424 | +1.5% | -5.81 to 18.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.11 | 3.15 | +1.3% | -0.0223 to 0.105 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 190 | -0.3% | -2.98 to 1.82 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.3% | -3.01 to 1.97 | EVEN, no difference beyond the noise |
| queries a second | 3,942 | 3,932 | -0.3% | -60.2 to 39.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.79 | 9.73 | -0.6% | -0.308 to 0.192 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.6 | 13.7 | +0.6% | -0.274 to 0.44 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.97 | 4.98 | +0.1% | -0.0343 to 0.0468 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 142 | +10.8% | 7.36 to 20.3 | power given |
| pages holding data, mean (MB) | 118 | 133 | +13.0% | 4.78 to 26 | power given |
| pages read from disk into the pool (misses) | 1,671,308 | 1,593,176 | -4.7% | -147,658 to -8,606 | shown, not judged |
| host CPU busy (share of the run) | 0.282 | 0.281 | -0.4% | -0.00854 to 0.00614 | EVEN, no difference beyond the noise |
| host CPU-seconds | 500 | 498 | -0.4% | -15 to 11 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.75 | 5.74 | -0.1% | -0.0884 to 0.0764 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,958 | 2,957 | -0.0% | -6.79 to 3.98 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,963 | -0.1% | -7.26 to 2.97 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,963 | -0.1% | -7.26 to 2.97 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.226 | 0.214 | -5.5% | -0.0654 to 0.0407 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.352 | 0.334 | -5.2% | -0.0693 to 0.0326 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0973 | 0.0941 | -3.3% | -0.0214 to 0.0149 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.1% | 0.108 to 13 | power given |
| pages holding data, mean (MB) | 121 | 132 | +9.2% | 3.14 to 19.2 | power given |
| pages read from disk into the pool (misses) | 1,029,333 | 1,009,497 | -1.9% | -44,500 to 4,827 | shown, not judged |
| host CPU busy (share of the run) | 0.0715 | 0.0699 | -2.3% | -0.0103 to 0.00699 | EVEN, no difference beyond the noise |
| host CPU-seconds | 128 | 125 | -2.3% | -18.2 to 12.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0947 | 0.0926 | -2.3% | -0.0135 to 0.00925 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 159 | 172 | +8.6% | -61.5 to 88.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 987 | 990 | +0.3% | -1.43 to 6.69 | EVEN, no difference beyond the noise |
| queries a second | 987 | 990 | +0.3% | -1.43 to 6.69 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.59 | 3.24 | +24.8% | -0.959 to 2.25 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.76 | 13.3 | +72.0% | -7.47 to 18.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.11 | 1.34 | +21.1% | -0.25 to 0.716 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 137 | +7.1% | -6.11 to 24.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 125 | +4.6% | -3.37 to 14.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 414,906 | 410,022 | -1.2% | -18,366 to 8,598 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.137 | -2.3% | -0.0227 to 0.0164 | EVEN, no difference beyond the noise |
| host CPU-seconds | 247 | 242 | -2.2% | -39.5 to 28.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.47 | 3.22 | -7.5% | -1.7 to 1.18 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | -2.61 to 14.6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
