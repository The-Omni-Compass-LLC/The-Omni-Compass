# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.62 | 4.09 | -38.2% | -5.58 to 0.523 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 985 | 983 | -0.1% | -2.6 to 0.311 | EVEN, no difference beyond the noise |
| queries a second | 985 | 983 | -0.1% | -2.6 to 0.311 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.22 | 2.53 | +13.8% | -0.0943 to 0.707 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.87 | 4.79 | +23.8% | -1.17 to 3.02 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.29 | 1.45 | +12.4% | -0.487 to 0.806 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.5% | 3.03 to 16.2 | power given |
| pages holding data, mean (MB) | 117 | 124 | +5.9% | 5.41 to 8.34 | power given |
| pages read from disk into the pool (misses) | 416,363 | 410,622 | -1.4% | -18,411 to 6,928 | shown, not judged |
| host CPU busy (share of the run) | 0.257 | 0.288 | +11.9% | -0.0333 to 0.0946 | EVEN, no difference beyond the noise |
| host CPU-seconds | 452 | 505 | +11.8% | -58.3 to 165 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 159 | 310 | +95.1% | -112 to 414 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
