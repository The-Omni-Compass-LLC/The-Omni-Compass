# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.6% | -3.01 to 6.82 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 296 | +0.7% | -2.85 to 6.89 | EVEN, no difference beyond the noise |
| queries a second | 4,699 | 4,732 | +0.7% | -45.7 to 110 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.08 | 2.97 | -3.5% | -0.247 to 0.0289 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.6 | 4.62 | +0.6% | -0.211 to 0.267 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.42 | 1.43 | +0.9% | -0.063 to 0.0896 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 501 | -2.1% | -25.3 to 3.52 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 439 | -1.8% | -15.1 to -1.33 | GAIN |
| pages read from disk into the pool (misses) | 244,500 | 232,826 | -4.8% | -20,353 to -2,996 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.107 | +1.7% | -0.00319 to 0.00672 | EVEN, no difference beyond the noise |
| host CPU-seconds | 63 | 64.1 | +1.7% | -1.81 to 3.95 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.41 | 1.42 | +1.0% | -0.0653 to 0.0936 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
