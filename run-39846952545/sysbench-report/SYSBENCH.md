# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | -0.1% | -1.79 to 1.26 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.1% | -2.62 to 2.13 | EVEN, no difference beyond the noise |
| queries a second | 4,743 | 4,739 | -0.1% | -41.9 to 34 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.47 | 3.16 | -9.1% | -1.34 to 0.707 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.15 | 4.68 | -9.0% | -2.46 to 1.53 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.57 | 1.45 | -7.2% | -0.439 to 0.214 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +8.0% | -28.4 to 48.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 131 | +8.9% | -30.5 to 51.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 573,124 | 560,712 | -2.2% | -106,091 to 81,269 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.104 | -8.9% | -0.0325 to 0.0121 | EVEN, no difference beyond the noise |
| host CPU-seconds | 68.7 | 62.5 | -9.0% | -19.1 to 6.85 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.52 | 1.39 | -8.7% | -0.43 to 0.164 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | -3.5 to 6.84 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | -0.1% | -4.1 to 3.35 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.1% | -4.1 to 3.51 | EVEN, no difference beyond the noise |
| queries a second | 4,743 | 4,738 | -0.1% | -65.6 to 56.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.83 | 1.85 | +0.6% | -0.197 to 0.221 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.86 | 3.73 | -3.6% | -0.48 to 0.203 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.28 | 1.28 | +0.6% | -0.158 to 0.173 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.8% | 1.61 to 13.3 | power given |
| pages holding data, mean (MB) | 120 | 135 | +12.6% | 8.64 to 21.7 | power given |
| pages read from disk into the pool (misses) | 1,979,125 | 1,914,811 | -3.2% | -148,143 to 19,513 | shown, not judged |
| host CPU busy (share of the run) | 0.0998 | 0.1 | +0.4% | -0.015 to 0.0157 | EVEN, no difference beyond the noise |
| host CPU-seconds | 179 | 180 | +0.4% | -26.8 to 28.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.33 | 1.33 | +0.5% | -0.18 to 0.193 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 1.03 to 11 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 191 | -0.8% | -8.84 to 5.66 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.5% | 0.213 to 1.66 | GAIN |
| queries a second | 3,938 | 3,957 | +0.5% | 4.26 to 33.2 | GAIN |
| latency, 95th percentile (ms) | 8.38 | 9.32 | +11.3% | -2.13 to 4.02 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 14.4 | 35.1 | +143.1% | -58.8 to 100 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.25 | 4.96 | +16.7% | -1.6 to 3.02 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +5.9% | 1.3 to 13.9 | power given |
| pages holding data, mean (MB) | 121 | 128 | +5.7% | 1.18 to 12.7 | power given |
| pages read from disk into the pool (misses) | 1,663,472 | 1,630,116 | -2.0% | -85,584 to 18,872 | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.204 | +0.7% | -0.00836 to 0.0113 | EVEN, no difference beyond the noise |
| host CPU-seconds | 358 | 361 | +0.7% | -14.8 to 19.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.08 | 4.14 | +1.6% | -0.102 to 0.23 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 1.03 to 11 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,960 | 2,961 | +0.0% | -25.3 to 26.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,964 | 2,965 | +0.0% | -24.2 to 26.5 | EVEN, no difference beyond the noise |
| queries a second | 2,964 | 2,965 | +0.0% | -24.2 to 26.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.191 | 0.191 | +0.0% | -0.0911 to 0.0911 | EVEN, the same |
| latency, 99th percentile (ms) | 0.304 | 0.302 | -0.5% | -0.0182 to 0.0149 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0857 | 0.0869 | +1.4% | -0.00268 to 0.00512 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 136 | +6.0% | -3.94 to 19.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 132 | +8.6% | -0.0694 to 21 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,030,200 | 1,010,682 | -1.9% | -66,479 to 27,442 | shown, not judged |
| host CPU busy (share of the run) | 0.0673 | 0.066 | -2.0% | -0.0141 to 0.0113 | EVEN, no difference beyond the noise |
| host CPU-seconds | 120 | 118 | -2.0% | -25.1 to 20.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0891 | 0.0873 | -2.1% | -0.0193 to 0.0156 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 4 | 4.71 | +17.8% | -3.12 to 4.54 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 985 | +0.1% | -1.32 to 3.23 | EVEN, no difference beyond the noise |
| queries a second | 984 | 985 | +0.1% | -1.32 to 3.23 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.15 | 2.25 | +4.8% | -0.766 to 0.971 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.96 | 4.42 | +11.4% | -3.06 to 3.97 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 1.37 | +16.4% | -0.706 to 1.09 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 144 | +12.4% | 9.6 to 22.1 | power given |
| pages holding data, mean (MB) | 119 | 130 | +9.3% | 3.65 to 18.4 | power given |
| pages read from disk into the pool (misses) | 415,638 | 405,297 | -2.5% | -17,973 to -2,709 | shown, not judged |
| host CPU busy (share of the run) | 0.186 | 0.23 | +23.7% | -0.132 to 0.22 | EVEN, no difference beyond the noise |
| host CPU-seconds | 287 | 356 | +24.1% | -207 to 346 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 181 | 171 | -5.2% | -184 to 165 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 8 to 8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
