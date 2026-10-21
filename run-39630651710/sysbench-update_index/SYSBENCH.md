# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 110 | 118 | +7.6% | 2.14 to 14.7 | GAIN |
| throughput (transactions a second) | 986 | 985 | -0.1% | -11.7 to 10.6 | EVEN, no difference beyond the noise |
| queries a second | 986 | 985 | -0.1% | -11.7 to 10.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 155 | 154 | -0.7% | -23.1 to 21.1 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 330 | 328 | -0.8% | -35 to 29.9 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 30.9 | 28 | -9.4% | -13.2 to 7.45 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 525 | +2.6% | -17 to 44 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 454 | 425 | -6.3% | -77.7 to 21 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 190,804 | 213,480 | +11.9% | -36,662 to 82,015 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.136 | +1.1% | -0.0226 to 0.0255 | EVEN, no difference beyond the noise |
| host CPU-seconds | 238 | 240 | +1.0% | -38.6 to 43.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.95 | 4.64 | -6.3% | -1.18 to 0.555 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 |  | 9.26 to 28.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
