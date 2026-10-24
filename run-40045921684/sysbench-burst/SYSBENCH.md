# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.0% | -3.66 to 3.72 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | -0.1% | -4.02 to 3.35 | EVEN, no difference beyond the noise |
| queries a second | 4,693 | 4,687 | -0.1% | -64.3 to 53.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.65 | 4.57 | -1.8% | -0.442 to 0.275 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.63 | 6.32 | -4.7% | -1.04 to 0.421 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.07 | 3.04 | -0.9% | -0.15 to 0.092 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 528 | +3.2% | -71.5 to 104 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 478 | +6.4% | -34 to 91.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,251 | 227,519 | -6.9% | -68,579 to 35,115 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.17 | -0.9% | -0.0034 to 0.000146 | EVEN, no difference beyond the noise |
| host CPU-seconds | 95.1 | 94.1 | -1.1% | -2.47 to 0.427 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.12 | 2.1 | -1.0% | -0.0703 to 0.0296 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 2.7 to 11.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
