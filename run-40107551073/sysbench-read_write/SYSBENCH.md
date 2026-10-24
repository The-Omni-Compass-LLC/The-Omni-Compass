# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 194 | -0.7% | -7.35 to 4.76 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 198 | +0.1% | -3.33 to 3.88 | EVEN, no difference beyond the noise |
| queries a second | 3,948 | 3,954 | +0.1% | -66.6 to 77.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.06 | 5.83 | +15.1% | -1.36 to 2.9 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.8 | 16.9 | +57.0% | -7.56 to 19.8 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.93 | 3.24 | +10.7% | -0.791 to 1.42 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 523 | +2.2% | -73.7 to 95.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 472 | +2.3% | -52.8 to 73.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,045 | 604,457 | -1.9% | -209,932 to 186,757 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.127 | +2.4% | -0.00182 to 0.00781 | EVEN, no difference beyond the noise |
| host CPU-seconds | 220 | 225 | +2.5% | -2.78 to 13.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.47 | 2.55 | +3.1% | -0.0694 to 0.224 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14 |  | 5.04 to 23 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
