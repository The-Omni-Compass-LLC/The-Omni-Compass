# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 7.29 | 6.1 | -16.3% | -7.05 to 4.68 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 986 | +0.3% | 2.25 to 2.83 | GAIN |
| queries a second | 983 | 986 | +0.3% | 2.25 to 2.83 | GAIN |
| latency, 95th percentile (ms) | 1.88 | 2.01 | +7.3% | -0.615 to 0.889 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.19 | 4.42 | +5.5% | -1.26 to 1.72 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.14 | -2.2% | -0.446 to 0.396 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 499 | -2.4% | -135 to 110 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 413 | -9.0% | -76.5 to -4.74 | GAIN |
| pages read from disk into the pool (misses) | 189,159 | 219,358 | +16.0% | 8,382 to 52,016 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.16 | +32.2% | -0.165 to 0.243 | EVEN, no difference beyond the noise |
| host CPU-seconds | 186 | 247 | +32.7% | -257 to 378 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 67.2 | 90.8 | +35.0% | -129 to 176 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19.7 |  | -0.414 to 39.7 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
