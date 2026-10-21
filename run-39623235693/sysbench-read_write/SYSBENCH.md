# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 193 | +1.0% | 0.854 to 3.13 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.6% | -0.893 to 3.13 | EVEN, no difference beyond the noise |
| queries a second | 3,920 | 3,942 | +0.6% | -17.9 to 62.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.01 | 8.58 | -4.7% | -1.04 to 0.188 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.6 | 12.9 | -5.3% | -2.53 to 1.08 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.44 | 5.33 | -1.9% | -0.626 to 0.421 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 612 | +19.5% | 19.2 to 181 | power given |
| pages holding data, mean (MB) | 461 | 535 | +16.1% | 44.7 to 104 | power given |
| pages read from disk into the pool (misses) | 616,755 | 471,366 | -23.6% | -243,524 to -47,255 | shown, not judged |
| host CPU busy (share of the run) | 0.28 | 0.279 | -0.4% | -0.00371 to 0.0017 | EVEN, no difference beyond the noise |
| host CPU-seconds | 493 | 491 | -0.4% | -6.53 to 3.01 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.65 | 5.57 | -1.4% | -0.116 to -0.0417 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 17.7 |  | 10.5 to 24.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
