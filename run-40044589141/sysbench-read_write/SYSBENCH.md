# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 189 | 192 | +1.4% | 2.28 to 3.17 | GAIN |
| throughput (transactions a second) | 196 | 197 | +0.6% | -0.519 to 2.83 | EVEN, no difference beyond the noise |
| queries a second | 3,920 | 3,943 | +0.6% | -10.4 to 56.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.62 | 9.01 | -6.4% | -1.07 to -0.159 | GAIN |
| latency, 99th percentile (ms) | 15 | 13.6 | -9.0% | -3.1 to 0.397 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.01 | 5.57 | -7.2% | -0.782 to -0.0877 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 617 | +20.5% | 40.8 to 170 | power given |
| pages holding data, mean (MB) | 462 | 536 | +16.1% | 16.5 to 132 | power given |
| pages read from disk into the pool (misses) | 616,535 | 466,122 | -24.4% | -222,196 to -78,630 | shown, not judged |
| host CPU busy (share of the run) | 0.225 | 0.219 | -2.7% | -0.0117 to -0.000647 | GAIN |
| host CPU-seconds | 362 | 352 | -2.7% | -20.1 to 0.387 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.18 | 4.01 | -4.1% | -0.293 to -0.0501 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 19.3 |  | 14.2 to 24.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
