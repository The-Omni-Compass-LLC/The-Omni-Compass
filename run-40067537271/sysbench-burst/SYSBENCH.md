# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | -0.1% | -4.32 to 3.83 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 293 | -0.2% | -4.98 to 3.78 | EVEN, no difference beyond the noise |
| queries a second | 4,699 | 4,690 | -0.2% | -79.7 to 60.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.37 | 5.28 | -1.8% | -0.331 to 0.141 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.34 | 7.17 | -2.3% | -0.984 to 0.641 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.43 | 3.38 | -1.4% | -0.112 to 0.0153 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 147 | +14.7% | -1.55 to 39.2 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 120 | 145 | +20.6% | 8.61 to 40.9 | power given |
| pages read from disk into the pool (misses) | 576,142 | 536,355 | -6.9% | -90,565 to 10,992 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.203 | -0.4% | -0.0102 to 0.00869 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 112 | -0.4% | -5.81 to 4.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.52 | 2.52 | -0.3% | -0.11 to 0.0932 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
