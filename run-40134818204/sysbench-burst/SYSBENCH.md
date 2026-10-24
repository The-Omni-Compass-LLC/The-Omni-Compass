# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `7743f2e82851`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | -0.1% | -5.46 to 5.14 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.0% | -4.9 to 4.91 | EVEN, no difference beyond the noise |
| queries a second | 4,691 | 4,691 | +0.0% | -78.4 to 78.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.18 | 5.18 | +0.0% | -0.231 to 0.231 | EVEN, the same |
| latency, 99th percentile (ms) | 7.17 | 7.26 | +1.2% | -0.295 to 0.474 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.31 | 3.31 | -0.0% | -0.0677 to 0.067 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 528 | +3.2% | -53.9 to 86.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 448 | 445 | -0.6% | -103 to 97.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 244,350 | 233,036 | -4.6% | -73,532 to 50,904 | shown, not judged |
| host CPU busy (share of the run) | 0.189 | 0.193 | +2.1% | -0.0064 to 0.0142 | EVEN, no difference beyond the noise |
| host CPU-seconds | 104 | 107 | +2.4% | -3.34 to 8.34 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.39 | +2.3% | -0.0344 to 0.142 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
