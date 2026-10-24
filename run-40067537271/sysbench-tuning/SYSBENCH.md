# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,957 | 2,955 | -0.1% | -32 to 28.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,967 | +0.1% | -12.9 to 16.5 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,967 | +0.1% | -12.9 to 16.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.237 | 0.237 | +0.0% | -0.00994 to 0.00994 | EVEN, the same |
| latency, 99th percentile (ms) | 0.354 | 0.357 | +0.7% | -0.0493 to 0.054 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.225 | 0.275 | +21.9% | -0.266 to 0.365 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 133 | +3.9% | 5.05 to 5.05 | power given |
| pages holding data, mean (MB) | 121 | 128 | +5.5% | 2.19 to 11.2 | power given |
| pages read from disk into the pool (misses) | 1,029,140 | 1,016,269 | -1.3% | -16,391 to -9,350 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.115 | +1.0% | -0.00269 to 0.00494 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 205 | +1.0% | -4.82 to 8.78 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.151 | 0.152 | +1.0% | -0.00369 to 0.00685 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
