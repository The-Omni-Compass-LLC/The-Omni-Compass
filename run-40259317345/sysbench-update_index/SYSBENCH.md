# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.46 | 2.93 | -15.4% | -4.39 to 3.33 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 981 | 981 | +0.0% | -6.13 to 6.79 | EVEN, no difference beyond the noise |
| queries a second | 981 | 981 | +0.0% | -6.13 to 6.79 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.94 | 1.88 | -3.2% | -0.631 to 0.507 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.01 | 3.59 | -10.4% | -4.33 to 3.49 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.14 | 1.17 | +2.8% | -0.258 to 0.322 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 128 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 119 | 118 | -1.0% | -2.63 to 0.372 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 414,971 | 413,991 | -0.2% | -10,452 to 8,492 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.173 | +0.2% | -0.023 to 0.0237 | EVEN, no difference beyond the noise |
| host CPU-seconds | 309 | 310 | +0.2% | -40.6 to 41.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 223 | 232 | +4.0% | -290 to 308 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
