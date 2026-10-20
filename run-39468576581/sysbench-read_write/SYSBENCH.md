# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `80843e7684b3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 192 | +0.1% | -2.98 to 3.44 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.2% | -1.93 to 1.03 | EVEN, no difference beyond the noise |
| queries a second | 3,925 | 3,916 | -0.2% | -38.6 to 20.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.64 | 8.28 | -4.1% | -1.45 to 0.737 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.8 | 12.4 | -3.6% | -1.6 to 0.684 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.28 | 5.18 | -1.9% | -0.384 to 0.182 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 609 | +19.0% | 32 to 162 | power given |
| pages holding data, mean (MB) | 462 | 514 | +11.2% | 14.1 to 89.2 | power given |
| pages read from disk into the pool (misses) | 612,637 | 505,974 | -17.4% | -152,265 to -61,060 | shown, not judged |
| host CPU busy (share of the run) | 0.283 | 0.276 | -2.6% | -0.0157 to 0.0011 | EVEN, no difference beyond the noise |
| host CPU-seconds | 498 | 485 | -2.6% | -27.5 to 1.97 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.67 | 5.52 | -2.7% | -0.404 to 0.101 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18 |  | 9.04 to 27 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
