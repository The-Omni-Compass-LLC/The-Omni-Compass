# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.3% | -8.48 to 6.81 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.2% | -4.38 to 3.28 | EVEN, no difference beyond the noise |
| queries a second | 4,711 | 4,702 | -0.2% | -70.1 to 52.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.25 | 5.31 | +1.1% | -1.32 to 1.43 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.45 | 7.58 | +1.8% | -2.79 to 3.06 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.31 | 3.31 | +0.1% | -0.181 to 0.187 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 520 | +1.6% | -96.9 to 113 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 459 | +2.3% | -101 to 121 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,185 | 232,589 | -5.1% | -64,023 to 38,833 | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.19 | +0.9% | -0.0056 to 0.00907 | EVEN, no difference beyond the noise |
| host CPU-seconds | 104 | 105 | +1.1% | -3.07 to 5.32 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.32 | 2.35 | +1.4% | -0.0157 to 0.0791 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | -1.39 to 16.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
