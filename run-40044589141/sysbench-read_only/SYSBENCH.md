# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 295 | -0.2% | -2.97 to 2.04 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.1% | -2.94 to 2.11 | EVEN, no difference beyond the noise |
| queries a second | 4,722 | 4,716 | -0.1% | -47.1 to 33.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.08 | 4 | -1.8% | -0.253 to 0.107 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.47 | 5.34 | -2.4% | -0.41 to 0.15 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.18 | 3.15 | -0.8% | -0.0851 to 0.0324 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 599 | +17.0% | -49.8 to 224 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 518 | +12.3% | -32.3 to 146 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,702 | 493,630 | -24.6% | -459,021 to 136,875 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.189 | -0.7% | -0.00667 to 0.00388 | EVEN, no difference beyond the noise |
| host CPU-seconds | 314 | 312 | -0.7% | -11.6 to 7.23 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.32 | -0.6% | -0.0951 to 0.0694 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19 |  | 12.4 to 25.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
