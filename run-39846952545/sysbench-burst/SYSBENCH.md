# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | -0.1% | -1.79 to 1.26 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.1% | -2.62 to 2.13 | EVEN, no difference beyond the noise |
| queries a second | 4,743 | 4,739 | -0.1% | -41.9 to 34 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.47 | 3.16 | -9.1% | -1.34 to 0.707 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.15 | 4.68 | -9.0% | -2.46 to 1.53 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.57 | 1.45 | -7.2% | -0.439 to 0.214 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +8.0% | -28.4 to 48.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 131 | +8.9% | -30.5 to 51.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 573,124 | 560,712 | -2.2% | -106,091 to 81,269 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.104 | -8.9% | -0.0325 to 0.0121 | EVEN, no difference beyond the noise |
| host CPU-seconds | 68.7 | 62.5 | -9.0% | -19.1 to 6.85 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.52 | 1.39 | -8.7% | -0.43 to 0.164 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | -3.5 to 6.84 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
