# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 187 | 186 | -0.4% | -13.7 to 12.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 195 | -0.9% | -4.34 to 0.982 | EVEN, no difference beyond the noise |
| queries a second | 3,940 | 3,907 | -0.9% | -86.8 to 19.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 10.8 | 10.4 | -3.6% | -6.22 to 5.45 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 19.1 | 20.4 | +6.5% | -26.1 to 28.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.11 | 6.14 | +0.4% | -2.31 to 2.35 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 581 | +13.5% | -68 to 206 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 513 | +11.3% | -56 to 160 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 618,102 | 501,006 | -18.9% | -358,663 to 124,471 | shown, not judged |
| host CPU busy (share of the run) | 0.241 | 0.226 | -6.0% | -0.0571 to 0.0285 | EVEN, no difference beyond the noise |
| host CPU-seconds | 388 | 365 | -5.9% | -93.8 to 47.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.53 | 4.28 | -5.4% | -1.37 to 0.879 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 11 to 21 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
