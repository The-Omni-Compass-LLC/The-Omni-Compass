# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 189 | 189 | +0.4% | -3.05 to 4.68 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.2% | -2 to 1.07 | EVEN, no difference beyond the noise |
| queries a second | 3,931 | 3,922 | -0.2% | -40 to 21.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 10.2 | 9.5 | -6.4% | -1.67 to 0.368 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 15.2 | 15.9 | +4.4% | -9.08 to 10.4 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.78 | 5.79 | +0.3% | -0.819 to 0.856 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 672 | +31.3% | -98.7 to 419 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 566 | +22.7% | -25.3 to 234 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 617,087 | 410,181 | -33.5% | -469,269 to 55,458 | shown, not judged |
| host CPU busy (share of the run) | 0.22 | 0.214 | -3.1% | -0.0114 to -0.00216 | GAIN |
| host CPU-seconds | 355 | 344 | -3.0% | -17 to -4.51 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.1 | 3.96 | -3.4% | -0.153 to -0.129 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 18.3 |  | 5.83 to 30.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
