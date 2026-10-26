# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,944 | 2,947 | +0.1% | 1.06 to 4.11 | GAIN |
| throughput (transactions a second) | 2,951 | 2,954 | +0.1% | 0.719 to 5.67 | GAIN |
| queries a second | 2,951 | 2,954 | +0.1% | 0.719 to 5.67 | GAIN |
| latency, 95th percentile (ms) | 0.346 | 0.348 | +0.6% | -0.0208 to 0.0248 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.451 | 0.453 | +0.6% | -0.00881 to 0.0141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.212 | +1.1% | -0.00873 to 0.0134 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 130 | +1.9% | 2.02 to 2.82 | power given |
| pages holding data, mean (MB) | 121 | 124 | +2.5% | -0.0195 to 6.04 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 1,028,019 | 1,020,820 | -0.7% | -8,659 to -5,738 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.114 | +1.8% | -0.00803 to 0.012 | EVEN, no difference beyond the noise |
| host CPU-seconds | 187 | 190 | +1.7% | -13.6 to 20.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.139 | 0.141 | +1.6% | -0.0102 to 0.0147 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
