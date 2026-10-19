# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 189 | 190 | +0.4% | -3.8 to 5.19 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.0% | -3.56 to 3.75 | EVEN, no difference beyond the noise |
| queries a second | 3,916 | 3,917 | +0.0% | -71.2 to 75 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.39 | 9.22 | -1.8% | -0.579 to 0.246 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 125 | 55.8 | -55.5% | -252 to 113 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7.65 | 6.46 | -15.5% | -3.54 to 1.16 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 137 | +7.2% | 5.59 to 12.8 | power given |
| pages holding data, mean (MB) | 121 | 130 | +6.9% | 5.95 to 10.9 | power given |
| pages read from disk into the pool (misses) | 1,662,650 | 1,623,984 | -2.3% | -106,343 to 29,010 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.194 | +1.6% | -0.0117 to 0.0177 | EVEN, no difference beyond the noise |
| host CPU-seconds | 344 | 350 | +1.6% | -21.7 to 32.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.96 | 4.01 | +1.2% | -0.203 to 0.297 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
