# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 189 | -0.2% | -1.67 to 0.781 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.4% | -1.74 to -0.00619 | LOSS |
| queries a second | 3,935 | 3,918 | -0.4% | -34.8 to -0.124 | LOSS |
| latency, 95th percentile (ms) | 9.85 | 9.62 | -2.4% | -0.484 to 0.0177 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.9 | 13.6 | -1.8% | -1.32 to 0.815 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.15 | 5.1 | -1.0% | -0.136 to 0.0294 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 141 | +10.4% | 10.4 to 16.1 | power given |
| pages holding data, mean (MB) | 120 | 132 | +10.0% | 3.18 to 20.9 | power given |
| pages read from disk into the pool (misses) | 1,667,496 | 1,597,945 | -4.2% | -119,690 to -19,412 | shown, not judged |
| host CPU busy (share of the run) | 0.28 | 0.277 | -1.1% | -0.00679 to 0.000355 | EVEN, no difference beyond the noise |
| host CPU-seconds | 494 | 489 | -1.1% | -11.6 to 0.524 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.69 | 5.64 | -0.9% | -0.156 to 0.0551 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 7.8 to 13.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
