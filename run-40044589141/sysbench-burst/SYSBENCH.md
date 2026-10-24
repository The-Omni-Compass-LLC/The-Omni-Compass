# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 291 | 292 | +0.2% | -5.66 to 6.72 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 294 | +0.5% | -1.47 to 4.4 | EVEN, no difference beyond the noise |
| queries a second | 4,677 | 4,701 | +0.5% | -23.6 to 70.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.15 | 5.34 | +3.7% | -0.289 to 0.672 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.21 | 7.78 | +7.9% | -1.6 to 2.73 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.31 | 3.46 | +4.5% | -0.361 to 0.659 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 474 | -7.5% | -174 to 96.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 449 | 405 | -9.8% | -157 to 69.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 242,140 | 257,686 | +6.4% | -50,636 to 81,727 | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.192 | +2.0% | -0.00106 to 0.00869 | EVEN, no difference beyond the noise |
| host CPU-seconds | 104 | 106 | +2.2% | -0.6 to 5.22 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.38 | +2.0% | -0.0143 to 0.11 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 2.03 to 12 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
