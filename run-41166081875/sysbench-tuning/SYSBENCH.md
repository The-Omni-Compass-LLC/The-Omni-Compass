# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,952 | 2,956 | +0.1% | -2.8 to 11.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,964 | 2,963 | -0.0% | -5.57 to 3.7 | EVEN, no difference beyond the noise |
| queries a second | 2,964 | 2,963 | -0.0% | -5.57 to 3.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.253 | 0.23 | -9.2% | -0.0464 to -0.00025 | GAIN |
| latency, 99th percentile (ms) | 0.372 | 0.361 | -3.0% | -0.0462 to 0.0242 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.27 | 0.185 | -31.5% | -0.275 to 0.105 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,181 | +823.0% | 950 to 1,156 | power given |
| pages holding data, mean (MB) | 121 | 905 | +646.4% | 750 to 817 | power given |
| pages read from disk into the pool (misses) | 1,030,291 | 88,760 | -91.4% | -975,432 to -907,630 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.112 | -6.7% | -0.0172 to 0.00107 | EVEN, no difference beyond the noise |
| host CPU-seconds | 213 | 199 | -6.7% | -30.3 to 1.91 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.159 | 0.148 | -6.8% | -0.0224 to 0.000818 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9.67 |  | -0.374 to 19.7 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
