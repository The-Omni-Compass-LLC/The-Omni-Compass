# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | +0.1% | -2.49 to 2.82 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | +0.1% | -2.69 to 3.16 | EVEN, no difference beyond the noise |
| queries a second | 4,698 | 4,702 | +0.1% | -43 to 50.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.86 | 2.74 | -4.1% | -0.38 to 0.144 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.57 | 4.38 | -4.1% | -0.414 to 0.0393 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.08 | 2.04 | -1.9% | -0.236 to 0.158 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 580 | +13.2% | -125 to 261 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 503 | +8.9% | -73.2 to 155 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 651,470 | 544,234 | -16.5% | -443,498 to 229,027 | shown, not judged |
| host CPU busy (share of the run) | 0.392 | 0.39 | -0.4% | -0.017 to 0.014 | EVEN, no difference beyond the noise |
| host CPU-seconds | 700 | 697 | -0.4% | -31.2 to 26 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 5.19 | 5.16 | -0.4% | -0.283 to 0.237 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15.3 |  | 11.5 to 19.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
