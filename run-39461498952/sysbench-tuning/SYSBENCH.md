# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,962 | +0.0% | -7.79 to 9.34 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,965 | 2,966 | +0.0% | -5.54 to 7.78 | EVEN, no difference beyond the noise |
| queries a second | 2,965 | 2,966 | +0.0% | -5.54 to 7.78 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.169 | 0.163 | -3.6% | -0.0711 to 0.0591 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.334 | 0.326 | -2.3% | -0.0542 to 0.0388 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0968 | 0.0981 | +1.4% | -0.0263 to 0.029 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 460 | -10.1% | -100 to -3.08 | GAIN |
| pages holding data, mean (MB) | 463 | 419 | -9.5% | -87.8 to -0.0139 | GAIN |
| pages read from disk into the pool (misses) | 367,548 | 428,544 | +16.6% | 12,108 to 109,884 | shown, not judged |
| host CPU busy (share of the run) | 0.0735 | 0.0741 | +0.8% | -0.022 to 0.0232 | EVEN, no difference beyond the noise |
| host CPU-seconds | 132 | 133 | +0.8% | -39.3 to 41.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0976 | 0.0984 | +0.8% | -0.0289 to 0.0304 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 7.46 to 13.2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
