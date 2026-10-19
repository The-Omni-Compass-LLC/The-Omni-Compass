# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.5% | -5.25 to 2.29 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 294 | -0.5% | -4.96 to 2.22 | EVEN, no difference beyond the noise |
| queries a second | 4,728 | 4,706 | -0.5% | -79.4 to 35.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.41 | 4.2 | -4.7% | -0.315 to -0.0967 | GAIN |
| latency, 99th percentile (ms) | 5.88 | 5.67 | -3.5% | -0.461 to 0.0461 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.38 | 3.28 | -2.8% | -0.144 to -0.0432 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 484 | -5.4% | -178 to 122 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 436 | -5.6% | -177 to 126 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,351 | 705,979 | +7.7% | -344,807 to 446,063 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.201 | -3.7% | -0.0104 to -0.0048 | GAIN |
| host CPU-seconds | 346 | 333 | -3.5% | -16.7 to -7.8 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.56 | 2.48 | -3.0% | -0.121 to -0.0352 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 12.5 to 18.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
