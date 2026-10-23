# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.86 | 6.55 | -4.6% | -4.16 to 3.53 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 983 | +0.1% | -3.46 to 4.89 | EVEN, no difference beyond the noise |
| queries a second | 983 | 983 | +0.1% | -3.46 to 4.89 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.68 | 1.7 | +1.0% | -0.232 to 0.265 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.06 | 3.23 | +5.5% | 0.0414 to 0.296 | LOSS |
| latency, mean (ms) | 1.04 | 1.06 | +1.2% | -0.0546 to 0.0797 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -45.4 to 24.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 429 | -5.5% | -72.3 to 22.7 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,751 | 202,439 | +7.3% | -25,156 to 52,530 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.134 | +7.3% | -0.0543 to 0.0727 | EVEN, no difference beyond the noise |
| host CPU-seconds | 193 | 207 | +7.5% | -83.3 to 112 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 63.6 | 74.1 | +16.7% | -2.76 to 23.9 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 |  | 13.2 to 23.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
