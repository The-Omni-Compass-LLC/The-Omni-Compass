# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 293 | +0.6% | -1.04 to 4.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.6% | -0.12 to 3.73 | EVEN, no difference beyond the noise |
| queries a second | 4,698 | 4,727 | +0.6% | -1.91 to 59.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.57 | 5.57 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 99th percentile (ms) | 8.08 | 8.03 | -0.6% | -0.602 to 0.504 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.44 | 3.41 | -0.9% | -0.202 to 0.14 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.4% | 5.68 to 8.21 | power given |
| pages holding data, mean (MB) | 120 | 130 | +8.0% | 8.01 to 11.1 | power given |
| pages read from disk into the pool (misses) | 572,987 | 560,449 | -2.2% | -23,272 to -1,803 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.2 | +1.8% | -0.0044 to 0.0117 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 111 | +1.9% | -2.65 to 6.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.45 | 2.48 | +1.2% | -0.0954 to 0.155 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
