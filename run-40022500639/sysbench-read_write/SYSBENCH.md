# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 192 | -0.5% | -3.63 to 1.61 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.4% | -3.72 to 2.18 | EVEN, no difference beyond the noise |
| queries a second | 3,933 | 3,918 | -0.4% | -74.3 to 43.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.28 | 8.38 | +1.2% | -0.835 to 1.04 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.3 | 12.4 | +0.6% | -1.07 to 1.22 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.28 | 5.25 | -0.5% | -0.153 to 0.0999 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 517 | +0.9% | -22.8 to 32.2 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 461 | -0.2% | -37.5 to 35.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,847 | 613,531 | -0.5% | -98,041 to 91,410 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.212 | -1.8% | -0.00722 to -0.000698 | GAIN |
| host CPU-seconds | 348 | 342 | -1.7% | -12.5 to 0.623 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.94 | 3.9 | -1.2% | -0.172 to 0.0783 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 11.8 to 17.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
