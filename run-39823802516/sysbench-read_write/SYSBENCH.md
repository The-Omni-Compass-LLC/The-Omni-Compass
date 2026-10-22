# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 157 | 148 | -5.7% | -16.6 to -1.49 | LOSS |
| throughput (transactions a second) | 197 | 197 | +0.2% | -1.99 to 2.89 | EVEN, no difference beyond the noise |
| queries a second | 3,936 | 3,945 | +0.2% | -39.8 to 57.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 104 | 134 | +28.8% | 19 to 41.1 | LOSS |
| latency, 99th percentile (ms) | 267 | 316 | +18.6% | -84.7 to 184 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 20.1 | 25.8 | +28.5% | 1.56 to 9.9 | LOSS |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 513 | +0.3% | -131 to 134 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 461 | +0.0% | -116 to 116 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,332 | 610,100 | -1.0% | -193,241 to 180,777 | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.215 | -2.6% | -0.0134 to 0.0019 | EVEN, no difference beyond the noise |
| host CPU-seconds | 392 | 382 | -2.4% | -24 to 5.36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.45 | 5.65 | +3.6% | -0.239 to 0.63 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19 |  | 9.06 to 28.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
