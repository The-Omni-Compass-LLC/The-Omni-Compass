# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 21.2 | 21.6 | +1.9% | -5.84 to 6.65 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 986 | 983 | -0.4% | -6.33 to -0.599 | LOSS |
| queries a second | 986 | 983 | -0.4% | -6.33 to -0.599 | LOSS |
| latency, 95th percentile (ms) | 1.41 | 1.4 | -0.7% | -0.16 to 0.14 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2 | 2.02 | +1.2% | -0.48 to 0.527 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.95 | 0.939 | -1.2% | -0.0487 to 0.0264 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 476 | -7.1% | -114 to 42 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 453 | 408 | -10.0% | -114 to 23.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 189,240 | 214,359 | +13.3% | -38,722 to 88,961 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.111 | -1.9% | -0.0257 to 0.0214 | EVEN, no difference beyond the noise |
| host CPU-seconds | 174 | 171 | -1.7% | -38.7 to 32.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 18.5 | 18.5 | -0.1% | -2.92 to 2.89 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 18 |  | 8.06 to 27.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
