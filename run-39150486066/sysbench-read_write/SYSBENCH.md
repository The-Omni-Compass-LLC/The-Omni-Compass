# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `c1c1b59711b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 196 | +0.2% | -4 to 4.65 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 198 | +0.1% | -4.03 to 4.43 | EVEN, no difference beyond the noise |
| queries a second | 3,955 | 3,959 | +0.1% | -80.7 to 88.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.89 | 7.84 | -0.6% | -0.253 to 0.157 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 11.2 | 11.1 | -0.6% | -0.355 to 0.221 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.97 | 4.01 | +1.1% | -0.102 to 0.187 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.5% | 2.66 to 11.4 | power given |
| pages holding data, mean (MB) | 122 | 127 | +4.2% | 3.15 to 7.19 | power given |
| pages read from disk into the pool (misses) | 1,670,787 | 1,639,449 | -1.9% | -139,779 to 77,102 | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.201 | +0.1% | -0.00556 to 0.00577 | EVEN, no difference beyond the noise |
| host CPU-seconds | 356 | 356 | +0.1% | -9.33 to 9.79 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4 | 3.99 | -0.1% | -0.0637 to 0.0556 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
