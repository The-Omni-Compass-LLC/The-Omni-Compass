# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 291 | +0.5% | -0.0916 to 2.75 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.2% | -2.6 to 3.79 | EVEN, no difference beyond the noise |
| queries a second | 4,682 | 4,691 | +0.2% | -41.6 to 60.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.68 | 5.47 | -3.6% | -0.885 to 0.475 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.28 | 7.89 | -4.8% | -1.18 to 0.396 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.4 | 3.33 | -2.1% | -0.377 to 0.231 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 522 | +2.0% | -52.9 to 72.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 446 | 424 | -5.0% | -86.1 to 41.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 241,863 | 241,499 | -0.2% | -42,845 to 42,118 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.188 | +1.6% | -0.00236 to 0.00817 | EVEN, no difference beyond the noise |
| host CPU-seconds | 102 | 104 | +1.7% | -1.25 to 4.63 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.3 | 2.33 | +1.2% | -0.0294 to 0.0851 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.33 |  | 4.9 to 7.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
