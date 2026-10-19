# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,946 | 2,946 | -0.0% | -9.49 to 9.42 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,953 | +0.0% | -9.82 to 10.6 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,953 | +0.0% | -9.82 to 10.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.342 | 0.342 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 0.453 | 0.456 | +0.6% | -0.00881 to 0.0141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.208 | -0.4% | -0.00245 to 0.00086 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +8.1% | 4.15 to 16.7 | power given |
| pages holding data, mean (MB) | 121 | 134 | +10.6% | 7.24 to 18.4 | power given |
| pages read from disk into the pool (misses) | 1,028,978 | 994,835 | -3.3% | -66,610 to -1,677 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.11 | -0.7% | -0.00205 to 0.000483 | EVEN, no difference beyond the noise |
| host CPU-seconds | 184 | 183 | -0.8% | -3.69 to 0.788 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.137 | 0.136 | -0.8% | -0.0023 to 0.000161 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
