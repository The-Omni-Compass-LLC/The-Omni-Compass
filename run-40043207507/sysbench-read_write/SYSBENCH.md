# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 174 | 176 | +1.1% | -8.09 to 11.9 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 198 | 197 | -0.3% | -2.97 to 1.9 | EVEN, no difference beyond the noise |
| queries a second | 3,954 | 3,943 | -0.3% | -59.4 to 37.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 58.9 | 43.7 | -25.7% | -86.6 to 56.3 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 246 | 153 | -37.8% | -433 to 247 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 14.3 | 10.3 | -27.8% | -21.3 to 13.4 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 549 | +7.2% | -153 to 227 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 489 | +6.0% | -118 to 173 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,227 | 596,824 | -3.0% | -258,962 to 222,156 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.181 | -0.6% | -0.0105 to 0.0083 | EVEN, no difference beyond the noise |
| host CPU-seconds | 323 | 321 | -0.6% | -18.5 to 14.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.08 | 4 | -1.8% | -0.529 to 0.384 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13.7 |  | 9.87 to 17.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
