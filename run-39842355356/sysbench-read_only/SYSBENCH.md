# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.6% | 0.426 to 3.02 | GAIN |
| throughput (transactions a second) | 294 | 296 | +0.6% | 0.42 to 3.16 | GAIN |
| queries a second | 4,703 | 4,731 | +0.6% | 6.72 to 50.6 | GAIN |
| latency, 95th percentile (ms) | 4.13 | 4.1 | -0.6% | -0.133 to 0.0826 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.57 | 5.54 | -0.6% | -0.321 to 0.254 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.19 | 3.19 | +0.1% | -0.0382 to 0.0449 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 498 | -2.8% | -73.8 to 45.5 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 444 | -3.8% | -79.9 to 44.6 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 651,496 | 679,661 | +4.3% | -132,176 to 188,507 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.192 | +1.5% | -0.00168 to 0.00733 | EVEN, no difference beyond the noise |
| host CPU-seconds | 314 | 319 | +1.6% | -3.22 to 13 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.33 | 2.36 | +1.0% | -0.0477 to 0.0924 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 8.41 to 20.9 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
