# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `bc2eb38f4ca8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 191 | 192 | +0.6% | -0.836 to 3.12 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.0% | -0.524 to 0.657 | EVEN, no difference beyond the noise |
| queries a second | 3,930 | 3,932 | +0.0% | -10.5 to 13.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 9.17 | 8.63 | -5.8% | -1.54 to 0.469 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.4 | 12.8 | -4.1% | -1.46 to 0.356 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.45 | 5.38 | -1.4% | -0.142 to -0.00688 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 598 | +16.8% | 12.8 to 160 | power given |
| pages holding data, mean (MB) | 462 | 534 | +15.5% | 50 to 93.4 | power given |
| pages read from disk into the pool (misses) | 616,088 | 463,656 | -24.7% | -189,599 to -115,265 | shown, not judged |
| host CPU busy (share of the run) | 0.213 | 0.207 | -2.5% | -0.0124 to 0.00167 | EVEN, no difference beyond the noise |
| host CPU-seconds | 342 | 334 | -2.4% | -19.4 to 2.84 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.91 | 3.79 | -3.0% | -0.208 to -0.0269 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 17.7 |  | 13.9 to 21.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
