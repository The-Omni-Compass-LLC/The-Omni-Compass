# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 192 | +1.1% | -0.832 to 4.88 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 197 | +0.5% | -1.06 to 2.93 | EVEN, no difference beyond the noise |
| queries a second | 3,923 | 3,942 | +0.5% | -21.2 to 58.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.18 | 8.58 | -6.4% | -1.12 to -0.0592 | GAIN |
| latency, 99th percentile (ms) | 13.5 | 12.8 | -4.7% | -1.01 to -0.254 | GAIN |
| latency, mean (ms) | 5.4 | 5.33 | -1.3% | -0.261 to 0.116 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 635 | +24.1% | 59.4 to 187 | power given |
| pages holding data, mean (MB) | 463 | 555 | +19.8% | 62.4 to 121 | power given |
| pages read from disk into the pool (misses) | 614,989 | 427,476 | -30.5% | -273,997 to -101,029 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.21 | -1.0% | -0.0081 to 0.00401 | EVEN, no difference beyond the noise |
| host CPU-seconds | 341 | 338 | -1.0% | -14.2 to 7.74 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.91 | 3.83 | -2.0% | -0.257 to 0.099 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19 |  | 9.06 to 28.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
