# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 37.2 | 51.7 | +38.9% | -25.8 to 54.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 986 | 985 | -0.1% | -4.83 to 3.35 | EVEN, no difference beyond the noise |
| queries a second | 986 | 985 | -0.1% | -4.83 to 3.35 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 135 | 117 | -13.4% | -178 to 142 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 374 | 285 | -23.7% | -483 to 305 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 24.6 | 19.5 | -20.9% | -35.8 to 25.5 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 494 | -3.5% | -79.5 to 43.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 428 | -5.6% | -102 to 50.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,829 | 202,349 | +6.6% | -29,316 to 54,356 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.149 | -3.3% | -0.0128 to 0.00271 | EVEN, no difference beyond the noise |
| host CPU-seconds | 271 | 263 | -3.3% | -23.2 to 5.38 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 16.8 | 11.4 | -32.3% | -18.8 to 7.92 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 5.94 to 23.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
