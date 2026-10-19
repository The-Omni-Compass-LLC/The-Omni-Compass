# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.2% | -2.78 to 4.05 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.2% | -2.55 to 3.73 | EVEN, no difference beyond the noise |
| queries a second | 4,688 | 4,698 | +0.2% | -40.7 to 59.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.31 | 5.31 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 7.3 | 7.3 | +0.0% | -0.326 to 0.328 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.4 | 3.38 | -0.7% | -0.115 to 0.0704 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.5% | -1.26 to 20.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 133 | +10.4% | 1.84 to 23.1 | power given |
| pages read from disk into the pool (misses) | 578,402 | 539,224 | -6.8% | -60,837 to -17,520 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.2 | -1.3% | -0.00986 to 0.00439 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 111 | -1.6% | -6.35 to 2.81 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.52 | 2.48 | -1.7% | -0.166 to 0.0802 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
