# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,938 | 2,939 | +0.0% | -8.4 to 10.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,953 | 2,953 | +0.0% | -10.7 to 11.4 | EVEN, no difference beyond the noise |
| queries a second | 2,953 | 2,953 | +0.0% | -10.7 to 11.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.355 | 0.353 | -0.6% | -0.0272 to 0.0232 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.546 | 0.54 | -1.2% | -0.0687 to 0.056 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.22 | +2.1% | -0.00516 to 0.0142 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -19.5 to 15 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 457 | -1.4% | -17.4 to 4.07 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,692 | 361,519 | -1.4% | -34,716 to 24,370 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.114 | +3.7% | -0.00419 to 0.0123 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 189 | +3.8% | -6.37 to 20.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.135 | 0.141 | +3.8% | -0.00488 to 0.0152 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 13 |  | 6.43 to 19.6 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
