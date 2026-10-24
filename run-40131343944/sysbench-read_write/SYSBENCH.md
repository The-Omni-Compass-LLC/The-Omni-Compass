# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 144 | 157 | +8.9% | -26.4 to 52 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.4% | -3.97 to 2.52 | EVEN, no difference beyond the noise |
| queries a second | 3,955 | 3,941 | -0.4% | -79.5 to 50.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 148 | 109 | -26.1% | -168 to 91.4 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 355 | 295 | -16.7% | -466 to 347 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 29.3 | 21.7 | -25.8% | -35.8 to 20.7 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 480 | -6.2% | -82.5 to 18.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 429 | -7.0% | -59.7 to -5.17 | GAIN |
| pages read from disk into the pool (misses) | 617,284 | 692,914 | +12.3% | -70,398 to 221,657 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.182 | +0.3% | -0.00542 to 0.00637 | EVEN, no difference beyond the noise |
| host CPU-seconds | 324 | 324 | +0.2% | -8.15 to 9.33 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.94 | 4.56 | -7.8% | -1.47 to 0.696 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17.7 |  | 11.4 to 23.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
