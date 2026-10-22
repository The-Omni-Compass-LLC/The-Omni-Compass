# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.3% | -3.48 to 1.96 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.2% | -3.6 to 2.24 | EVEN, no difference beyond the noise |
| queries a second | 4,705 | 4,694 | -0.2% | -57.7 to 35.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.82 | 4.77 | -1.2% | -0.306 to 0.19 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.59 | 6.71 | +1.8% | -0.183 to 0.424 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.18 | 3.17 | -0.0% | -0.0559 to 0.0542 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 505 | -1.4% | -45.7 to 31.2 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 439 | -1.8% | -124 to 108 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,409 | 244,801 | +0.2% | -35,875 to 36,659 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.18 | +0.8% | -0.0116 to 0.0144 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98.2 | 99.1 | +0.9% | -6.68 to 8.39 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.19 | 2.21 | +1.1% | -0.126 to 0.176 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
