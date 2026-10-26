# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 279 | 282 | +1.4% | -9.48 to 17 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.3% | -1.67 to 3.46 | EVEN, no difference beyond the noise |
| queries a second | 4,710 | 4,725 | +0.3% | -26.7 to 55.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 14.6 | 7.57 | -48.1% | -46.3 to 32.3 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 114 | 104 | -9.3% | -283 to 262 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.39 | 5.44 | -14.9% | -12.9 to 11 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 489 | -4.5% | -171 to 125 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 445 | 431 | -3.1% | -125 to 97 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 245,091 | 241,710 | -1.4% | -60,246 to 53,484 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.164 | +0.9% | -0.00435 to 0.00736 | EVEN, no difference beyond the noise |
| host CPU-seconds | 97.4 | 98.4 | +1.0% | -2.94 to 4.88 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.3 | 2.29 | -0.4% | -0.178 to 0.159 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 3.52 to 8.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
