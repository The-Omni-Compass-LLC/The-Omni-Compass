# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 5.48 | 5.29 | -3.5% | -1.75 to 1.36 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 982 | 984 | +0.3% | -2.87 to 7.93 | EVEN, no difference beyond the noise |
| queries a second | 982 | 984 | +0.3% | -2.87 to 7.93 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.94 | 1.9 | -2.0% | -0.364 to 0.286 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.8 | 4.77 | -0.6% | -0.363 to 0.303 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.16 | 1.15 | -1.1% | -0.102 to 0.0762 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 454 | 451 | -0.7% | -15.1 to 9.09 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,178 | 186,783 | -1.3% | -10,789 to 6,000 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.114 | -4.1% | -0.0337 to 0.0239 | EVEN, no difference beyond the noise |
| host CPU-seconds | 184 | 176 | -4.1% | -51.1 to 36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 76.8 | 73.4 | -4.4% | -48.8 to 42.1 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
