# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,963 | 2,960 | -0.1% | -10.6 to 4.64 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,966 | 2,964 | -0.1% | -13.4 to 9.67 | EVEN, no difference beyond the noise |
| queries a second | 2,966 | 2,964 | -0.1% | -13.4 to 9.67 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.218 | 0.215 | -1.2% | -0.0234 to 0.018 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.352 | 0.352 | -0.1% | -0.0165 to 0.0158 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.169 | 0.179 | +5.8% | -0.0636 to 0.0833 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 401 | -21.7% | -236 to 13.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 463 | 366 | -20.9% | -195 to 1.16 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 367,194 | 501,193 | +36.5% | -54,068 to 322,066 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.115 | +1.7% | -0.00443 to 0.00833 | EVEN, no difference beyond the noise |
| host CPU-seconds | 201 | 205 | +1.7% | -7.83 to 14.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.149 | 0.152 | +1.8% | -0.00603 to 0.0114 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | -6.15 to 20.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
