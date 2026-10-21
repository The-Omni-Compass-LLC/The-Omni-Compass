# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,953 | 2,948 | -0.2% | -10.9 to 0.112 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,967 | 2,963 | -0.1% | -6.52 to -0.581 | LOSS |
| queries a second | 2,967 | 2,963 | -0.1% | -6.52 to -0.581 | LOSS |
| latency, 95th percentile (ms) | 0.227 | 0.225 | -1.2% | -0.0178 to 0.0125 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.386 | 0.39 | +1.2% | -0.0154 to 0.0247 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.315 | 0.331 | +5.3% | -0.223 to 0.257 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 521 | +1.7% | -52.3 to 69.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 472 | +1.9% | -61.6 to 79.4 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,934 | 348,116 | -5.6% | -91,504 to 49,870 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.111 | +2.1% | -0.00776 to 0.0123 | EVEN, no difference beyond the noise |
| host CPU-seconds | 193 | 197 | +2.0% | -14.3 to 22 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.146 | +2.2% | -0.0103 to 0.0167 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 5.52 to 10.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
