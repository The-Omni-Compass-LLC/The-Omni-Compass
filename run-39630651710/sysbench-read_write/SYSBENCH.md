# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 193 | +0.2% | -1.55 to 2.35 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 195 | 195 | -0.0% | -2.22 to 2.12 | EVEN, no difference beyond the noise |
| queries a second | 3,905 | 3,904 | -0.0% | -44.4 to 42.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 7.04 | 7.05 | +0.1% | -0.84 to 0.858 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 11.9 | 10.9 | -7.8% | -4.28 to 2.43 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.93 | 3.95 | +0.5% | -0.315 to 0.354 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 523 | +2.2% | -67.8 to 90.3 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 461 | 473 | +2.5% | -51.2 to 74.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 618,608 | 588,118 | -4.9% | -194,777 to 133,795 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.182 | -0.9% | -0.0129 to 0.00958 | EVEN, no difference beyond the noise |
| host CPU-seconds | 340 | 337 | -1.0% | -24.1 to 17.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.83 | 3.79 | -1.1% | -0.284 to 0.196 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 9.5 to 19.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
