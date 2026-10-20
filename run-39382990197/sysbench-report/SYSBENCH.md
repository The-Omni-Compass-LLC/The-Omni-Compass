# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.2% | -7.14 to 5.85 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.3% | -6.92 to 5.07 | EVEN, no difference beyond the noise |
| queries a second | 4,719 | 4,704 | -0.3% | -111 to 81.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.67 | 5.6 | -1.2% | -0.212 to 0.0775 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.84 | 7.7 | -1.8% | -0.493 to 0.211 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.57 | 3.53 | -1.1% | -0.0864 to 0.00787 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.9% | 2.7 to 20.1 | power given |
| pages holding data, mean (MB) | 120 | 137 | +13.9% | -0.0407 to 33.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 580,528 | 555,558 | -4.3% | -50,415 to 475 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.215 | -0.3% | -0.0164 to 0.0152 | EVEN, no difference beyond the noise |
| host CPU-seconds | 120 | 120 | -0.1% | -9.63 to 9.41 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.67 | 2.67 | -0.0% | -0.146 to 0.144 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.0% | -2.11 to 2.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.0% | -1.77 to 1.88 | EVEN, no difference beyond the noise |
| queries a second | 4,718 | 4,719 | +0.0% | -28.4 to 30.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.33 | 4.25 | -1.8% | -0.0795 to -0.0745 | GAIN |
| latency, 99th percentile (ms) | 6.21 | 6.06 | -2.4% | -0.567 to 0.273 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.28 | 3.24 | -1.4% | -0.101 to 0.0111 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 137 | +7.0% | 2.12 to 15.8 | power given |
| pages holding data, mean (MB) | 120 | 135 | +12.7% | 9.08 to 21.4 | power given |
| pages read from disk into the pool (misses) | 1,979,239 | 1,908,468 | -3.6% | -112,654 to -28,888 | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.199 | -1.5% | -0.00959 to 0.00353 | EVEN, no difference beyond the noise |
| host CPU-seconds | 338 | 333 | -1.5% | -15.9 to 5.78 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.51 | 2.47 | -1.5% | -0.104 to 0.0266 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 112 | 104 | -7.1% | -58.1 to 42.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.0% | -1.25 to 1.35 | EVEN, no difference beyond the noise |
| queries a second | 3,933 | 3,934 | +0.0% | -25 to 27.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 365 | 419 | +15.0% | -132 to 241 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 741 | 916 | +23.6% | -372 to 722 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 71.3 | 82.9 | +16.4% | -44.9 to 68.2 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 144 | +12.6% | 7.99 to 24.3 | power given |
| pages holding data, mean (MB) | 122 | 137 | +12.1% | 6.76 to 22.9 | power given |
| pages read from disk into the pool (misses) | 1,660,503 | 1,583,670 | -4.6% | -152,575 to -1,090 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.211 | -0.4% | -0.00279 to 0.000885 | EVEN, no difference beyond the noise |
| host CPU-seconds | 379 | 377 | -0.4% | -4.92 to 1.76 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 7.56 | 7.97 | +5.4% | -3.01 to 3.83 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9 |  | 6.52 to 11.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,958 | 2,960 | +0.1% | -5.44 to 9.26 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,966 | 2,967 | +0.0% | -6.27 to 8.45 | EVEN, no difference beyond the noise |
| queries a second | 2,966 | 2,967 | +0.0% | -6.27 to 8.45 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.21 | 0.208 | -1.0% | -0.0776 to 0.0736 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.336 | 0.33 | -1.8% | -0.0849 to 0.0729 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0971 | 0.0961 | -1.1% | -0.0366 to 0.0345 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 140 | +9.5% | -3.77 to 28.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 136 | +12.3% | 0.635 to 29.3 | power given |
| pages read from disk into the pool (misses) | 1,029,529 | 999,577 | -2.9% | -76,426 to 16,521 | shown, not judged |
| host CPU busy (share of the run) | 0.0752 | 0.0754 | +0.3% | -0.0271 to 0.0276 | EVEN, no difference beyond the noise |
| host CPU-seconds | 135 | 135 | +0.2% | -48.4 to 49 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.1 | 0.1 | +0.2% | -0.0359 to 0.0362 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.67 |  | 1.87 to 9.46 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 11 | 8.6 | -21.7% | -12.5 to 7.69 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 985 | 985 | +0.0% | -5.27 to 5.34 | EVEN, no difference beyond the noise |
| queries a second | 985 | 985 | +0.0% | -5.27 to 5.34 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.12 | 2.33 | +9.8% | -1.13 to 1.55 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.19 | 5.33 | +2.7% | -7.41 to 7.69 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.19 | 1.23 | +3.6% | -0.509 to 0.595 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 142 | +10.8% | 5.31 to 22.3 | power given |
| pages holding data, mean (MB) | 119 | 128 | +7.7% | 3.28 to 14.9 | power given |
| pages read from disk into the pool (misses) | 416,168 | 407,051 | -2.2% | -19,806 to 1,572 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.272 | +48.3% | -0.182 to 0.36 | EVEN, no difference beyond the noise |
| host CPU-seconds | 285 | 424 | +48.9% | -285 to 564 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 84.4 | 111 | +31.6% | -178 to 231 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 8 to 8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
