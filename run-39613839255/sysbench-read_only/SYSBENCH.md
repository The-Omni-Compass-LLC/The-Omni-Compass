# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 296 | +0.2% | -2.45 to 3.89 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.3% | -2.5 to 4.09 | EVEN, no difference beyond the noise |
| queries a second | 4,732 | 4,745 | +0.3% | -40 to 65.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.07 | 2.08 | +0.3% | -0.496 to 0.508 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.79 | 3.86 | +1.8% | -0.227 to 0.367 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.33 | 1.34 | +0.6% | -0.142 to 0.157 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 363 | -29.0% | -266 to -31.2 | GAIN |
| pages holding data, mean (MB) | 461 | 335 | -27.3% | -250 to -1.57 | GAIN |
| pages read from disk into the pool (misses) | 654,860 | 1,035,429 | +58.1% | 25,588 to 735,549 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.108 | +0.5% | -0.0128 to 0.0139 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 193 | +0.5% | -22.9 to 24.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.43 | 1.43 | +0.2% | -0.183 to 0.191 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 6.87 to 14.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
