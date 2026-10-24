# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | -0.1% | -3.69 to 2.91 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.1% | -3.68 to 2.89 | EVEN, no difference beyond the noise |
| queries a second | 4,707 | 4,701 | -0.1% | -58.8 to 46.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.06 | 2.97 | -3.0% | -0.297 to 0.117 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.05 | 3.98 | -1.8% | -0.0778 to -0.0675 | GAIN |
| latency, mean (ms) | 2.38 | 2.31 | -2.7% | -0.213 to 0.0868 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.8% | 7.03 to 7.8 | power given |
| pages holding data, mean (MB) | 120 | 135 | +12.0% | 12.3 to 16.6 | power given |
| pages read from disk into the pool (misses) | 1,984,537 | 1,936,544 | -2.4% | -192,501 to 96,517 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.186 | -2.6% | -0.0169 to 0.00711 | EVEN, no difference beyond the noise |
| host CPU-seconds | 346 | 338 | -2.5% | -30.1 to 12.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.56 | 2.5 | -2.4% | -0.22 to 0.0971 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
