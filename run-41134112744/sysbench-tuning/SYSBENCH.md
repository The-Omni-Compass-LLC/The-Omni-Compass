# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,953 | +0.1% | -15.6 to 23.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,965 | +0.0% | -5.2 to 5.24 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,965 | +0.0% | -5.2 to 5.24 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.226 | 0.215 | -4.7% | -0.0258 to 0.00451 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.4 | 0.386 | -3.4% | -0.082 to 0.0547 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.327 | 0.281 | -14.1% | -0.345 to 0.253 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,195 | +133.4% | 617 to 749 | power given |
| pages holding data, mean (MB) | 464 | 922 | +98.8% | 445 to 471 | power given |
| pages read from disk into the pool (misses) | 367,264 | 76,805 | -79.1% | -302,030 to -278,886 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.112 | -0.8% | -0.00812 to 0.00638 | EVEN, no difference beyond the noise |
| host CPU-seconds | 201 | 199 | -0.8% | -14.5 to 11.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.149 | 0.148 | -0.9% | -0.0118 to 0.00915 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
