# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 145 | 141 | -2.9% | -49.7 to 41.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 987 | 988 | +0.1% | -4.79 to 7.13 | EVEN, no difference beyond the noise |
| queries a second | 987 | 988 | +0.1% | -4.79 to 7.13 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 147 | 187 | +27.2% | -170 to 250 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 341 | 424 | +24.4% | -406 to 573 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 26.6 | 34.6 | +29.8% | -41.6 to 57.5 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,238 | +141.9% | 705 to 748 | power given |
| pages holding data, mean (MB) | 457 | 893 | +95.5% | 409 to 464 | power given |
| pages read from disk into the pool (misses) | 191,677 | 71,827 | -62.5% | -130,253 to -109,446 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.128 | -4.4% | -0.0225 to 0.0107 | EVEN, no difference beyond the noise |
| host CPU-seconds | 237 | 227 | -4.2% | -38.1 to 18.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.72 | 3.56 | -4.3% | -1.56 to 1.24 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
