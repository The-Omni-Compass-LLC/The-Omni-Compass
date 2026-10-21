# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 22.2 | 23.5 | +6.0% | -22.9 to 25.6 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 984 | 984 | -0.1% | -5.14 to 4.02 | EVEN, no difference beyond the noise |
| queries a second | 984 | 984 | -0.1% | -5.14 to 4.02 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.57 | 1.61 | +2.3% | -0.611 to 0.683 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.47 | 2.67 | +8.1% | -0.94 to 1.34 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.982 | 1 | +2.3% | -0.155 to 0.199 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 560 | +9.3% | -107 to 203 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 470 | +3.7% | -99 to 133 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,883 | 184,595 | -2.8% | -83,557 to 72,981 | shown, not judged |
| host CPU busy (share of the run) | 0.227 | 0.242 | +6.4% | -0.0933 to 0.122 | EVEN, no difference beyond the noise |
| host CPU-seconds | 399 | 424 | +6.3% | -161 to 212 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 41.9 | 62.2 | +48.3% | -86.4 to 127 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 19.7 |  | 13.9 to 25.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
