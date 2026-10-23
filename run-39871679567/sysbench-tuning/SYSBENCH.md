# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,917 | 2,909 | -0.3% | -61.2 to 44.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,935 | 2,933 | -0.1% | -8.43 to 4.68 | EVEN, no difference beyond the noise |
| queries a second | 2,935 | 2,933 | -0.1% | -8.43 to 4.68 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.281 | 0.278 | -1.1% | -0.0585 to 0.0525 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.549 | 0.625 | +13.8% | -0.36 to 0.512 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.275 | +39.8% | -0.275 to 0.431 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 525 | +2.6% | -65.6 to 92.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 463 | -0.0% | -97.7 to 97.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,627 | 354,102 | -3.7% | -147,333 to 120,284 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.138 | +0.3% | -0.00302 to 0.00389 | EVEN, no difference beyond the noise |
| host CPU-seconds | 248 | 249 | +0.4% | -5.43 to 7.29 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.185 | 0.186 | +0.7% | -0.00662 to 0.00908 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.7 |  | 1.19 to 24.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
