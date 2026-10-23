# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 196 | 196 | -0.3% | -3.19 to 1.85 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.2% | -2.57 to 1.92 | EVEN, no difference beyond the noise |
| queries a second | 3,948 | 3,941 | -0.2% | -51.4 to 38.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.18 | -0.7% | -0.743 to 0.671 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 9.01 | 9.39 | +4.3% | -0.802 to 1.57 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.85 | 2.9 | +1.9% | -0.371 to 0.478 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 555 | +8.4% | -174 to 260 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 487 | +5.3% | -106 to 155 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,656 | 585,734 | -5.0% | -300,623 to 238,778 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.131 | -3.9% | -0.0195 to 0.00889 | EVEN, no difference beyond the noise |
| host CPU-seconds | 242 | 232 | -3.9% | -34.4 to 15.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.7 | 2.61 | -3.5% | -0.406 to 0.215 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.7 |  | 7.94 to 25.4 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
