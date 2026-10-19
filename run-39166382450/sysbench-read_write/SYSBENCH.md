# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 152 | 152 | -0.1% | -18.6 to 18.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 196 | 196 | -0.1% | -2.7 to 2.28 | EVEN, no difference beyond the noise |
| queries a second | 3,915 | 3,911 | -0.1% | -54 to 45.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 180 | 180 | +0.2% | -137 to 138 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 382 | 358 | -6.3% | -137 to 88.4 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 31.6 | 30 | -4.9% | -16.4 to 13.4 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 573 | +11.9% | -33.5 to 156 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 514 | +11.3% | -40.9 to 145 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 614,729 | 499,555 | -18.7% | -262,749 to 32,401 | shown, not judged |
| host CPU busy (share of the run) | 0.268 | 0.26 | -3.1% | -0.0365 to 0.0196 | EVEN, no difference beyond the noise |
| host CPU-seconds | 440 | 426 | -3.1% | -63.7 to 36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 6.34 | 6.13 | -3.3% | -1.63 to 1.21 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12.3 |  | 4.35 to 20.3 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 4.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
