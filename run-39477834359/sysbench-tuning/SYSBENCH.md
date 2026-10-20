# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,948 | 2,948 | +0.0% | -7.57 to 7.85 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,953 | +0.0% | -7.56 to 9.18 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,953 | +0.0% | -7.56 to 9.18 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.33 | 0.32 | -3.0% | -0.0186 to -0.00139 | GAIN |
| latency, 99th percentile (ms) | 0.443 | 0.432 | -2.4% | -0.0221 to 0.000808 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.198 | 0.2 | +1.4% | -0.00844 to 0.0138 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 597 | +16.6% | -52.7 to 223 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 530 | +14.4% | -7.78 to 141 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,136 | 273,576 | -25.7% | -200,638 to 11,517 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.159 | -1.2% | -0.00722 to 0.00331 | EVEN, no difference beyond the noise |
| host CPU-seconds | 283 | 280 | -1.2% | -12.7 to 5.74 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.21 | 0.208 | -1.2% | -0.00979 to 0.00473 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.7 |  | 5.5 to 15.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
