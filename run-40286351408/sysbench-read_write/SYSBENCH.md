# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 196 | +0.3% | -1.76 to 3.06 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.1% | -1.1 to 1.49 | EVEN, no difference beyond the noise |
| queries a second | 3,935 | 3,939 | +0.1% | -22.1 to 29.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.78 | 5.71 | -1.2% | -1.14 to 1 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.6 | 9.29 | -12.0% | -7.09 to 4.55 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.74 | 3.63 | -2.8% | -0.913 to 0.704 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 549 | +7.2% | -128 to 201 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 498 | +8.0% | -102 to 175 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,325 | 542,358 | -11.7% | -298,936 to 155,002 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.18 | +0.0% | -0.00323 to 0.00333 | EVEN, no difference beyond the noise |
| host CPU-seconds | 318 | 319 | +0.1% | -6.9 to 7.34 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.58 | 3.57 | -0.3% | -0.0767 to 0.0587 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | 3.04 to 21 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
