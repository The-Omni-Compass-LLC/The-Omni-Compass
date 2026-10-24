# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 333 | 256 | -22.9% | -231 to 78.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 987 | 988 | +0.0% | -0.984 to 1.89 | EVEN, no difference beyond the noise |
| queries a second | 987 | 988 | +0.0% | -0.984 to 1.89 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.37 | 2.51 | +6.1% | -1.18 to 1.47 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.97 | 5.72 | +15.0% | -1.9 to 3.4 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.877 | 0.997 | +13.7% | -0.166 to 0.407 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 461 | -9.9% | -195 to 93.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 403 | -11.0% | -179 to 79.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,780 | 217,277 | +15.1% | -33,179 to 90,175 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.121 | +7.0% | -0.0163 to 0.032 | EVEN, no difference beyond the noise |
| host CPU-seconds | 199 | 212 | +6.9% | -28.2 to 55.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.46 | 2.14 | +46.7% | -1.27 to 2.63 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.7 |  | 6.41 to 18.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
