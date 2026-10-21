# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,949 | 2,944 | -0.2% | -18.7 to 8.71 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,955 | 2,953 | -0.1% | -11.8 to 6.81 | EVEN, no difference beyond the noise |
| queries a second | 2,955 | 2,953 | -0.1% | -11.8 to 6.81 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.34 | 0.332 | -2.4% | -0.0653 to 0.0487 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.465 | 0.473 | +1.8% | -0.082 to 0.0987 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.214 | +7.3% | -0.00903 to 0.0383 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 674 | +31.6% | 107 to 217 | power given |
| pages holding data, mean (MB) | 464 | 560 | +20.7% | 39.2 to 153 | power given |
| pages read from disk into the pool (misses) | 368,666 | 246,841 | -33.0% | -147,197 to -96,454 | shown, not judged |
| host CPU busy (share of the run) | 0.162 | 0.164 | +1.3% | -0.017 to 0.0213 | EVEN, no difference beyond the noise |
| host CPU-seconds | 284 | 288 | +1.3% | -29.5 to 37.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.211 | 0.214 | +1.5% | -0.0225 to 0.0288 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18 |  | 4.85 to 31.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
