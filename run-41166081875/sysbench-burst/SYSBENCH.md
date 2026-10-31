# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.3% | -7.92 to 6.18 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.0% | -5.39 to 5.42 | EVEN, no difference beyond the noise |
| queries a second | 4,692 | 4,693 | +0.0% | -86.2 to 86.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.09 | 5.19 | +2.0% | -0.506 to 0.705 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.91 | 7.45 | +7.7% | -0.67 to 1.74 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.25 | 3.16 | -2.8% | -0.206 to 0.0267 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 977 | +663.2% | 616 to 1,081 | power given |
| pages holding data, mean (MB) | 121 | 862 | +610.5% | 607 to 874 | power given |
| pages read from disk into the pool (misses) | 603,096 | 106,694 | -82.3% | -581,695 to -411,109 | shown, not judged |
| host CPU busy (share of the run) | 0.249 | 0.242 | -3.0% | -0.00931 to -0.0055 | GAIN |
| host CPU-seconds | 148 | 144 | -3.0% | -5.54 to -3.36 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 3.31 | 3.22 | -2.7% | -0.156 to -0.0222 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
