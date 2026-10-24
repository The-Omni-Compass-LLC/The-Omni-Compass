# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,942 | 2,939 | -0.1% | -10.6 to 3.81 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,943 | 2,941 | -0.1% | -9.28 to 3.43 | EVEN, no difference beyond the noise |
| queries a second | 2,943 | 2,941 | -0.1% | -9.28 to 3.43 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.173 | 0.164 | -5.4% | -0.0181 to -0.000609 | GAIN |
| latency, 99th percentile (ms) | 0.361 | 0.346 | -4.1% | -0.0402 to 0.0108 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.113 | 0.117 | +4.2% | -0.0123 to 0.0218 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 418 | -18.4% | -171 to -16.9 | GAIN |
| pages holding data, mean (MB) | 464 | 384 | -17.2% | -159 to -0.265 | GAIN |
| pages read from disk into the pool (misses) | 368,588 | 473,304 | +28.4% | 8,633 to 200,799 | shown, not judged |
| host CPU busy (share of the run) | 0.0922 | 0.0923 | +0.0% | -0.00311 to 0.00319 | EVEN, no difference beyond the noise |
| host CPU-seconds | 167 | 167 | +0.0% | -5.48 to 5.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.124 | 0.124 | +0.2% | -0.00418 to 0.00456 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | -1.74 to 17.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
