# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 21.9 | 21.7 | -1.2% | -5.73 to 5.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 986 | 984 | -0.2% | -3.48 to 0.287 | EVEN, no difference beyond the noise |
| queries a second | 986 | 984 | -0.2% | -3.48 to 0.287 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.48 | 1.55 | +4.5% | -0.0546 to 0.187 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.25 | 2.47 | +9.5% | -0.454 to 0.883 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.957 | 0.994 | +3.9% | -0.0633 to 0.137 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 478 | -6.7% | -97.6 to 29.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 398 | -12.2% | -150 to 38.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,771 | 223,612 | +18.5% | -32,318 to 102,000 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.139 | +23.1% | -0.0702 to 0.122 | EVEN, no difference beyond the noise |
| host CPU-seconds | 174 | 214 | +23.4% | -111 to 192 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 18 | 22.3 | +24.0% | -8.61 to 17.2 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 21.3 |  | 2.36 to 40.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
