# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 139 | 142 | +2.2% | -49.9 to 56.1 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 987 | -0.1% | -2.99 to 0.612 | EVEN, no difference beyond the noise |
| queries a second | 988 | 987 | -0.1% | -2.99 to 0.612 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 86.4 | 136 | +57.5% | -66.2 to 166 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 213 | 358 | +68.7% | -81.5 to 373 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 13.3 | 23 | +72.7% | -8.85 to 28.2 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 475 | -7.3% | -198 to 123 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 381 | -16.0% | -192 to 47 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 190,191 | 235,795 | +24.0% | 1,042 to 90,166 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.136 | -2.1% | -0.0185 to 0.0125 | EVEN, no difference beyond the noise |
| host CPU-seconds | 246 | 241 | -1.9% | -31.6 to 22 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.98 | 3.8 | -4.6% | -2.05 to 1.68 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17 |  | 9.55 to 24.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
