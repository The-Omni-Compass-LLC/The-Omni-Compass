# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 289 | 288 | -0.6% | -20 to 16.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 297 | 296 | -0.4% | -7.14 to 4.83 | EVEN, no difference beyond the noise |
| queries a second | 4,747 | 4,728 | -0.4% | -114 to 77.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.6 | 4.63 | +0.6% | -1.92 to 1.97 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 52 | 48.1 | -7.5% | -101 to 93 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.74 | 3.54 | -5.2% | -2.25 to 1.86 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 501 | -2.1% | -48 to 26.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 451 | +0.5% | -26.7 to 31.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 246,524 | 226,998 | -7.9% | -23,982 to -15,071 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.178 | -0.7% | -0.009 to 0.00635 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 108 | -0.9% | -5.46 to 3.53 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.47 | 2.46 | -0.2% | -0.131 to 0.122 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 |  | 6.9 to 9.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
