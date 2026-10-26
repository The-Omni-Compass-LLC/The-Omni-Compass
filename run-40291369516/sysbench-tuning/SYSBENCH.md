# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,962 | 2,959 | -0.1% | -10.3 to 3.67 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,964 | 2,964 | -0.0% | -5.51 to 5.25 | EVEN, no difference beyond the noise |
| queries a second | 2,964 | 2,964 | -0.0% | -5.51 to 5.25 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.198 | 0.198 | -0.2% | -0.00906 to 0.00839 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.344 | 0.342 | -0.6% | -0.0106 to 0.00661 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.136 | 0.227 | +67.0% | -0.252 to 0.434 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 534 | +4.3% | -319 to 362 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 476 | +2.6% | -259 to 283 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,509 | 351,449 | -4.4% | -389,561 to 357,441 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.108 | +0.4% | -0.00212 to 0.00298 | EVEN, no difference beyond the noise |
| host CPU-seconds | 193 | 193 | +0.4% | -3.84 to 5.43 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.143 | +0.5% | -0.00241 to 0.00389 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 11.3 |  | -7.64 to 30.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
