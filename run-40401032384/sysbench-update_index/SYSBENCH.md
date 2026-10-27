# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 34.6 | 25.7 | -25.9% | -58 to 40 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 978 | 966 | -1.2% | -61.8 to 37.3 | EVEN, no difference beyond the noise |
| queries a second | 978 | 966 | -1.2% | -61.8 to 37.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 534 | 1,155 | +116.4% | -3,309 to 4,551 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,172 | 2,432 | +107.4% | -6,964 to 9,483 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 99.1 | 213 | +115.4% | -515 to 743 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | EVEN, the same |
| pages holding data, mean (MB) | 452 | 449 | -0.6% | -16.9 to 11 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 140,097 | 136,571 | -2.5% | -13,975 to 6,923 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.132 | -7.6% | -0.0269 to 0.00516 | EVEN, no difference beyond the noise |
| host CPU-seconds | 170 | 158 | -7.0% | -31.1 to 7.43 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 23.1 | 23.6 | +2.1% | -55.7 to 56.7 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
