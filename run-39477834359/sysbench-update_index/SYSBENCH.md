# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 17.3 | 16.5 | -4.7% | -10.4 to 8.83 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 982 | 980 | -0.2% | -7.96 to 4.59 | EVEN, no difference beyond the noise |
| queries a second | 982 | 980 | -0.2% | -7.96 to 4.59 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.01 | 1.93 | -4.3% | -1.05 to 0.877 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.37 | 4.65 | -13.4% | -4.88 to 3.45 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.41 | 1.32 | -6.5% | -0.428 to 0.244 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 444 | -13.3% | -226 to 89.8 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 452 | 384 | -15.2% | -204 to 66 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 190,115 | 246,505 | +29.7% | -73,421 to 186,199 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.144 | -0.4% | -0.0252 to 0.0239 | EVEN, no difference beyond the noise |
| host CPU-seconds | 259 | 258 | -0.4% | -44.5 to 42.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 34.6 | 34.3 | -1.0% | -29.3 to 28.7 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 7.49 to 21.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 2.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
