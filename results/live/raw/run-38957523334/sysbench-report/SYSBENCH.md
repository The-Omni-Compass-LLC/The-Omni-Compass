# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.3% | -1.15 to 3.01 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 293 | +0.2% | -1.75 to 3.11 | EVEN, no difference beyond the noise |
| queries a second | 4,679 | 4,690 | +0.2% | -28 to 49.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.37 | 3.21 | -4.7% | -0.34 to 0.0217 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.18 | 4.91 | -5.2% | -0.488 to -0.0558 | GAIN |
| latency, mean (ms) | 1.87 | 1.85 | -0.7% | -0.0382 to 0.0119 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 428 | -16.5% | -157 to -11.7 | GAIN |
| pages holding data, mean (MB) | 445 | 360 | -19.1% | -144 to -25.6 | GAIN |
| pages read from disk into the pool (misses) | 245,342 | 268,684 | +9.5% | -10,130 to 56,813 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.142 | +0.9% | -0.0037 to 0.00633 | EVEN, no difference beyond the noise |
| host CPU-seconds | 85.7 | 86.5 | +0.9% | -2.43 to 4.02 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.91 | 1.92 | +0.6% | -0.0447 to 0.0677 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | -0.1% | -3.79 to 3.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.3% | -2.81 to 1.1 | EVEN, no difference beyond the noise |
| queries a second | 4,698 | 4,684 | -0.3% | -45 to 17.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.79 | 2.79 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 5.11 | 4.63 | -9.6% | -3.14 to 2.16 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.22 | 2.14 | -33.4% | -5.99 to 3.84 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 442 | -13.6% | -162 to 22.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 402 | -12.8% | -159 to 41 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 656,154 | 783,868 | +19.5% | -144,782 to 400,210 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.16 | +0.3% | -0.00522 to 0.0061 | EVEN, no difference beyond the noise |
| host CPU-seconds | 290 | 291 | +0.3% | -9.49 to 11.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.16 | 2.17 | +0.3% | -0.0501 to 0.0651 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 3.61 to 21.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 190 | -0.4% | -1.41 to -0.154 | LOSS |
| throughput (transactions a second) | 197 | 196 | -0.4% | -1.22 to -0.232 | LOSS |
| queries a second | 3,935 | 3,920 | -0.4% | -24.4 to -4.65 | LOSS |
| latency, 95th percentile (ms) | 9.06 | 9 | -0.6% | -0.286 to 0.178 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.3 | 13.5 | +1.8% | -0.36 to 0.844 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.51 | 5.48 | -0.6% | -0.204 to 0.137 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 541 | +5.6% | -6.68 to 63.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 483 | +4.6% | 11 to 31.4 | power given |
| pages read from disk into the pool (misses) | 617,955 | 570,854 | -7.6% | -75,922 to -18,278 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.216 | -1.7% | -0.0106 to 0.00311 | EVEN, no difference beyond the noise |
| host CPU-seconds | 354 | 348 | -1.6% | -16.8 to 5.39 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.04 | 3.99 | -1.2% | -0.186 to 0.0891 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14 |  | 4.06 to 23.9 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,887 | 2,892 | +0.2% | -38.8 to 48.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,931 | 2,929 | -0.1% | -10.9 to 6.22 | EVEN, no difference beyond the noise |
| queries a second | 2,931 | 2,929 | -0.1% | -10.9 to 6.22 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.413 | 0.405 | -2.0% | -0.103 to 0.0861 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.669 | 0.646 | -3.4% | -0.2 to 0.154 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.188 | 0.188 | -0.2% | -0.0282 to 0.0274 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 491 | -4.0% | -105 to 64.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 444 | -4.2% | -99.8 to 60.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,859 | 382,727 | +4.3% | -85,428 to 117,164 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.14 | -0.6% | -0.0204 to 0.0186 | EVEN, no difference beyond the noise |
| host CPU-seconds | 254 | 253 | -0.6% | -36.1 to 33.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.191 | 0.19 | -0.8% | -0.0301 to 0.027 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14 |  | 6.55 to 21.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| throughput (transactions a second) | 978 | 977 | -0.1% | -7.71 to 6.02 | EVEN, no difference beyond the noise |
| queries a second | 978 | 977 | -0.1% | -7.71 to 6.02 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.15 | 2.12 | -1.5% | -0.488 to 0.424 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.3 | 3.49 | -34.2% | -12.1 to 8.52 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.55 | 1.49 | -3.6% | -0.427 to 0.315 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -61 to 56.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 446 | -1.8% | -58.1 to 41.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,024 | 189,944 | +0.5% | -31,901 to 33,742 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.226 | -0.9% | -0.0243 to 0.0203 | EVEN, no difference beyond the noise |
| host CPU-seconds | 406 | 402 | -0.9% | -42.7 to 35.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 405,730 | 402,197 | -0.9% | -42,747 to 35,680 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.7 |  | 11.2 to 14.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
