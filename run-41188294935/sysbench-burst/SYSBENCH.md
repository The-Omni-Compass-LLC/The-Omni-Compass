# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 291 | -1.1% | -17.1 to 10.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.2% | -5.88 to 4.49 | EVEN, no difference beyond the noise |
| queries a second | 4,745 | 4,733 | -0.2% | -94.1 to 71.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.54 | 3.67 | +3.6% | -1.19 to 1.44 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.14 | 41.9 | +414.2% | -73.4 to 141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.31 | 3.22 | +38.9% | -1.41 to 3.21 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,199 | +134.2% | 634 to 740 | power given |
| pages holding data, mean (MB) | 458 | 973 | +112.2% | 493 to 536 | power given |
| pages read from disk into the pool (misses) | 248,951 | 83,074 | -66.6% | -175,629 to -156,126 | shown, not judged |
| host CPU busy (share of the run) | 0.162 | 0.16 | -1.5% | -0.0038 to -0.00119 | GAIN |
| host CPU-seconds | 97.1 | 95.6 | -1.5% | -2.41 to -0.574 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.17 | 2.16 | -0.4% | -0.128 to 0.108 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
