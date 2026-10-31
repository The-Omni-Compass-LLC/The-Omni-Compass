# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 297 | +0.3% | -0.707 to 2.55 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.3% | -0.721 to 2.57 | EVEN, no difference beyond the noise |
| queries a second | 4,735 | 4,749 | +0.3% | -11.5 to 41.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.69 | 1.74 | +3.0% | 0.00543 to 0.0972 | LOSS |
| latency, 99th percentile (ms) | 2.98 | 3.15 | +5.5% | -0.0695 to 0.4 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.21 | +0.2% | -0.0667 to 0.0714 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 587 | +14.6% | -247 to 397 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 521 | +12.4% | -209 to 325 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,794 | 541,461 | -17.2% | -588,001 to 363,337 | shown, not judged |
| host CPU busy (share of the run) | 0.0971 | 0.0976 | +0.5% | -0.00722 to 0.00817 | EVEN, no difference beyond the noise |
| host CPU-seconds | 175 | 175 | +0.5% | -13.1 to 14.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.3 | 1.3 | +0.2% | -0.101 to 0.106 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.667 |  | -2.2 to 3.54 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
