# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 288 | 289 | +0.0% | -7.21 to 7.37 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 293 | +0.1% | -2.09 to 2.86 | EVEN, no difference beyond the noise |
| queries a second | 4,678 | 4,684 | +0.1% | -33.4 to 45.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.65 | 6.18 | -7.0% | -3.31 to 2.38 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.61 | 8.71 | +1.1% | -4.55 to 4.73 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.27 | 3.84 | -10.2% | -1.78 to 0.91 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 918 | +617.2% | 486 to 1,095 | power given |
| pages holding data, mean (MB) | 120 | 819 | +580.6% | 452 to 945 | power given |
| pages read from disk into the pool (misses) | 585,871 | 117,732 | -79.9% | -563,270 to -373,007 | shown, not judged |
| host CPU busy (share of the run) | 0.321 | 0.291 | -9.3% | -0.127 to 0.0674 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 173 | -9.2% | -75.2 to 40 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.3 | 3.91 | -9.2% | -1.77 to 0.983 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | -0.0% | -1.32 to 1.12 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.0% | -1.22 to 1.21 | EVEN, no difference beyond the noise |
| queries a second | 4,714 | 4,714 | -0.0% | -19.5 to 19.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.1 | 4.08 | -0.6% | -0.301 to 0.255 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.47 | 5.54 | +1.2% | -0.221 to 0.355 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.16 | 3.09 | -2.1% | -0.274 to 0.138 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 573 | +347.7% | 152 to 738 | power given |
| pages holding data, mean (MB) | 120 | 517 | +331.3% | 142 to 652 | power given |
| pages read from disk into the pool (misses) | 1,969,416 | 547,092 | -72.2% | -1,868,582 to -976,066 | shown, not judged |
| host CPU busy (share of the run) | 0.249 | 0.244 | -1.8% | -0.0191 to 0.00999 | EVEN, no difference beyond the noise |
| host CPU-seconds | 442 | 434 | -1.8% | -33.8 to 17.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.28 | 3.22 | -1.8% | -0.258 to 0.139 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 3.9 to 6.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 155 | 159 | +2.3% | -10.6 to 17.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.0% | -1.64 to 1.54 | EVEN, no difference beyond the noise |
| queries a second | 3,950 | 3,949 | -0.0% | -32.9 to 30.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 183 | 116 | -36.7% | -238 to 104 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 529 | 433 | -18.3% | -289 to 95.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 34.9 | 26.1 | -25.4% | -31.1 to 13.3 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,239 | +867.6% | 976 to 1,245 | power given |
| pages holding data, mean (MB) | 121 | 1,011 | +735.2% | 841 to 939 | power given |
| pages read from disk into the pool (misses) | 1,667,004 | 140,148 | -91.6% | -1,804,172 to -1,249,540 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.175 | -17.6% | -0.0452 to -0.0297 | GAIN |
| host CPU-seconds | 377 | 310 | -17.7% | -80 to -53 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 5.34 | 4.31 | -19.4% | -1.23 to -0.847 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 6.04 to 24 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 11.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,944 | 2,952 | +0.3% | -41.7 to 59 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,964 | 2,966 | +0.1% | -11.4 to 15.8 | EVEN, no difference beyond the noise |
| queries a second | 2,964 | 2,966 | +0.1% | -11.4 to 15.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.27 | 0.249 | -7.9% | -0.0802 to 0.0376 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.9 | 0.383 | -92.2% | -24 to 15 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 0.397 | -66.8% | -4.86 to 3.26 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,148 | +797.0% | 948 to 1,092 | power given |
| pages holding data, mean (MB) | 121 | 909 | +650.2% | 774 to 802 | power given |
| pages read from disk into the pool (misses) | 1,033,469 | 97,579 | -90.6% | -975,155 to -896,624 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.12 | -6.8% | -0.0127 to -0.00484 | GAIN |
| host CPU-seconds | 228 | 213 | -6.8% | -22.2 to -8.86 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 0.17 | 0.158 | -7.0% | -0.0167 to -0.00724 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 8.67 |  | 3.5 to 13.8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 6.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 123 | 167 | +35.4% | 20.8 to 66.2 | GAIN |
| throughput (transactions a second) | 986 | 987 | +0.1% | -1.76 to 4.44 | EVEN, no difference beyond the noise |
| queries a second | 986 | 987 | +0.1% | -1.76 to 4.44 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.35 | 1.13 | -16.1% | -0.415 to -0.018 | GAIN |
| latency, 99th percentile (ms) | 2.15 | 1.63 | -24.0% | -1.29 to 0.261 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.844 | 0.805 | -4.7% | -0.143 to 0.0646 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,240 | +868.7% | 986 to 1,238 | power given |
| pages holding data, mean (MB) | 118 | 869 | +633.6% | 730 to 771 | power given |
| pages read from disk into the pool (misses) | 419,320 | 84,063 | -80.0% | -375,443 to -295,072 | shown, not judged |
| host CPU busy (share of the run) | 0.237 | 0.209 | -11.7% | -0.048 to -0.0072 | GAIN |
| host CPU-seconds | 419 | 370 | -11.7% | -84.4 to -13.5 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 7.6 | 4.9 | -35.5% | -5.37 to -0.0223 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
