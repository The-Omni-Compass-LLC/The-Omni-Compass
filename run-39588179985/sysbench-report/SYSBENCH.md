# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 289 | -0.1% | -2.16 to 1.31 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.1% | -2.44 to 1.71 | EVEN, no difference beyond the noise |
| queries a second | 4,704 | 4,698 | -0.1% | -39 to 27.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.21 | 6.21 | -0.0% | -0.278 to 0.276 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.84 | 8.89 | +0.6% | -0.174 to 0.279 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.56 | 3.54 | -0.7% | -0.118 to 0.0716 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 147 | +14.6% | 0.0365 to 37.2 | power given |
| pages holding data, mean (MB) | 120 | 141 | +16.8% | 11.4 to 29 | power given |
| pages read from disk into the pool (misses) | 580,778 | 511,537 | -11.9% | -101,319 to -37,163 | shown, not judged |
| host CPU busy (share of the run) | 0.205 | 0.203 | -1.1% | -0.0127 to 0.00827 | EVEN, no difference beyond the noise |
| host CPU-seconds | 114 | 112 | -1.1% | -7.13 to 4.67 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.56 | 2.54 | -1.0% | -0.144 to 0.094 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.3% | -3.23 to 1.31 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.3% | -3.33 to 1.38 | EVEN, no difference beyond the noise |
| queries a second | 4,731 | 4,715 | -0.3% | -53.3 to 22 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.25 | 4.25 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 5.81 | 5.77 | -0.6% | -0.186 to 0.116 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.32 | 3.31 | -0.3% | -0.0372 to 0.0201 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 137 | +7.3% | 4.64 to 14 | power given |
| pages holding data, mean (MB) | 120 | 136 | +13.1% | 6.98 to 24.4 | power given |
| pages read from disk into the pool (misses) | 1,985,776 | 1,908,332 | -3.9% | -184,450 to 29,562 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.207 | -0.3% | -0.00341 to 0.0022 | EVEN, no difference beyond the noise |
| host CPU-seconds | 347 | 346 | -0.3% | -5.9 to 4.09 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.56 | 2.57 | +0.1% | -0.0468 to 0.0499 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 169 | 170 | +0.6% | -5.27 to 7.42 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | +0.2% | -2.85 to 3.47 | EVEN, no difference beyond the noise |
| queries a second | 3,903 | 3,909 | +0.2% | -57.1 to 69.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 16.2 | 15.8 | -2.4% | -2.23 to 1.45 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 278 | 226 | -18.8% | -204 to 99.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 12.2 | 10.3 | -15.8% | -6.08 to 2.22 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 143 | +11.4% | 5.17 to 23.9 | power given |
| pages holding data, mean (MB) | 122 | 136 | +11.3% | 5.46 to 22.2 | power given |
| pages read from disk into the pool (misses) | 1,661,561 | 1,602,907 | -3.5% | -125,574 to 8,267 | shown, not judged |
| host CPU busy (share of the run) | 0.249 | 0.248 | -0.4% | -0.00592 to 0.00404 | EVEN, no difference beyond the noise |
| host CPU-seconds | 449 | 447 | -0.3% | -11.3 to 8.24 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.77 | 5.72 | -1.0% | -0.389 to 0.272 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.33 |  | 6.46 to 12.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,926 | 2,930 | +0.1% | -11.9 to 19.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,932 | 2,934 | +0.1% | -2.27 to 5.92 | EVEN, no difference beyond the noise |
| queries a second | 2,932 | 2,934 | +0.1% | -2.27 to 5.92 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.238 | 0.24 | +0.6% | -0.0261 to 0.0288 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.409 | 0.402 | -1.8% | -0.0382 to 0.0235 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.386 | 0.144 | -62.8% | -1.29 to 0.807 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 134 | +4.4% | -3.08 to 14.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 129 | +6.2% | -1.65 to 16.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,029,971 | 1,013,436 | -1.6% | -36,127 to 3,057 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.124 | +1.1% | -0.00639 to 0.00912 | EVEN, no difference beyond the noise |
| host CPU-seconds | 223 | 225 | +1.1% | -11.5 to 16.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.165 | 0.167 | +1.0% | -0.00903 to 0.0122 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 120 | 139 | +16.1% | -42.8 to 81.5 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 986 | 987 | +0.1% | -8.1 to 9.29 | EVEN, no difference beyond the noise |
| queries a second | 986 | 987 | +0.1% | -8.1 to 9.29 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.35 | 2.31 | -2.0% | -0.926 to 0.834 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.74 | 4.46 | -6.0% | -2.53 to 1.96 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.09 | 1.11 | +2.0% | -0.0614 to 0.104 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.8% | -2.7 to 25.2 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 118 | 126 | +6.5% | -4.44 to 19.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 415,149 | 408,087 | -1.7% | -16,383 to 2,259 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.162 | +8.4% | -0.0683 to 0.0934 | EVEN, no difference beyond the noise |
| host CPU-seconds | 263 | 285 | +8.3% | -120 to 163 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.84 | 4.49 | -7.2% | -1.97 to 1.27 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | -0.923 to 14.3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
