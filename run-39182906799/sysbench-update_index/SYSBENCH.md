# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `bc2eb38f4ca8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.5 | 3.21 | -8.3% | -4.66 to 4.07 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 983 | -0.1% | -2.37 to -0.496 | LOSS |
| queries a second | 984 | 983 | -0.1% | -2.37 to -0.496 | LOSS |
| latency, 95th percentile (ms) | 1.9 | 1.85 | -2.6% | -0.509 to 0.411 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.3 | 3.73 | -13.2% | -3.45 to 2.32 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.45 | 1.17 | -19.4% | -1.58 to 1.02 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 575 | +12.3% | -80.1 to 206 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 485 | +6.8% | -14.2 to 75.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,348 | 174,146 | -8.0% | -42,640 to 12,238 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.124 | -1.2% | -0.017 to 0.0139 | EVEN, no difference beyond the noise |
| host CPU-seconds | 193 | 191 | -1.2% | -25.7 to 21.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 124 | 156 | +25.4% | -219 to 282 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 |  | -0.964 to 37.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
