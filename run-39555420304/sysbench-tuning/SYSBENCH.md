# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,940 | 2,943 | +0.1% | -14 to 21.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,954 | +0.1% | -12.8 to 16 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,954 | +0.1% | -12.8 to 16 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.357 | 0.334 | -6.4% | -0.0307 to -0.0147 | GAIN |
| latency, 99th percentile (ms) | 0.505 | 0.479 | -5.2% | -0.0475 to -0.0052 | GAIN |
| latency, mean (ms) | 0.216 | 0.207 | -3.9% | -0.0141 to -0.00284 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 453 | -11.5% | -261 to 143 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 407 | -12.2% | -233 to 121 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,211 | 437,277 | +18.8% | -208,218 to 346,350 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.164 | -4.7% | -0.0165 to 0.000279 | EVEN, no difference beyond the noise |
| host CPU-seconds | 303 | 289 | -4.7% | -29.2 to 0.528 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.226 | 0.215 | -4.8% | -0.0207 to -0.00113 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 11 |  | 4.43 to 17.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
