# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.3% | -2.21 to 0.564 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.2% | -1.92 to 0.624 | EVEN, no difference beyond the noise |
| queries a second | 4,722 | 4,712 | -0.2% | -30.7 to 9.99 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.15 | 4.23 | +1.8% | -0.112 to 0.263 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.13 | 6.28 | +2.4% | -0.273 to 0.567 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.11 | 3.07 | -1.1% | -0.128 to 0.057 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 930 | +81.6% | 144 to 692 | power given |
| pages holding data, mean (MB) | 464 | 823 | +77.1% | 126 to 591 | power given |
| pages read from disk into the pool (misses) | 657,382 | 167,519 | -74.5% | -644,140 to -335,586 | shown, not judged |
| host CPU busy (share of the run) | 0.243 | 0.24 | -1.2% | -0.00995 to 0.00401 | EVEN, no difference beyond the noise |
| host CPU-seconds | 432 | 427 | -1.2% | -17.8 to 7.24 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.21 | 3.18 | -1.0% | -0.115 to 0.054 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
