# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,946 | 2,950 | +0.1% | -3.29 to 11.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,950 | 2,954 | +0.1% | -4.34 to 12.8 | EVEN, no difference beyond the noise |
| queries a second | 2,950 | 2,954 | +0.1% | -4.34 to 12.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.314 | 0.313 | -0.5% | -0.00884 to 0.00551 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.432 | 0.435 | +0.6% | -0.00881 to 0.0141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.191 | -0.9% | -0.00588 to 0.00245 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 464 | 461 | -0.7% | -17.9 to 11.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,578 | 364,818 | -0.8% | -18,850 to 13,330 | shown, not judged |
| host CPU busy (share of the run) | 0.157 | 0.157 | -0.3% | -0.00342 to 0.0025 | EVEN, no difference beyond the noise |
| host CPU-seconds | 277 | 276 | -0.2% | -5.85 to 4.49 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.205 | 0.205 | -0.4% | -0.00432 to 0.0028 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
