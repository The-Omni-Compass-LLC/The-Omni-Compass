# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.1% | -2.78 to 2.17 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.1% | -2.76 to 2.37 | EVEN, no difference beyond the noise |
| queries a second | 4,720 | 4,717 | -0.1% | -44.1 to 37.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.91 | 3.86 | -1.2% | -0.147 to 0.0538 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.64 | 5.54 | -1.8% | -0.355 to 0.152 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.98 | 2.96 | -0.7% | -0.0549 to 0.0135 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 492 | -3.9% | -135 to 95.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 444 | -3.8% | -103 to 68.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 654,564 | 678,965 | +3.7% | -249,765 to 298,567 | shown, not judged |
| host CPU busy (share of the run) | 0.235 | 0.234 | -0.7% | -0.00526 to 0.00206 | EVEN, no difference beyond the noise |
| host CPU-seconds | 419 | 416 | -0.7% | -8.88 to 3.07 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.11 | 3.09 | -0.6% | -0.0423 to 0.00562 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 17 |  | 6.17 to 27.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
