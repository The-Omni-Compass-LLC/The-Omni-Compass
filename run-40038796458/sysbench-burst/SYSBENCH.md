# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 294 | -0.6% | -6.29 to 2.88 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 297 | 295 | -0.8% | -4.03 to -0.476 | LOSS |
| queries a second | 4,751 | 4,715 | -0.8% | -64.5 to -7.62 | LOSS |
| latency, 95th percentile (ms) | 3.24 | 3.08 | -5.0% | -1 to 0.676 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.07 | 4.68 | -7.7% | -2.26 to 1.48 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.49 | 1.44 | -3.6% | -0.39 to 0.284 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 133 | +3.9% | -5.78 to 15.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 126 | +4.8% | -6.26 to 17.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 570,238 | 550,176 | -3.5% | -97,471 to 57,346 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.105 | -0.3% | -0.0153 to 0.0146 | EVEN, no difference beyond the noise |
| host CPU-seconds | 63.3 | 63.1 | -0.3% | -9.24 to 8.84 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.41 | 1.41 | +0.3% | -0.208 to 0.216 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.33 |  | -1.54 to 4.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
