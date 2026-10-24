# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `7743f2e82851`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,956 | 2,958 | +0.1% | -9.02 to 12.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,964 | -0.0% | -6.33 to 3.8 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,964 | -0.0% | -6.33 to 3.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.209 | 0.203 | -2.9% | -0.0198 to 0.00783 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.354 | 0.346 | -2.4% | -0.0184 to 0.00171 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.271 | 0.173 | -36.3% | -0.445 to 0.248 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 409 | -20.2% | -214 to 7.33 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 374 | -19.3% | -181 to 2.29 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,147 | 495,478 | +34.6% | -37,240 to 291,902 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.11 | -1.3% | -0.00812 to 0.00515 | EVEN, no difference beyond the noise |
| host CPU-seconds | 199 | 196 | -1.3% | -14.5 to 9.21 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.148 | 0.146 | -1.4% | -0.0109 to 0.00674 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4.33 |  | -1.4 to 10.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
