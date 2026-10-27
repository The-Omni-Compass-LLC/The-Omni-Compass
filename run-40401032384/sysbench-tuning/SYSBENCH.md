# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,935 | 2,940 | +0.2% | -4.98 to 14.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,943 | 2,947 | +0.1% | -1.75 to 10.4 | EVEN, no difference beyond the noise |
| queries a second | 2,943 | 2,947 | +0.1% | -1.75 to 10.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.283 | 0.277 | -2.4% | -0.0138 to 0.000505 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.365 | 0.354 | -2.9% | -0.0348 to 0.0135 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.217 | -3.1% | -0.112 to 0.0977 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 569 | +11.1% | -63.3 to 176 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 513 | +10.9% | -16.9 to 118 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 264,047 | 213,339 | -19.2% | -122,748 to 21,333 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.114 | -2.5% | -0.00588 to 7.43e-05 | EVEN, no difference beyond the noise |
| host CPU-seconds | 140 | 137 | -2.5% | -7.23 to 0.206 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.156 | 0.152 | -2.6% | -0.00872 to 0.000454 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 3.43 to 16.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
