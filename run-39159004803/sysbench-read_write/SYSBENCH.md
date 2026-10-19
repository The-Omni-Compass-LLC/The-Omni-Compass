# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 185 | 180 | -2.6% | -18 to 8.48 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.4% | -4.79 to 3.13 | EVEN, no difference beyond the noise |
| queries a second | 3,956 | 3,939 | -0.4% | -95.8 to 62.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 23.8 | 33.5 | +40.9% | -38 to 57.4 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 153 | 171 | +11.2% | -36.1 to 70.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 9.49 | 10.7 | +13.1% | -0.696 to 3.19 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 137 | +6.8% | 5.89 to 11.5 | power given |
| pages holding data, mean (MB) | 122 | 128 | +5.4% | 1.56 to 11.5 | power given |
| pages read from disk into the pool (misses) | 1,671,699 | 1,613,168 | -3.5% | -140,504 to 23,443 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.205 | -0.8% | -0.00568 to 0.00248 | EVEN, no difference beyond the noise |
| host CPU-seconds | 366 | 363 | -0.7% | -9.56 to 4.13 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.34 | 4.42 | +1.8% | -0.222 to 0.382 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
