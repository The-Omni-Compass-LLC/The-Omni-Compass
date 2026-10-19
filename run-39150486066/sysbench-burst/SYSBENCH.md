# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | -0.0% | -4.2 to 4.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.0% | -4.33 to 4.14 | EVEN, no difference beyond the noise |
| queries a second | 4,700 | 4,699 | -0.0% | -69.3 to 66.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.09 | 5.12 | +0.6% | -0.102 to 0.164 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.79 | 6.83 | +0.6% | -0.308 to 0.392 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.38 | 3.37 | -0.3% | -0.0616 to 0.0399 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.5% | -0.0902 to 19.2 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 135 | +12.2% | 10.4 to 19 | power given |
| pages read from disk into the pool (misses) | 572,588 | 543,189 | -5.1% | -94,336 to 35,538 | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.201 | -0.2% | -0.00513 to 0.00431 | EVEN, no difference beyond the noise |
| host CPU-seconds | 112 | 112 | -0.3% | -2.79 to 2.18 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.5 | 2.49 | -0.2% | -0.0304 to 0.0182 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
