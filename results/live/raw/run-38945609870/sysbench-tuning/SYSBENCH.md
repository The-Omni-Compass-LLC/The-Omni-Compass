# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,946 | 2,947 | +0.0% | -3.71 to 5.23 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,950 | 2,951 | +0.0% | -4.62 to 6.75 | EVEN, no difference beyond the noise |
| queries a second | 2,950 | 2,951 | +0.0% | -4.62 to 6.75 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.332 | 0.338 | +1.8% | -0.0334 to 0.0454 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.451 | 0.445 | -1.2% | -0.0554 to 0.0447 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.209 | +2.3% | -0.0158 to 0.025 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 483 | -5.7% | -112 to 53 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 428 | -7.7% | -137 to 65.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,574 | 410,943 | +12.1% | -141,547 to 230,284 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.107 | +4.1% | -0.0169 to 0.0253 | EVEN, no difference beyond the noise |
| host CPU-seconds | 171 | 178 | +4.3% | -28.7 to 43.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.127 | 0.132 | +4.2% | -0.0214 to 0.0321 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 3.49 to 17.8 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
