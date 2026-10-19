# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 294 | +0.4% | -1.1 to 3.31 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.3% | -1.36 to 2.83 | EVEN, no difference beyond the noise |
| queries a second | 4,703 | 4,715 | +0.3% | -21.7 to 45.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.41 | 5.18 | -4.1% | -0.361 to -0.0832 | GAIN |
| latency, 99th percentile (ms) | 7.52 | 7.17 | -4.7% | -0.547 to -0.159 | GAIN |
| latency, mean (ms) | 3.42 | 3.35 | -1.9% | -0.19 to 0.0624 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 479 | -6.5% | -123 to 56.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 445 | 400 | -10.1% | -119 to 29.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,823 | 256,619 | +5.2% | -41,694 to 67,286 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.197 | -0.7% | -0.0151 to 0.0122 | EVEN, no difference beyond the noise |
| host CPU-seconds | 110 | 109 | -0.7% | -8.24 to 6.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.45 | 2.43 | -1.0% | -0.174 to 0.123 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 5.52 to 10.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
