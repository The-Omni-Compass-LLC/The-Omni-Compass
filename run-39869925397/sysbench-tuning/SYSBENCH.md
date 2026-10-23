# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,946 | 2,945 | -0.0% | -4.18 to 2.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,950 | -0.1% | -8.45 to 3.48 | EVEN, no difference beyond the noise |
| queries a second | 2,953 | 2,950 | -0.1% | -8.45 to 3.48 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.361 | 0.334 | -7.4% | -0.0751 to 0.0218 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.476 | 0.448 | -5.7% | -0.074 to 0.0193 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.213 | 0.205 | -4.0% | -0.0325 to 0.0154 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 513 | +0.2% | -48 to 50.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 456 | -1.6% | -34.7 to 20.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,773 | 374,530 | +2.1% | -60,142 to 75,656 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.104 | -8.1% | -0.0319 to 0.0135 | EVEN, no difference beyond the noise |
| host CPU-seconds | 188 | 173 | -8.2% | -53.7 to 22.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.14 | 0.128 | -8.2% | -0.0396 to 0.0168 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | 4.43 to 17.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
