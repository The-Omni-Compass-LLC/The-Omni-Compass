# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 295 | +0.6% | -2.46 to 5.98 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 296 | +0.4% | -0.212 to 2.48 | EVEN, no difference beyond the noise |
| queries a second | 4,711 | 4,729 | +0.4% | -3.39 to 39.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.34 | 3.3 | -1.2% | -0.416 to 0.337 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 4.97 | -5.5% | -1.95 to 1.38 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.63 | 1.53 | -6.3% | -0.486 to 0.281 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 134 | +4.8% | 0.154 to 12.1 | power given |
| pages holding data, mean (MB) | 120 | 130 | +8.6% | -7.44 to 28.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 577,036 | 563,639 | -2.3% | -30,531 to 3,738 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.112 | -1.0% | -0.00717 to 0.00487 | EVEN, no difference beyond the noise |
| host CPU-seconds | 67.7 | 67 | -1.0% | -4.25 to 2.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.52 | 1.49 | -1.6% | -0.105 to 0.0572 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 293 | +0.9% | -0.198 to 5.51 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.4% | -1.45 to 3.95 | EVEN, no difference beyond the noise |
| queries a second | 4,681 | 4,701 | +0.4% | -23.2 to 63.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.86 | 2.86 | -0.0% | -0.128 to 0.128 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 54.2 | 4.74 | -91.3% | -262 to 163 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.46 | 2.32 | -48.0% | -11.6 to 7.3 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.2% | 3.08 to 10.2 | power given |
| pages holding data, mean (MB) | 120 | 132 | +10.1% | 5.92 to 18.3 | power given |
| pages read from disk into the pool (misses) | 1,974,271 | 1,925,685 | -2.5% | -122,673 to 25,501 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.165 | +0.3% | -0.0016 to 0.00255 | EVEN, no difference beyond the noise |
| host CPU-seconds | 300 | 301 | +0.3% | -2.87 to 4.39 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.25 | 2.23 | -0.6% | -0.0643 to 0.0357 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 98 | 106 | +8.1% | -37.8 to 53.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.2% | -3.42 to 2.58 | EVEN, no difference beyond the noise |
| queries a second | 3,934 | 3,926 | -0.2% | -68.4 to 51.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 407 | 522 | +28.4% | -981 to 1,213 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 837 | 859 | +2.6% | -1,358 to 1,402 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 82 | 93.8 | +14.4% | -165 to 188 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 143 | +11.6% | 8.24 to 21.6 | power given |
| pages holding data, mean (MB) | 122 | 137 | +12.6% | 9.59 to 21.1 | power given |
| pages read from disk into the pool (misses) | 1,662,620 | 1,587,330 | -4.5% | -160,247 to 9,666 | shown, not judged |
| host CPU busy (share of the run) | 0.219 | 0.218 | -0.6% | -0.018 to 0.0154 | EVEN, no difference beyond the noise |
| host CPU-seconds | 392 | 390 | -0.5% | -34 to 30 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 8.87 | 8.39 | -5.3% | -5.39 to 4.44 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.33 |  | 6.46 to 12.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,931 | 2,930 | -0.0% | -8.42 to 6.99 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,934 | 2,934 | -0.0% | -8.11 to 7.83 | EVEN, no difference beyond the noise |
| queries a second | 2,934 | 2,934 | -0.0% | -8.11 to 7.83 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.233 | 0.229 | -1.7% | -0.0139 to 0.00594 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.461 | 0.464 | +0.7% | -0.0207 to 0.0267 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.146 | 0.148 | +1.1% | -0.00745 to 0.0108 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 134 | +5.1% | -2.42 to 15.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 129 | +6.2% | -4 to 19 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,030,357 | 1,012,966 | -1.7% | -41,665 to 6,882 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.117 | -0.3% | -0.00496 to 0.00422 | EVEN, no difference beyond the noise |
| host CPU-seconds | 212 | 211 | -0.3% | -9.15 to 7.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.157 | 0.156 | -0.3% | -0.00709 to 0.00616 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 160 | 204 | +27.5% | -47.8 to 136 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 988 | -0.0% | -6.86 to 6.82 | EVEN, no difference beyond the noise |
| queries a second | 988 | 988 | -0.0% | -6.86 to 6.82 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 26.2 | +356.1% | -82.6 to 123 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,128 | 112 | -90.1% | -5,867 to 3,835 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 24.6 | 5.69 | -76.9% | -124 to 86.1 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.1% | 1.78 to 13.9 | power given |
| pages holding data, mean (MB) | 119 | 124 | +4.3% | 1.92 to 8.17 | power given |
| pages read from disk into the pool (misses) | 417,345 | 413,205 | -1.0% | -5,262 to -3,019 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.166 | -9.6% | -0.0429 to 0.0075 | EVEN, no difference beyond the noise |
| host CPU-seconds | 323 | 292 | -9.5% | -78.4 to 17.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.92 | 3.18 | -35.4% | -5.52 to 2.04 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
