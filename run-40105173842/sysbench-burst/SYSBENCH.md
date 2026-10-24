# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.2% | -4.52 to 5.77 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.1% | -4.34 to 5.05 | EVEN, no difference beyond the noise |
| queries a second | 4,700 | 4,705 | +0.1% | -69.4 to 80.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.12 | 5 | -2.4% | -0.593 to 0.349 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.04 | 6.83 | -2.9% | -0.987 to 0.573 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.3 | 3.28 | -0.4% | -0.105 to 0.0761 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 500 | -2.3% | -99.2 to 76 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 417 | -6.6% | -140 to 80.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,765 | 245,551 | -0.1% | -81,933 to 81,505 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.194 | +2.1% | -0.00142 to 0.00954 | EVEN, no difference beyond the noise |
| host CPU-seconds | 104 | 107 | +2.4% | -0.56 to 5.61 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.38 | +2.2% | 0.0238 to 0.0801 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 4.52 to 9.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
