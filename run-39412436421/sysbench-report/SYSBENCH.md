# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.5% | -6.95 to 3.93 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 293 | -0.5% | -6.97 to 4.09 | EVEN, no difference beyond the noise |
| queries a second | 4,715 | 4,692 | -0.5% | -112 to 65.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.34 | 5.31 | -0.6% | -0.393 to 0.33 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.39 | 7.39 | +0.0% | -0.332 to 0.334 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.35 | 3.3 | -1.7% | -0.117 to 0.00178 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 140 | +9.1% | 2.69 to 20.6 | power given |
| pages holding data, mean (MB) | 120 | 137 | +13.9% | 6.41 to 26.9 | power given |
| pages read from disk into the pool (misses) | 581,384 | 535,133 | -8.0% | -99,099 to 6,597 | shown, not judged |
| host CPU busy (share of the run) | 0.256 | 0.251 | -1.9% | -0.0103 to 0.000684 | EVEN, no difference beyond the noise |
| host CPU-seconds | 152 | 149 | -1.9% | -6.27 to 0.384 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.39 | 3.34 | -1.4% | -0.139 to 0.0453 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 293 | +0.7% | -5.85 to 9.98 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.5% | -2.5 to 5.68 | EVEN, no difference beyond the noise |
| queries a second | 4,729 | 4,755 | +0.5% | -40 to 90.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.83 | 2.84 | +0.6% | -0.129 to 0.163 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 26.1 | 16.5 | -36.9% | -54.1 to 34.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3 | 2.76 | -8.3% | -1.17 to 0.677 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 134 | +4.6% | 2.16 to 9.54 | power given |
| pages holding data, mean (MB) | 120 | 131 | +9.5% | 5.85 to 16.8 | power given |
| pages read from disk into the pool (misses) | 1,975,286 | 1,933,564 | -2.1% | -94,019 to 10,576 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.166 | +0.6% | -0.00592 to 0.00792 | EVEN, no difference beyond the noise |
| host CPU-seconds | 295 | 297 | +0.6% | -10.7 to 14.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.22 | 2.22 | -0.1% | -0.0375 to 0.0318 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 170 | 170 | -0.1% | -3.73 to 3.37 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 195 | -0.3% | -2.91 to 1.71 | EVEN, no difference beyond the noise |
| queries a second | 3,914 | 3,902 | -0.3% | -58.2 to 34.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 15.1 | 14.9 | -1.2% | -0.567 to 0.207 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 20.5 | 20.6 | +0.6% | -1.28 to 1.53 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.16 | 6.17 | +0.1% | -0.177 to 0.183 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 141 | +10.3% | 10.3 to 16 | power given |
| pages holding data, mean (MB) | 121 | 134 | +10.6% | 10.7 to 14.9 | power given |
| pages read from disk into the pool (misses) | 1,668,284 | 1,597,946 | -4.2% | -158,008 to 17,333 | shown, not judged |
| host CPU busy (share of the run) | 0.277 | 0.274 | -1.2% | -0.00658 to 8.48e-05 | EVEN, no difference beyond the noise |
| host CPU-seconds | 509 | 503 | -1.3% | -13.2 to 0.449 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 6.49 | 6.42 | -1.1% | -0.296 to 0.149 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 7.8 to 13.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,961 | +0.0% | -11.9 to 12.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,966 | 2,965 | -0.0% | -14.1 to 12 | EVEN, no difference beyond the noise |
| queries a second | 2,966 | 2,965 | -0.0% | -14.1 to 12 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.231 | 0.237 | +2.3% | -0.00614 to 0.0168 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.358 | 0.361 | +0.7% | -0.016 to 0.0213 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.171 | -14.6% | -0.119 to 0.0605 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 131 | +2.6% | -6.22 to 13 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 127 | +4.6% | -9.43 to 20.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,030,826 | 1,019,632 | -1.1% | -40,518 to 18,129 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.116 | +1.9% | -0.0019 to 0.0062 | EVEN, no difference beyond the noise |
| host CPU-seconds | 202 | 206 | +1.9% | -3.21 to 11 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.15 | 0.153 | +1.9% | -0.00194 to 0.00762 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -4.92 to 10.3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 132 | 131 | -1.1% | -75.7 to 72.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 986 | 987 | +0.1% | -3.04 to 4.33 | EVEN, no difference beyond the noise |
| queries a second | 986 | 987 | +0.1% | -3.04 to 4.33 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 99.4 | 97.1 | -2.3% | -187 to 182 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 229 | 212 | -7.6% | -413 to 378 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 19 | 16 | -15.7% | -41.2 to 35.2 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.9% | 0.358 to 19.9 | power given |
| pages holding data, mean (MB) | 119 | 125 | +5.1% | -0.457 to 12.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 419,185 | 411,702 | -1.8% | -12,018 to -2,948 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.157 | -1.8% | -0.0179 to 0.0122 | EVEN, no difference beyond the noise |
| host CPU-seconds | 283 | 278 | -1.8% | -31.2 to 21.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.32 | 4.74 | -10.9% | -4.99 to 3.83 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
