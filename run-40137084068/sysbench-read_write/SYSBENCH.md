# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 192 | +0.4% | -2.87 to 4.39 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.3% | -3.33 to 2.28 | EVEN, no difference beyond the noise |
| queries a second | 3,938 | 3,928 | -0.3% | -66.6 to 45.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.17 | 8.7 | -5.1% | -2.28 to 1.34 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 14 | 13 | -7.4% | -4.94 to 2.86 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.79 | 5.35 | -7.7% | -2.26 to 1.38 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 658 | +28.5% | -178 to 470 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 556 | +20.3% | -105 to 293 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 618,056 | 434,535 | -29.7% | -602,232 to 235,191 | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.206 | -2.1% | -0.0204 to 0.0115 | EVEN, no difference beyond the noise |
| host CPU-seconds | 339 | 332 | -2.0% | -32.1 to 18.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.87 | 3.78 | -2.4% | -0.44 to 0.254 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 20 |  | 7.09 to 32.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
