# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 289 | 290 | +0.4% | -2.56 to 5.06 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 294 | +0.3% | -3.99 to 5.96 | EVEN, no difference beyond the noise |
| queries a second | 4,691 | 4,706 | +0.3% | -63.9 to 95.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.02 | 5.88 | -2.4% | -0.557 to 0.269 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.79 | 8.69 | -1.2% | -0.33 to 0.121 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.46 | 3.46 | +0.1% | -0.0668 to 0.0719 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 495 | -3.4% | -53.8 to 18.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 447 | 416 | -7.1% | -109 to 45.8 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,651 | 248,254 | +1.9% | -22,098 to 31,304 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.198 | +2.6% | -0.00508 to 0.0152 | EVEN, no difference beyond the noise |
| host CPU-seconds | 107 | 110 | +2.7% | -2.83 to 8.61 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.41 | 2.46 | +2.4% | -0.0392 to 0.154 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7.67 |  | 3.87 to 11.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
