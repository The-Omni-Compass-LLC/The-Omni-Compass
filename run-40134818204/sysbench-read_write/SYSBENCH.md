# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `7743f2e82851`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 192 | +0.4% | -1.69 to 3.04 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 197 | +0.0% | -2.32 to 2.46 | EVEN, no difference beyond the noise |
| queries a second | 3,930 | 3,931 | +0.0% | -46.5 to 49.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.74 | 8.43 | -3.5% | -0.69 to 0.0725 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.1 | 12.6 | -4.1% | -1.74 to 0.663 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.34 | 5.32 | -0.3% | -0.169 to 0.136 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 654 | +27.8% | 37.4 to 247 | power given |
| pages holding data, mean (MB) | 462 | 557 | +20.7% | 8.24 to 183 | power given |
| pages read from disk into the pool (misses) | 615,056 | 436,215 | -29.1% | -351,621 to -6,061 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.21 | +0.7% | -0.00511 to 0.00822 | EVEN, no difference beyond the noise |
| host CPU-seconds | 335 | 338 | +0.9% | -7.16 to 13.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.82 | 3.84 | +0.5% | -0.102 to 0.143 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 23 |  | 18.7 to 27.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
