# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 24.5 | 26.2 | +7.2% | -9.05 to 12.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 985 | 984 | -0.0% | -5.8 to 5.04 | EVEN, no difference beyond the noise |
| queries a second | 985 | 984 | -0.0% | -5.8 to 5.04 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.57 | 1.54 | -2.0% | -0.225 to 0.163 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.95 | 2.99 | +1.5% | -1.13 to 1.22 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.15 | 1.13 | -2.0% | -0.644 to 0.599 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 485 | -5.3% | -69.8 to 15.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 452 | 408 | -9.8% | -101 to 11.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,942 | 215,288 | +13.3% | -14,135 to 64,826 | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.217 | -1.8% | -0.0344 to 0.0266 | EVEN, no difference beyond the noise |
| host CPU-seconds | 387 | 380 | -1.8% | -60.3 to 46.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 36.4 | 32.1 | -11.7% | -26.5 to 18 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
