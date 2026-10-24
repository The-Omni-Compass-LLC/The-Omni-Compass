# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 192 | +0.6% | -0.41 to 2.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.2% | -0.475 to 1.37 | EVEN, no difference beyond the noise |
| queries a second | 3,913 | 3,922 | +0.2% | -9.5 to 27.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7 | 6.9 | -1.5% | -1.97 to 1.77 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 126 | 71.4 | -43.3% | -166 to 56.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7.71 | 6.21 | -19.4% | -6.01 to 3.02 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 522 | +2.0% | -309 to 330 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 457 | -0.8% | -259 to 251 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,694 | 660,359 | +7.4% | -506,599 to 597,930 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.176 | +0.6% | -0.0158 to 0.018 | EVEN, no difference beyond the noise |
| host CPU-seconds | 315 | 317 | +0.6% | -28.5 to 32.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.58 | 3.58 | +0.0% | -0.342 to 0.344 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 12.5 to 17.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
