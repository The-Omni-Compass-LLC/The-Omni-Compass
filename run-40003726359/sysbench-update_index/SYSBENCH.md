# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1.18 | 0.923 | -21.9% | -2.51 to 2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 984 | +0.0% | -9.4 to 9.79 | EVEN, no difference beyond the noise |
| queries a second | 984 | 984 | +0.0% | -9.4 to 9.79 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.1 | 2.13 | +1.7% | -0.219 to 0.29 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.91 | 5.06 | +3.0% | 0.0231 to 0.276 | LOSS |
| latency, mean (ms) | 1.19 | 1.22 | +1.9% | -0.0193 to 0.0654 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.1% | -11.9 to 12.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 445 | -1.9% | -26.6 to 9.14 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 188,459 | 190,222 | +0.9% | -2,917 to 6,442 | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.127 | -2.3% | -0.035 to 0.0291 | EVEN, no difference beyond the noise |
| host CPU-seconds | 199 | 195 | -2.1% | -52.2 to 43.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 535 | 463 | -13.4% | -887 to 744 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.3 |  | 10.5 to 18.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
