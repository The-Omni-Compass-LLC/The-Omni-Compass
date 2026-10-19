# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `bc2eb38f4ca8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 295 | -0.3% | -1.88 to 0.132 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.3% | -4.57 to 2.83 | EVEN, no difference beyond the noise |
| queries a second | 4,743 | 4,729 | -0.3% | -73.2 to 45.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.01 | 3.01 | -0.0% | -0.875 to 0.873 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.75 | 4.78 | +0.7% | -1.95 to 2.02 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.43 | 1.45 | +1.2% | -0.291 to 0.324 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 469 | -8.4% | -207 to 121 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 451 | 412 | -8.8% | -178 to 98.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 249,109 | 260,706 | +4.7% | -89,523 to 112,717 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.104 | +2.7% | -0.00276 to 0.00829 | EVEN, no difference beyond the noise |
| host CPU-seconds | 60.9 | 62.5 | +2.7% | -1.7 to 5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.35 | 1.39 | +3.0% | -0.0317 to 0.114 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6.33 |  | 1.16 to 11.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
