# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 190 | 192 | +0.7% | -0.828 to 3.42 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.0% | -0.838 to 0.769 | EVEN, no difference beyond the noise |
| queries a second | 3,927 | 3,926 | -0.0% | -16.8 to 15.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.28 | 8.74 | -5.8% | -1.15 to 0.0691 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.9 | 12.9 | -6.9% | -2.17 to 0.241 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.61 | 5.47 | -2.4% | -0.454 to 0.179 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 630 | +23.1% | 79.7 to 156 | power given |
| pages holding data, mean (MB) | 463 | 555 | +19.9% | 67.8 to 117 | power given |
| pages read from disk into the pool (misses) | 613,351 | 430,126 | -29.9% | -274,578 to -91,873 | shown, not judged |
| host CPU busy (share of the run) | 0.218 | 0.212 | -2.7% | -0.0159 to 0.00399 | EVEN, no difference beyond the noise |
| host CPU-seconds | 351 | 342 | -2.7% | -25.3 to 6.17 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.03 | 3.89 | -3.4% | -0.337 to 0.066 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18.7 |  | 13.5 to 23.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
