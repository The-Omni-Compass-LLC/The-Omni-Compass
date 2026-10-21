# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.3% | -3.23 to 1.31 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.3% | -3.33 to 1.38 | EVEN, no difference beyond the noise |
| queries a second | 4,731 | 4,715 | -0.3% | -53.3 to 22 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.25 | 4.25 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 5.81 | 5.77 | -0.6% | -0.186 to 0.116 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.32 | 3.31 | -0.3% | -0.0372 to 0.0201 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 137 | +7.3% | 4.64 to 14 | power given |
| pages holding data, mean (MB) | 120 | 136 | +13.1% | 6.98 to 24.4 | power given |
| pages read from disk into the pool (misses) | 1,985,776 | 1,908,332 | -3.9% | -184,450 to 29,562 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.207 | -0.3% | -0.00341 to 0.0022 | EVEN, no difference beyond the noise |
| host CPU-seconds | 347 | 346 | -0.3% | -5.9 to 4.09 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.56 | 2.57 | +0.1% | -0.0468 to 0.0499 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
