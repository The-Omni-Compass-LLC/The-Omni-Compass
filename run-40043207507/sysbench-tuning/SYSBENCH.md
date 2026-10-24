# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,960 | -0.0% | -16.3 to 13.5 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,964 | 2,963 | -0.0% | -14.3 to 12.3 | EVEN, no difference beyond the noise |
| queries a second | 2,964 | 2,963 | -0.0% | -14.3 to 12.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.153 | 0.161 | +5.2% | -0.0971 to 0.113 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.327 | 0.332 | +1.6% | -0.0495 to 0.0601 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0898 | 0.0908 | +1.1% | -0.0453 to 0.0471 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 497 | -3.0% | -120 to 90.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 456 | -1.6% | -112 to 96.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,733 | 373,446 | +1.6% | -112,353 to 123,780 | shown, not judged |
| host CPU busy (share of the run) | 0.0696 | 0.0694 | -0.3% | -0.0358 to 0.0354 | EVEN, no difference beyond the noise |
| host CPU-seconds | 125 | 124 | -0.2% | -63.6 to 63 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0924 | 0.0922 | -0.2% | -0.0475 to 0.047 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8.33 |  | 5.46 to 11.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
