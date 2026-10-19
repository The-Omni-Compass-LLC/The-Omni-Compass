# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | -0.1% | -1.77 to 0.996 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.1% | -1.9 to 1.17 | EVEN, no difference beyond the noise |
| queries a second | 4,742 | 4,736 | -0.1% | -30.4 to 18.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.8 | 1.81 | +0.6% | -0.0341 to 0.0548 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.62 | 3.71 | +2.4% | -0.387 to 0.562 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.26 | +2.1% | -0.0424 to 0.0956 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.2% | 4.09 to 17 | power given |
| pages holding data, mean (MB) | 120 | 139 | +15.8% | 13.9 to 24 | power given |
| pages read from disk into the pool (misses) | 1,999,442 | 1,923,564 | -3.8% | -247,785 to 96,029 | shown, not judged |
| host CPU busy (share of the run) | 0.0976 | 0.1 | +2.7% | -0.00391 to 0.00911 | EVEN, no difference beyond the noise |
| host CPU-seconds | 175 | 180 | +2.7% | -7.19 to 16.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.3 | 1.34 | +2.8% | -0.0454 to 0.118 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
