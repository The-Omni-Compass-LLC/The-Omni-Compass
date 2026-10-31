# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 296 | +0.3% | -1.52 to 3.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.3% | -0.621 to 2.43 | EVEN, no difference beyond the noise |
| queries a second | 4,736 | 4,751 | +0.3% | -9.94 to 38.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.83 | 2.97 | +4.9% | -0.352 to 0.63 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.3 | 4.55 | +5.7% | -0.69 to 1.18 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.41 | 1.42 | +0.5% | -0.0114 to 0.0268 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 540 | +322.0% | -490 to 1,315 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 457 | +278.5% | -290 to 962 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 600,439 | 311,465 | -48.1% | -564,011 to -13,936 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.106 | +3.9% | -0.00155 to 0.00943 | EVEN, no difference beyond the noise |
| host CPU-seconds | 61.4 | 63.7 | +3.8% | -0.944 to 5.66 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.36 | 1.41 | +3.5% | -0.0204 to 0.116 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | -5.61 to 11.6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 293 | -0.5% | -4.98 to 1.95 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 293 | -0.5% | -5.05 to 2.06 | EVEN, no difference beyond the noise |
| queries a second | 4,719 | 4,695 | -0.5% | -80.8 to 33 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.36 | 3.47 | +3.0% | -0.211 to 0.415 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.82 | 4.94 | +2.4% | -0.21 to 0.441 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.48 | 2.46 | -0.8% | -0.135 to 0.0941 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 503 | +293.3% | 366 to 385 | power given |
| pages holding data, mean (MB) | 120 | 458 | +281.4% | 337 to 338 | power given |
| pages read from disk into the pool (misses) | 1,986,212 | 652,381 | -67.2% | -1,399,665 to -1,267,998 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.201 | -1.0% | -0.00729 to 0.00326 | EVEN, no difference beyond the noise |
| host CPU-seconds | 370 | 366 | -1.0% | -13.1 to 5.83 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.73 | 2.72 | -0.5% | -0.107 to 0.0799 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 179 | 196 | +9.4% | 14.3 to 19.3 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.3% | -2.44 to 3.55 | EVEN, no difference beyond the noise |
| queries a second | 3,923 | 3,934 | +0.3% | -48.9 to 71.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 12.9 | 7.39 | -42.8% | -5.98 to -5.06 | GAIN |
| latency, 99th percentile (ms) | 18.2 | 9.74 | -46.4% | -8.9 to -7.97 | GAIN |
| latency, mean (ms) | 6.29 | 5.1 | -18.9% | -1.35 to -1.03 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,060 | +728.3% | 788 to 1,077 | power given |
| pages holding data, mean (MB) | 121 | 936 | +674.7% | 737 to 893 | power given |
| pages read from disk into the pool (misses) | 1,663,808 | 169,958 | -89.8% | -1,648,515 to -1,339,185 | shown, not judged |
| host CPU busy (share of the run) | 0.315 | 0.272 | -13.8% | -0.055 to -0.0321 | GAIN |
| host CPU-seconds | 554 | 477 | -13.9% | -96.8 to -57.5 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 6.77 | 5.33 | -21.3% | -1.67 to -1.21 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 2.7 to 11.3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,943 | 2,945 | +0.1% | -4.6 to 7.62 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,950 | 2,953 | +0.1% | -5.43 to 11 | EVEN, no difference beyond the noise |
| queries a second | 2,950 | 2,953 | +0.1% | -5.43 to 11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.352 | 0.348 | -1.2% | -0.0282 to 0.0195 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.459 | 0.47 | +2.5% | -0.0314 to 0.0541 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.208 | -4.0% | -0.0244 to 0.00706 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 574 | +348.8% | -25.3 to 918 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 516 | +325.6% | 19.2 to 770 | power given |
| pages read from disk into the pool (misses) | 1,029,862 | 335,919 | -67.4% | -1,163,981 to -223,904 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.166 | -3.7% | -0.0196 to 0.00695 | EVEN, no difference beyond the noise |
| host CPU-seconds | 304 | 293 | -3.7% | -34.7 to 12.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.226 | 0.217 | -3.7% | -0.0262 to 0.00947 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.33 |  | -0.535 to 5.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7.68 | 14.6 | +90.5% | 3.86 to 10 | GAIN |
| throughput (transactions a second) | 984 | 984 | +0.1% | -5.73 to 7.25 | EVEN, no difference beyond the noise |
| queries a second | 984 | 984 | +0.1% | -5.73 to 7.25 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.82 | 1.5 | -18.0% | -0.486 to -0.172 | GAIN |
| latency, 99th percentile (ms) | 2.76 | 2.2 | -20.4% | -0.776 to -0.352 | GAIN |
| latency, mean (ms) | 1.06 | 0.979 | -7.7% | -0.129 to -0.0347 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,257 | +882.4% | 1,032 to 1,227 | power given |
| pages holding data, mean (MB) | 117 | 862 | +636.0% | 716 to 774 | power given |
| pages read from disk into the pool (misses) | 418,080 | 87,632 | -79.0% | -379,077 to -281,820 | shown, not judged |
| host CPU busy (share of the run) | 0.262 | 0.231 | -11.9% | -0.0546 to -0.00788 | GAIN |
| host CPU-seconds | 459 | 404 | -12.0% | -95.4 to -14.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 131 | 60.8 | -53.5% | -84.8 to -55.3 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
