# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 181 | 181 | +0.3% | -1.82 to 2.92 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.2% | -3.83 to 3.19 | EVEN, no difference beyond the noise |
| queries a second | 3,927 | 3,921 | -0.2% | -76.6 to 63.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 12.3 | 12.2 | -1.2% | -0.976 to 0.684 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 17.1 | 16.9 | -1.2% | -0.644 to 0.235 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.18 | 6.15 | -0.5% | -0.181 to 0.116 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 146 | +14.2% | 11.5 to 24.8 | power given |
| pages holding data, mean (MB) | 121 | 138 | +14.8% | 15.3 to 20.4 | power given |
| pages read from disk into the pool (misses) | 1,666,497 | 1,581,119 | -5.1% | -163,248 to -7,508 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.249 | -0.9% | -0.00613 to 0.00158 | EVEN, no difference beyond the noise |
| host CPU-seconds | 406 | 403 | -0.9% | -8.63 to 1.69 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.91 | 4.85 | -1.2% | -0.168 to 0.0536 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
