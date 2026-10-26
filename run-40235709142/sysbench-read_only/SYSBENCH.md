# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 293 | -0.2% | -1.99 to 0.777 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | -0.1% | -2.12 to 1.79 | EVEN, no difference beyond the noise |
| queries a second | 4,741 | 4,738 | -0.1% | -34 to 28.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.81 | 2.73 | -2.9% | -0.27 to 0.105 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.05 | 9.72 | +60.7% | -12.2 to 19.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.4 | 2.49 | +3.9% | -0.627 to 0.817 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 457 | -10.7% | -147 to 37.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 426 | -7.7% | -145 to 73.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 652,102 | 779,000 | +19.5% | -153,781 to 407,577 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.163 | +0.1% | -0.0103 to 0.0106 | EVEN, no difference beyond the noise |
| host CPU-seconds | 291 | 292 | +0.1% | -18 to 18.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.17 | 2.18 | +0.3% | -0.136 to 0.15 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 4.74 to 19.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
