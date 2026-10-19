# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 0.0029 | 0.00218 | -25.0% | -0.012 to 0.0105 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 980 | 979 | -0.1% | -8.14 to 6.51 | EVEN, no difference beyond the noise |
| queries a second | 980 | 979 | -0.1% | -8.14 to 6.51 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.15 | 1.97 | -8.1% | -1.16 to 0.813 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.55 | 3.73 | -32.8% | -11.7 to 8.01 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.48 | 1.51 | +2.1% | -0.355 to 0.418 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 556 | +8.5% | -91.6 to 179 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 475 | +4.7% | -66.3 to 109 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 187,472 | 176,814 | -5.7% | -41,458 to 20,140 | shown, not judged |
| host CPU busy (share of the run) | 0.408 | 0.404 | -1.1% | -0.0279 to 0.0191 | EVEN, no difference beyond the noise |
| host CPU-seconds | 717 | 708 | -1.2% | -55.6 to 37.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 482,685 | 589,320 | +22.1% | -954,696 to 1,167,966 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | -2.31 to 35 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
