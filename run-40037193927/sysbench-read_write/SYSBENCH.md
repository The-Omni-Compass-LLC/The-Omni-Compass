# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | +0.1% | -1.66 to 2.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.1% | -1.44 to 1.08 | EVEN, no difference beyond the noise |
| queries a second | 3,945 | 3,941 | -0.1% | -28.8 to 21.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.33 | 8.03 | -3.5% | -1.26 to 0.671 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.3 | 12 | -2.3% | -1.95 to 1.37 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.3 | 5.21 | -1.6% | -0.331 to 0.158 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 579 | +13.1% | 32.4 to 101 | power given |
| pages holding data, mean (MB) | 462 | 508 | +9.9% | 4.69 to 86.7 | power given |
| pages read from disk into the pool (misses) | 617,647 | 522,957 | -15.3% | -105,547 to -83,833 | shown, not judged |
| host CPU busy (share of the run) | 0.217 | 0.211 | -2.8% | -0.0193 to 0.00712 | EVEN, no difference beyond the noise |
| host CPU-seconds | 349 | 340 | -2.8% | -31.7 to 12.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.95 | 3.84 | -2.9% | -0.401 to 0.173 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 |  | 10.3 to 26.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
