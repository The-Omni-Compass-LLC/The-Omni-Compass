# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.3% | -2.6 to 4.55 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.3% | -2.33 to 4.22 | EVEN, no difference beyond the noise |
| queries a second | 4,686 | 4,701 | +0.3% | -37.3 to 67.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.06 | 5 | -1.2% | -0.191 to 0.0699 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.79 | 6.71 | -1.2% | -0.543 to 0.38 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.32 | 3.29 | -1.1% | -0.0727 to -4.79e-05 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.4% | 1.63 to 19.8 | power given |
| pages holding data, mean (MB) | 120 | 136 | +13.4% | 14.8 to 17.4 | power given |
| pages read from disk into the pool (misses) | 576,209 | 548,696 | -4.8% | -70,560 to 15,534 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.194 | -1.0% | -0.0107 to 0.00655 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 107 | -1.2% | -6.15 to 3.63 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.43 | 2.39 | -1.5% | -0.121 to 0.0488 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
