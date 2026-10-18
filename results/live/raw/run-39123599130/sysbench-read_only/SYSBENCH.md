# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | -0.0% | -3.83 to 3.69 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.0% | -3.91 to 3.63 | EVEN, no difference beyond the noise |
| queries a second | 4,714 | 4,712 | -0.0% | -62.6 to 58.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.18 | 4.08 | -2.4% | -0.204 to 0.00537 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.06 | 5.84 | -3.5% | -0.481 to 0.0512 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.17 | 3.14 | -0.8% | -0.0385 to -0.00966 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 498 | -2.8% | -69.1 to 40.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 447 | -3.2% | -50.1 to 21 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,094 | 646,584 | -1.3% | -82,452 to 65,433 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.186 | -0.5% | -0.00317 to 0.00146 | EVEN, no difference beyond the noise |
| host CPU-seconds | 309 | 307 | -0.4% | -5.08 to 2.61 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.29 | 2.28 | -0.4% | -0.0201 to 0.00325 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 |  | 12.4 to 24.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
