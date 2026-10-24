# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 296 | +0.1% | -0.529 to 0.985 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.1% | -0.366 to 1.05 | EVEN, no difference beyond the noise |
| queries a second | 4,727 | 4,732 | +0.1% | -5.86 to 16.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.91 | 3.82 | -2.4% | -0.195 to 0.00917 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.15 | 5.09 | -1.2% | -0.195 to 0.0714 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.07 | 3.05 | -0.5% | -0.0532 to 0.0244 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 576 | +12.6% | -30 to 159 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 500 | +8.3% | -28.7 to 105 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,960 | 541,886 | -17.4% | -355,447 to 127,301 | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.18 | -0.3% | -0.0025 to 0.00141 | EVEN, no difference beyond the noise |
| host CPU-seconds | 299 | 299 | -0.3% | -4.56 to 2.92 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.22 | 2.21 | -0.4% | -0.0383 to 0.0222 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 22 |  | 17.7 to 26.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
