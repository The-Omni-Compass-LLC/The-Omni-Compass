# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 195 | 195 | +0.2% | -0.837 to 1.53 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | +0.1% | -1.86 to 2.24 | EVEN, no difference beyond the noise |
| queries a second | 3,923 | 3,927 | +0.1% | -37.2 to 44.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.67 | 6.47 | -2.9% | -0.935 to 0.543 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.2 | 9.97 | -2.4% | -1.55 to 1.06 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.42 | 4.39 | -0.7% | -0.119 to 0.0586 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 613 | +19.7% | -61.9 to 264 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 524 | +13.4% | -20.8 to 145 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 615,071 | 485,713 | -21.0% | -239,001 to -19,716 | shown, not judged |
| host CPU busy (share of the run) | 0.244 | 0.241 | -1.2% | -0.007 to 0.00116 | EVEN, no difference beyond the noise |
| host CPU-seconds | 431 | 426 | -1.2% | -12.6 to 2.47 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.83 | 4.77 | -1.4% | -0.122 to -0.00959 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 20.7 |  | 6.54 to 34.8 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
