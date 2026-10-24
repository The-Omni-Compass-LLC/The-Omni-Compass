# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6.63 | 6.32 | -4.7% | -8.2 to 7.58 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 983 | +0.0% | -2.01 to 2.75 | EVEN, no difference beyond the noise |
| queries a second | 983 | 983 | +0.0% | -2.01 to 2.75 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.67 | 1.83 | +9.6% | -0.156 to 0.476 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.88 | 3.51 | +21.9% | -0.667 to 1.93 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 1.12 | +5.8% | -0.037 to 0.159 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 534 | +4.3% | -73.9 to 118 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 454 | +0.1% | -88.5 to 89.3 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,677 | 192,914 | +1.7% | -37,719 to 44,194 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.218 | +72.0% | -0.0893 to 0.272 | EVEN, no difference beyond the noise |
| host CPU-seconds | 195 | 337 | +73.2% | -141 to 426 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 65.1 | 125 | +92.6% | -100 to 221 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 21 |  | 8.09 to 33.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
